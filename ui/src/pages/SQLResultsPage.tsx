import { ResultTable } from '../components/sql/ResultTable'
import { EmptyState } from '../components/common/EmptyState'
import { useAnalysis } from '../state/AnalysisContext'

export function SQLResultsPage() {
  const { state } = useAnalysis()
  if (!state.result) return <EmptyState />

  const { sql } = state.result
  return (
    <div>
      <h1 style={{ marginBottom: 32, fontSize: 24, fontWeight: 700 }}>SQL Results</h1>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
        <ResultTable title="Delivery by Hour" rows={sql.delivery_by_hour} />
        <ResultTable title="Peak vs Non-Peak" rows={sql.peak_vs_non_peak} />
        <ResultTable title="City Performance" rows={sql.city_performance} />
      </div>
    </div>
  )
}
