interface Props {
  disabled: boolean
  loading: boolean
  onClick: () => void
}

export function RunButton({ disabled, loading, onClick }: Props) {
  return (
    <button
      disabled={disabled || loading}
      onClick={onClick}
      style={{
        padding: '12px 32px', fontSize: 15, fontWeight: 600,
        background: disabled || loading ? 'var(--bg-elevated)' : 'var(--accent)',
        color: disabled || loading ? 'var(--text-secondary)' : '#fff',
        border: 'none', borderRadius: 'var(--radius)', cursor: disabled || loading ? 'not-allowed' : 'pointer',
        transition: 'background 0.2s',
      }}
    >
      {loading ? 'Running…' : 'Run Analysis'}
    </button>
  )
}
