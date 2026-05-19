import io
import time
import sys
import os
from datetime import datetime, timezone

import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../src"))

from preprocessing import preprocess, validate_data
from analysis import kpi_metrics, peak_hour_analysis, demand_by_city
from prediction import train_and_evaluate
from sql_runner import run_queries_json

from api.schemas.analysis import (
    AnalysisResult, ResultMeta, KpiMetrics, PeakHourRow,
    CityDemandRow, MlResult, SqlResults,
)

PEAK_HOURS = frozenset(range(19, 23))
REQUIRED_COLUMNS = {"order_id", "order_time", "delivery_time", "distance_km", "order_value", "city"}


def run_full_pipeline(csv_bytes: bytes) -> AnalysisResult:
    start = time.monotonic()

    df = pd.read_csv(io.BytesIO(csv_bytes))

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = preprocess(df)
    validate_data(df)

    kpis = kpi_metrics(df)
    peak = peak_hour_analysis(df)
    city = demand_by_city(df)
    _, mae, r2 = train_and_evaluate(df)
    sql = run_queries_json(df)

    duration_ms = int((time.monotonic() - start) * 1000)

    return AnalysisResult(
        meta=ResultMeta(
            row_count=len(df),
            columns=list(df.columns),
            duration_ms=duration_ms,
            generated_at=datetime.now(timezone.utc).isoformat(),
        ),
        kpis=KpiMetrics(
            total_orders=int(kpis["total_orders"]),
            avg_delivery_time=round(kpis["avg_delivery_time"], 2),
            peak_delivery_time=round(kpis["peak_delivery_time"], 2),
            non_peak_delivery_time=round(kpis["non_peak_delivery_time"], 2),
        ),
        peak_hour_trend=[
            PeakHourRow(
                hour=int(row["hour"]),
                avg_delivery_duration=round(float(row["delivery_duration"]), 2),
                is_peak=int(row["hour"]) in PEAK_HOURS,
            )
            for _, row in peak.iterrows()
        ],
        city_demand=[
            CityDemandRow(city=str(row["city"]), total_orders=int(row["total_orders"]))
            for _, row in city.iterrows()
        ],
        ml=MlResult(
            model="LinearRegression",
            features=["distance_km", "hour", "is_peak_hour"],
            target="delivery_duration",
            mae=round(float(mae), 4),
            r2=round(float(r2), 4),
            test_size=0.2,
            random_seed=42,
        ),
        sql=SqlResults(
            delivery_by_hour=sql["delivery_by_hour"],
            peak_vs_non_peak=sql["peak_vs_non_peak"],
            city_performance=sql["city_performance"],
        ),
    )
