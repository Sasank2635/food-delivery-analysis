import { useNavigate } from 'react-router-dom'

export function EmptyState() {
  const navigate = useNavigate()
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center',
      justifyContent: 'center', minHeight: 400, gap: 16, color: 'var(--text-secondary)' }}>
      <span style={{ fontSize: 48 }}>📊</span>
      <p style={{ fontSize: 16 }}>No analysis results yet</p>
      <button
        onClick={() => navigate('/upload')}
        style={{ padding: '10px 24px', background: 'var(--accent)', color: '#fff',
          border: 'none', borderRadius: 'var(--radius)', cursor: 'pointer', fontSize: 14 }}
      >
        Upload a CSV to get started
      </button>
    </div>
  )
}
