interface Props {
  label: string
  value: string
  unit: string
}

export function KpiCard({ label, value, unit }: Props) {
  return (
    <div style={{
      background: 'var(--bg-surface)', border: '1px solid var(--border)',
      borderRadius: 'var(--radius-lg)', padding: '24px',
    }}>
      <p style={{ color: 'var(--text-secondary)', fontSize: 12, fontWeight: 600,
        textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: 8 }}>
        {label}
      </p>
      <p style={{ fontSize: 32, fontWeight: 700, lineHeight: 1 }}>{value}</p>
      <p style={{ color: 'var(--text-secondary)', fontSize: 12, marginTop: 4 }}>{unit}</p>
    </div>
  )
}
