import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Dropzone } from '../components/upload/Dropzone'
import { RunButton } from '../components/upload/RunButton'
import { LoadingOverlay } from '../components/common/LoadingOverlay'
import { useAnalysis } from '../state/AnalysisContext'

export function UploadPage() {
  const [file, setFile] = useState<File | null>(null)
  const { state, runAnalysis } = useAnalysis()
  const navigate = useNavigate()

  const handleRun = async () => {
    if (!file) return
    await runAnalysis(file)
    navigate('/overview')
  }

  return (
    <div style={{ maxWidth: 600 }}>
      {state.status === 'loading' && <LoadingOverlay />}
      <h1 style={{ marginBottom: 8, fontSize: 24, fontWeight: 700 }}>Upload Data</h1>
      <p style={{ color: 'var(--text-secondary)', marginBottom: 32 }}>
        Upload a CSV with columns: order_id, order_time, delivery_time, distance_km, order_value, city
      </p>
      <Dropzone onFile={setFile} fileName={file?.name ?? null} />
      <div style={{ marginTop: 24 }}>
        <RunButton disabled={!file} loading={state.status === 'loading'} onClick={handleRun} />
      </div>
    </div>
  )
}
