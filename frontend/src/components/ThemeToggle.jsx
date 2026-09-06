import { useEffect, useState } from 'react'

const THEMES = [
  { value: 'light', label: 'Claro' },
  { value: 'dark', label: 'Oscuro' },
  { value: 'gruvbox', label: 'Vim (Gruvbox)' },
]

function ThemeToggle() {
  const [theme, setTheme] = useState(() => localStorage.getItem('theme') || 'light')

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('theme', theme)
  }, [theme])

  return (
    <select
      value={theme}
      onChange={(e) => setTheme(e.target.value)}
      className="bg-[var(--surface)] text-[var(--text)] border border-[var(--border)] rounded-md px-3 py-1.5 text-sm focus:outline-none focus:ring-2 focus:ring-[var(--primary)]"
    >
      {THEMES.map(t => (
        <option key={t.value} value={t.value}>{t.label}</option>
      ))}
    </select>
  )
}

export default ThemeToggle
