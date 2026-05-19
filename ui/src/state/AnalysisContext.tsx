import { createContext, useContext, useReducer, useCallback } from 'react'
import type { ReactNode } from 'react'
import type { AnalysisResult, ApiError } from '../types/analysis'
import { uploadCsv, AnalysisApiError } from '../api/client'

type Status = 'idle' | 'loading' | 'success' | 'error'

interface AnalysisState {
  status: Status
  result: AnalysisResult | null
  error: ApiError | null
  fileName: string | null
}

type Action =
  | { type: 'START'; fileName: string }
  | { type: 'SUCCESS'; payload: AnalysisResult }
  | { type: 'FAILURE'; error: ApiError }
  | { type: 'RESET' }

function reducer(state: AnalysisState, action: Action): AnalysisState {
  switch (action.type) {
    case 'START':
      return { status: 'loading', result: null, error: null, fileName: action.fileName }
    case 'SUCCESS':
      return { status: 'success', result: action.payload, error: null, fileName: state.fileName }
    case 'FAILURE':
      return { status: 'error', result: null, error: action.error, fileName: state.fileName }
    case 'RESET':
      return { status: 'idle', result: null, error: null, fileName: null }
    default:
      return state
  }
}

const initialState: AnalysisState = { status: 'idle', result: null, error: null, fileName: null }

interface AnalysisContextValue {
  state: AnalysisState
  runAnalysis: (file: File) => Promise<void>
  reset: () => void
}

const AnalysisContext = createContext<AnalysisContextValue | null>(null)

export function AnalysisProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(reducer, initialState)

  const runAnalysis = useCallback(async (file: File) => {
    dispatch({ type: 'START', fileName: file.name })
    try {
      const result = await uploadCsv(file)
      dispatch({ type: 'SUCCESS', payload: result })
    } catch (err) {
      const apiError = err instanceof AnalysisApiError
        ? err.apiError
        : { code: 'UNKNOWN', message: String(err) }
      dispatch({ type: 'FAILURE', error: apiError })
    }
  }, [])

  const reset = useCallback(() => dispatch({ type: 'RESET' }), [])

  return (
    <AnalysisContext.Provider value={{ state, runAnalysis, reset }}>
      {children}
    </AnalysisContext.Provider>
  )
}

export function useAnalysis(): AnalysisContextValue {
  const ctx = useContext(AnalysisContext)
  if (!ctx) throw new Error('useAnalysis must be used inside AnalysisProvider')
  return ctx
}
