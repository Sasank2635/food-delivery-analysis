import type { AnalysisResult, ApiError } from '../types/analysis'

export class AnalysisApiError extends Error {
  constructor(public readonly apiError: ApiError) {
    super(apiError.message)
  }
}

export async function uploadCsv(file: File): Promise<AnalysisResult> {
  const form = new FormData()
  form.append('file', file)

  const res = await fetch('/api/analyze', { method: 'POST', body: form })
  const body = await res.json()

  if (!res.ok) {
    throw new AnalysisApiError(body.error as ApiError)
  }

  return body as AnalysisResult
}
