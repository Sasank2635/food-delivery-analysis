import { PeakHourChart } from '../components/charts/PeakHourChart'
import { CityDemandChart } from '../components/charts/CityDemandChart'
import { EmptyState } from '../components/common/EmptyState'
import { useAnalysis } from '../state/AnalysisContext'

export function ChartsPage() {
  const { state } = useAnalysis()
  if (!state.result) return <EmptyState />

  const { peak_hour_trend, city_demand } = state.result
  return (
    <div>
      <h1 style={{ marginBottom: 32, fontSize: 24, fontWeight: 700 }}>Charts</h1>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
        <PeakHourChart data={peak_hour_trend} />
        <CityDemandChart data={city_demand} />
      </div>
    </div>
  )
}
