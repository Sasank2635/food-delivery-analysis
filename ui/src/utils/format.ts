export function formatMinutes(minutes: number): string {
  return `${minutes.toFixed(1)} min`
}

export function formatNumber(n: number): string {
  return n.toLocaleString()
}
