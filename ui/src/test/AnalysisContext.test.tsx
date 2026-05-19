import { render, screen } from '@testing-library/react'
import { AnalysisProvider, useAnalysis } from '../state/AnalysisContext'

function StatusDisplay() {
  const { state } = useAnalysis()
  return <div data-testid="status">{state.status}</div>
}

it('starts with idle status', () => {
  render(<AnalysisProvider><StatusDisplay /></AnalysisProvider>)
  expect(screen.getByTestId('status').textContent).toBe('idle')
})
