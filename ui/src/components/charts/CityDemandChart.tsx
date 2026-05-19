import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
} from 'recharts'
import type { CityDemandRow } from '../../types/analysis'

interface Props { data: CityDemandRow[] }

export function CityDemandChart({ data }: Props) {
  const sorted = [...data].sort((a, b) => b.total_orders - a.total_orders)
  return (
    <div style={{ background: 'var(--bg-surface)', border: '1px solid var(--border)',
      borderRadius: 'var(--radius-lg)', padding: 24 }}>
      <h3 style={{ marginBottom: 16, fontSize: 16, fontWeight: 600 }}>Total Orders by City</h3>
      <ResponsiveContainer width="100%" height={280}>
        <BarChart data={sorted}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
          <XAxis dataKey="city" stroke="var(--text-secondary)" />
          <YAxis stroke="var(--text-secondary)" />
          <Tooltip
            contentStyle={{ background: 'var(--bg-elevated)', border: '1px solid var(--border)', borderRadius: 6 }}
            formatter={(v: number) => [v.toLocaleString(), 'Orders']}
          />
          <Bar dataKey="total_orders" fill="var(--accent)" radius={[4, 4, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
