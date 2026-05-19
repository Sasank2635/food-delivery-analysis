import { render, screen } from '@testing-library/react'
import { ResultTable } from '../components/sql/ResultTable'

it('infers columns from first row and renders data', () => {
  const rows = [
    { city: 'Mumbai', total_orders: 2000 },
    { city: 'Delhi', total_orders: 1800 },
  ]
  render(<ResultTable title="City Test" rows={rows} />)
  expect(screen.getByText('city')).toBeTruthy()
  expect(screen.getByText('Mumbai')).toBeTruthy()
  expect(screen.getByText('Delhi')).toBeTruthy()
})

it('shows empty message when no rows', () => {
  render(<ResultTable title="Empty" rows={[]} />)
  expect(screen.getByText('No data')).toBeTruthy()
})
