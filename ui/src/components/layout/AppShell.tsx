import { Outlet } from 'react-router-dom'
import { NavTabs } from './NavTabs'
import { ErrorBanner } from '../common/ErrorBanner'

export function AppShell() {
  return (
    <div style={{ display: 'flex', minHeight: '100vh' }}>
      <NavTabs />
      <main style={{ flex: 1, padding: 32, maxWidth: 1200, overflowY: 'auto' }}>
        <ErrorBanner />
        <Outlet />
      </main>
    </div>
  )
}
