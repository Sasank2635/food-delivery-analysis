import io
import pandas as pd
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def _make_csv_bytes() -> bytes:
    df = pd.DataFrame({
        "order_id": range(20),
        "order_time": ["2024-01-01 19:00:00"] * 10 + ["2024-01-01 10:00:00"] * 10,
        "delivery_time": ["2024-01-01 20:00:00"] * 10 + ["2024-01-01 10:40:00"] * 10,
        "distance_km": [5.0] * 20,
        "order_value": [200.0] * 20,
        "city": ["Mumbai"] * 10 + ["Delhi"] * 10,
    })
    buf = io.BytesIO()
    df.to_csv(buf, index=False)
    return buf.getvalue()


def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_analyze_success():
    r = client.post(
        "/api/analyze",
        files={"file": ("orders.csv", _make_csv_bytes(), "text/csv")},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["kpis"]["total_orders"] == 20
    assert "peak_hour_trend" in body
    assert "city_demand" in body
    assert "ml" in body
    assert "sql" in body


def test_analyze_rejects_non_csv():
    r = client.post(
        "/api/analyze",
        files={"file": ("data.xlsx", b"fake", "application/octet-stream")},
    )
    assert r.status_code == 400
    assert r.json()["error"]["code"] == "INVALID_EXT"


def test_analyze_rejects_missing_column():
    bad_csv = b"order_id,order_time\n1,2024-01-01"
    r = client.post(
        "/api/analyze",
        files={"file": ("orders.csv", bad_csv, "text/csv")},
    )
    assert r.status_code == 400
    assert r.json()["error"]["code"] == "INVALID_SCHEMA"
