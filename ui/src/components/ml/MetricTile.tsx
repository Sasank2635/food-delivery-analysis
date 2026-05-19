interface Props { label: string; value: string; description: string }

export function MetricTile({ label, value, description }: Props) {
  return (
    <div style={{ background: 'var(--bg-surface)', border: '1px solid var(--border)',
      borderRadius: 'var(--radius-lg)', padding: 32, textAlign: 'center' }}>
      <p style={{ color: 'var(--text-secondary)', fontSize: 12, fontWeight: 600,
        textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 8 }}>{label}</p>
      <p style={{ fontSize: 48, fontWeight: 800, color: 'var(--accent)', lineHeight: 1 }}>{value}</p>
      <p style={{ color: 'var(--text-secondary)', fontSize: 12, marginTop: 8 }}>{description}</p>
    </div>
  )
}
