import { Navigate, Route, Routes } from 'react-router-dom'
import { AppShell } from './components/layout/AppShell'
import { UploadPage } from './pages/UploadPage'
import { OverviewPage } from './pages/OverviewPage'
import { ChartsPage } from './pages/ChartsPage'
import { MLResultsPage } from './pages/MLResultsPage'
import { SQLResultsPage } from './pages/SQLResultsPage'

export function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppShell />}>
        <Route index element={<Navigate to="/upload" replace />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/overview" element={<OverviewPage />} />
        <Route path="/charts" element={<ChartsPage />} />
        <Route path="/ml" element={<MLResultsPage />} />
        <Route path="/sql" element={<SQLResultsPage />} />
      </Route>
    </Routes>
  )
}
