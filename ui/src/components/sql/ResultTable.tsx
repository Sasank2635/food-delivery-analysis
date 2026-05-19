interface Props {
  title: string
  rows: Record<string, unknown>[]
}

export function ResultTable({ title, rows }: Props) {
  const columns = rows.length > 0 ? Object.keys(rows[0]) : []

  return (
    <div style={{ background: 'var(--bg-surface)', border: '1px solid var(--border)',
      borderRadius: 'var(--radius-lg)', padding: 24 }}>
      <h3 style={{ marginBottom: 16, fontSize: 15, fontWeight: 600 }}>{title}</h3>
      {rows.length === 0
        ? <p style={{ color: 'var(--text-secondary)' }}>No data</p>
        : (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
              <thead>
                <tr>
                  {columns.map(col => (
                    <th key={col} style={{ textAlign: 'left', padding: '8px 12px',
                      borderBottom: '1px solid var(--border)', color: 'var(--text-secondary)',
                      fontWeight: 600, textTransform: 'uppercase', fontSize: 11 }}>
                      {col}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {rows.map((row, i) => (
                  <tr key={i} style={{ borderBottom: '1px solid var(--border)' }}>
                    {columns.map(col => (
                      <td key={col} style={{ padding: '8px 12px' }}>
                        {typeof row[col] === 'number'
                          ? (row[col] as number).toLocaleString(undefined, { maximumFractionDigits: 2 })
                          : String(row[col] ?? '')}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )
      }
    </div>
  )
}
