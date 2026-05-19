import { MetricTile } from '../components/ml/MetricTile'
import { EmptyState } from '../components/common/EmptyState'
import { useAnalysis } from '../state/AnalysisContext'

export function MLResultsPage() {
  const { state } = useAnalysis()
  if (!state.result) return <EmptyState />

  const { ml } = state.result
  return (
    <div>
      <h1 style={{ marginBottom: 8, fontSize: 24, fontWeight: 700 }}>ML Results</h1>
      <p style={{ color: 'var(--text-secondary)', marginBottom: 32 }}>
        Model: {ml.model} — Features: {ml.features.join(', ')} → {ml.target}
      </p>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, maxWidth: 600 }}>
        <MetricTile label="MAE" value={ml.mae.toFixed(2)} description="Mean Absolute Error (minutes)" />
        <MetricTile label="R²" value={ml.r2.toFixed(3)} description="Coefficient of Determination" />
      </div>
    </div>
  )
}
