import { KpiCard } from '../components/kpi/KpiCard'
import { EmptyState } from '../components/common/EmptyState'
import { useAnalysis } from '../state/AnalysisContext'
import { formatMinutes, formatNumber } from '../utils/format'

export function OverviewPage() {
  const { state } = useAnalysis()
  if (!state.result) return <EmptyState />

  const { kpis } = state.result
  return (
    <div>
      <h1 style={{ marginBottom: 8, fontSize: 24, fontWeight: 700 }}>Overview</h1>
      <p style={{ color: 'var(--text-secondary)', marginBottom: 32 }}>
        File: {state.fileName}
      </p>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 16 }}>
        <KpiCard label="Total Orders" value={formatNumber(kpis.total_orders)} unit="orders" />
        <KpiCard label="Avg Delivery Time" value={formatMinutes(kpis.avg_delivery_time)} unit="per order" />
        <KpiCard label="Peak Delivery Time" value={formatMinutes(kpis.peak_delivery_time)} unit="19:00–22:00" />
        <KpiCard label="Non-Peak Delivery" value={formatMinutes(kpis.non_peak_delivery_time)} unit="outside peak" />
      </div>
    </div>
  )
}
