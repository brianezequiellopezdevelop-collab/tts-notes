import { useState, useEffect } from 'react'

import ThemeToggle from './components/ThemeToggle'
import NoteList from './components/NoteList'
import NoteForm from './components/NoteForm'
import DocumentList from './components/DocumentList'
import DocumentUpload from './components/DocumentUpload'

function App() {
  const [activeTab, setActiveTab] = useState('notes')
  const [notesRefreshKey, setNotesRefreshKey] = useState(0)
  const [docsRefreshKey, setDocsRefreshKey] = useState(0)
  const interval = setInterval(sendHeartbeat, 3000)
  return () => clearInterval(interval)
}, [])
  return (
    <div className="min-h-screen bg-[var(--bg)] text-[var(--text)] transition-colors duration-300">
      <div className="max-w-2xl mx-auto px-4 py-8">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-3xl font-bold">TTS Notes</h1>
          <ThemeToggle />
        </div>

        <nav className="flex gap-2 mb-6 border-b border-[var(--border)]">
          <button
            onClick={() => setActiveTab('notes')}
            className={`px-4 py-2 font-medium border-b-2 transition-colors ${
              activeTab === 'notes'
                ? 'border-[var(--primary)] text-[var(--primary)]'
                : 'border-transparent text-[var(--text-muted)] hover:text-[var(--text)]'
            }`}
          >
            Notas
          </button>
          <button
            onClick={() => setActiveTab('documents')}
            className={`px-4 py-2 font-medium border-b-2 transition-colors ${
              activeTab === 'documents'
                ? 'border-[var(--primary)] text-[var(--primary)]'
                : 'border-transparent text-[var(--text-muted)] hover:text-[var(--text)]'
            }`}
          >
            Documentos PDF
          </button>
        </nav>

        {activeTab === 'notes' && (
          <div className="space-y-6">
            <NoteForm onNoteCreated={() => setNotesRefreshKey(k => k + 1)} />
            <NoteList key={notesRefreshKey} />
          </div>
        )}
        {activeTab === 'documents' && (
          <div className="space-y-6">
            <DocumentUpload onDocumentUploaded={() => setDocsRefreshKey(k => k + 1)} />
            <DocumentList key={docsRefreshKey} />
          </div>
        )}
      </div>
    </div>
  )
}

export default App
