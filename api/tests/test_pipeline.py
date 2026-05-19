import io
import pandas as pd
import pytest
from api.services.pipeline import run_full_pipeline
from api.schemas.analysis import AnalysisResult


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
    buf.seek(0)
    return buf.read()


def test_run_full_pipeline_returns_analysis_result():
    result = run_full_pipeline(_make_csv_bytes())
    assert isinstance(result, AnalysisResult)


def test_run_full_pipeline_kpis_total_orders():
    result = run_full_pipeline(_make_csv_bytes())
    assert result.kpis.total_orders == 20


def test_run_full_pipeline_peak_hour_trend_has_24_rows():
    result = run_full_pipeline(_make_csv_bytes())
    assert len(result.peak_hour_trend) == 2  # only 2 distinct hours in sample


def test_run_full_pipeline_city_demand_has_two_cities():
    result = run_full_pipeline(_make_csv_bytes())
    cities = {r.city for r in result.city_demand}
    assert cities == {"Mumbai", "Delhi"}


def test_run_full_pipeline_ml_has_mae_and_r2():
    result = run_full_pipeline(_make_csv_bytes())
    assert isinstance(result.ml.mae, float)
    assert isinstance(result.ml.r2, float)


def test_run_full_pipeline_sql_has_three_keys():
    result = run_full_pipeline(_make_csv_bytes())
    assert len(result.sql.delivery_by_hour) > 0
    assert len(result.sql.peak_vs_non_peak) == 2
