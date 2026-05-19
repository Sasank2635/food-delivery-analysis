export function LoadingOverlay() {
  return (
    <div style={{
      position: 'fixed', inset: 0, background: 'rgba(15,17,23,0.85)',
      display: 'flex', flexDirection: 'column', alignItems: 'center',
      justifyContent: 'center', gap: 16, zIndex: 999,
    }}>
      <div style={{
        width: 40, height: 40, border: '3px solid var(--border)',
        borderTopColor: 'var(--accent)', borderRadius: '50%',
        animation: 'spin 0.8s linear infinite',
      }} />
      <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
      <p style={{ color: 'var(--text-secondary)' }}>Running analysis…</p>
    </div>
  )
}
