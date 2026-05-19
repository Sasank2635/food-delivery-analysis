import pandas as pd
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))
from sql_runner import run_queries_json


def _sample_df():
    return pd.DataFrame({
        "order_id": range(10),
        "order_time": ["2024-01-01 19:00:00"] * 5 + ["2024-01-01 10:00:00"] * 5,
        "delivery_time": ["2024-01-01 20:00:00"] * 5 + ["2024-01-01 10:40:00"] * 5,
        "distance_km": [5.0] * 10,
        "order_value": [200.0] * 10,
        "city": ["Mumbai"] * 5 + ["Delhi"] * 5,
    })


def test_run_queries_json_returns_three_keys():
    result = run_queries_json(_sample_df())
    assert set(result.keys()) == {"delivery_by_hour", "peak_vs_non_peak", "city_performance"}


def test_run_queries_json_peak_vs_non_peak_has_two_rows():
    result = run_queries_json(_sample_df())
    assert len(result["peak_vs_non_peak"]) == 2


def test_run_queries_json_city_performance_has_two_cities():
    result = run_queries_json(_sample_df())
    cities = {row["city"] for row in result["city_performance"]}
    assert cities == {"Mumbai", "Delhi"}


def test_run_queries_json_rows_are_dicts():
    result = run_queries_json(_sample_df())
    assert isinstance(result["delivery_by_hour"][0], dict)
