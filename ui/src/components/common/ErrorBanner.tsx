import { useAnalysis } from '../../state/AnalysisContext'

export function ErrorBanner() {
  const { state, reset } = useAnalysis()
  if (!state.error) return null
  return (
    <div style={{
      background: '#3f1515', border: '1px solid var(--danger)',
      borderRadius: 'var(--radius)', padding: '12px 16px', marginBottom: 24,
      display: 'flex', justifyContent: 'space-between', alignItems: 'center',
    }}>
      <span style={{ color: '#fca5a5' }}>
        <strong>{state.error.code}:</strong> {state.error.message}
      </span>
      <button onClick={reset} style={{ background: 'none', border: 'none',
        color: 'var(--text-secondary)', cursor: 'pointer', fontSize: 18 }}>×</button>
    </div>
  )
}
