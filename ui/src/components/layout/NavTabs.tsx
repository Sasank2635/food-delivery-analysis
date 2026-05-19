import { NavLink } from 'react-router-dom'
import { useAnalysis } from '../../state/AnalysisContext'

const TABS = [
  { to: '/upload', label: 'Upload', always: true },
  { to: '/overview', label: 'Overview', always: false },
  { to: '/charts', label: 'Charts', always: false },
  { to: '/ml', label: 'ML Results', always: false },
  { to: '/sql', label: 'SQL Results', always: false },
]

export function NavTabs() {
  const { state } = useAnalysis()
  const hasResult = state.result !== null

  return (
    <nav style={{
      display: 'flex', flexDirection: 'column', gap: 4,
      padding: '16px 12px', minWidth: 160,
      background: 'var(--bg-surface)', borderRight: '1px solid var(--border)',
    }}>
      <span style={{ fontSize: 11, fontWeight: 700, letterSpacing: '0.08em',
        color: 'var(--text-secondary)', padding: '8px 8px 12px', textTransform: 'uppercase' }}>
        Dashboard
      </span>
      {TABS.map(tab => (
        <NavLink
          key={tab.to}
          to={tab.to}
          style={({ isActive }) => ({
            padding: '8px 12px', borderRadius: 'var(--radius)',
            color: isActive ? 'var(--accent)' : tab.always || hasResult ? 'var(--text-primary)' : 'var(--text-secondary)',
            background: isActive ? 'var(--bg-elevated)' : 'transparent',
            pointerEvents: tab.always || hasResult ? 'auto' : 'none',
            opacity: tab.always || hasResult ? 1 : 0.4,
            fontSize: 13,
          })}
        >
          {tab.label}
        </NavLink>
      ))}
    </nav>
  )
}
