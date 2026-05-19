export interface KpiMetrics {
  total_orders: number
  avg_delivery_time: number
  peak_delivery_time: number
  non_peak_delivery_time: number
}

export interface PeakHourRow {
  hour: number
  avg_delivery_duration: number
  is_peak: boolean
}

export interface CityDemandRow {
  city: string
  total_orders: number
}

export interface MlResult {
  model: string
  features: string[]
  target: string
  mae: number
  r2: number
  test_size: number
  random_seed: number
}

export interface SqlResults {
  delivery_by_hour: Record<string, unknown>[]
  peak_vs_non_peak: Record<string, unknown>[]
  city_performance: Record<string, unknown>[]
}

export interface ResultMeta {
  row_count: number
  columns: string[]
  duration_ms: number
  generated_at: string
}

export interface AnalysisResult {
  meta: ResultMeta
  kpis: KpiMetrics
  peak_hour_trend: PeakHourRow[]
  city_demand: CityDemandRow[]
  ml: MlResult
  sql: SqlResults
}

export interface ApiError {
  code: string
  message: string
}
