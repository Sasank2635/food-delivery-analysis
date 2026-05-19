import { render, screen } from '@testing-library/react'
import { KpiCard } from '../components/kpi/KpiCard'

it('renders label and formatted value', () => {
  render(<KpiCard label="Total Orders" value="10,000" unit="orders" />)
  expect(screen.getByText('Total Orders')).toBeTruthy()
  expect(screen.getByText('10,000')).toBeTruthy()
  expect(screen.getByText('orders')).toBeTruthy()
})
