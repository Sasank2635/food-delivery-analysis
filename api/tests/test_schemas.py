from api.schemas.analysis import AnalysisResult, KpiMetrics, PeakHourRow, CityDemandRow, MlResult, SqlResults, SqlRow


def test_kpi_metrics_fields():
    kpi = KpiMetrics(
        total_orders=10000,
        avg_delivery_time=38.4,
        peak_delivery_time=47.1,
        non_peak_delivery_time=35.9,
    )
    assert kpi.total_orders == 10000
    assert kpi.avg_delivery_time == 38.4


def test_peak_hour_row_is_peak_flag():
    row = PeakHourRow(hour=19, avg_delivery_duration=48.2, is_peak=True)
    assert row.is_peak is True


def test_analysis_result_roundtrip():
    result = AnalysisResult(
        meta={"row_count": 100, "columns": ["a"], "duration_ms": 500, "generated_at": "2026-05-19T00:00:00Z"},
        kpis=KpiMetrics(total_orders=100, avg_delivery_time=38.0, peak_delivery_time=47.0, non_peak_delivery_time=35.0),
        peak_hour_trend=[PeakHourRow(hour=0, avg_delivery_duration=32.1, is_peak=False)],
        city_demand=[CityDemandRow(city="Mumbai", total_orders=2000)],
        ml=MlResult(model="LinearRegression", features=["distance_km"], target="delivery_duration",
                    mae=4.2, r2=0.81, test_size=0.2, random_seed=42),
        sql=SqlResults(delivery_by_hour=[], peak_vs_non_peak=[], city_performance=[]),
    )
    assert result.kpis.total_orders == 100
