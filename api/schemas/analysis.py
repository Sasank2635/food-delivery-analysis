from pydantic import BaseModel


class KpiMetrics(BaseModel):
    total_orders: int
    avg_delivery_time: float
    peak_delivery_time: float
    non_peak_delivery_time: float


class PeakHourRow(BaseModel):
    hour: int
    avg_delivery_duration: float
    is_peak: bool


class CityDemandRow(BaseModel):
    city: str
    total_orders: int


class MlResult(BaseModel):
    model: str
    features: list[str]
    target: str
    mae: float
    r2: float
    test_size: float
    random_seed: int


class SqlRow(BaseModel):
    model_config = {"extra": "allow"}


class SqlResults(BaseModel):
    delivery_by_hour: list[dict]
    peak_vs_non_peak: list[dict]
    city_performance: list[dict]


class ResultMeta(BaseModel):
    row_count: int
    columns: list[str]
    duration_ms: int
    generated_at: str


class AnalysisResult(BaseModel):
    meta: ResultMeta
    kpis: KpiMetrics
    peak_hour_trend: list[PeakHourRow]
    city_demand: list[CityDemandRow]
    ml: MlResult
    sql: SqlResults
