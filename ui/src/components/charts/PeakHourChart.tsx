import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip,
  ReferenceArea, ResponsiveContainer,
} from 'recharts'
import type { PeakHourRow } from '../../types/analysis'

interface Props { data: PeakHourRow[] }

export function PeakHourChart({ data }: Props) {
  return (
    <div style={{ background: 'var(--bg-surface)', border: '1px solid var(--border)',
      borderRadius: 'var(--radius-lg)', padding: 24 }}>
      <h3 style={{ marginBottom: 16, fontSize: 16, fontWeight: 600 }}>Avg Delivery Duration by Hour</h3>
      <ResponsiveContainer width="100%" height={280}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
          <XAxis dataKey="hour" stroke="var(--text-secondary)"
            tickFormatter={(h: number) => `${String(h).padStart(2, '0')}:00`} />
          <YAxis stroke="var(--text-secondary)" unit=" min" />
          <Tooltip
            contentStyle={{ background: 'var(--bg-elevated)', border: '1px solid var(--border)', borderRadius: 6 }}
            labelFormatter={(h: number) => `${String(h).padStart(2, '0')}:00`}
            formatter={(v: number) => [`${v.toFixed(1)} min`, 'Avg Duration']}
          />
          <ReferenceArea x1={19} x2={22} fill="var(--warning)" fillOpacity={0.1}
            label={{ value: 'Peak', fill: 'var(--warning)', fontSize: 11 }} />
          <Line type="monotone" dataKey="avg_delivery_duration"
            stroke="var(--accent)" strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
