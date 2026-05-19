import { BrowserRouter } from 'react-router-dom'
import { AnalysisProvider } from './state/AnalysisContext'
import { AppRoutes } from './routes'

export default function App() {
  return (
    <BrowserRouter>
      <AnalysisProvider>
        <AppRoutes />
      </AnalysisProvider>
    </BrowserRouter>
  )
}
