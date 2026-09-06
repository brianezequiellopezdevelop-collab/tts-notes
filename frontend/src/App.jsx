import { useState } from 'react'
import NoteList from './components/NoteList'
import NoteForm from './components/NoteForm'
import DocumentList from './components/DocumentList'
import DocumentUpload from './components/DocumentUpload'

function App() {
  const [activeTab, setActiveTab] = useState('notes')
  const [notesRefreshKey, setNotesRefreshKey] = useState(0)
  const [docsRefreshKey, setDocsRefreshKey] = useState(0)

  return (
    <div>
      <h1>TTS Notes</h1>
      <nav>
        <button onClick={() => setActiveTab('notes')}>Notas</button>
        <button onClick={() => setActiveTab('documents')}>Documentos PDF</button>
      </nav>

      {activeTab === 'notes' && (
        <div>
          <NoteForm onNoteCreated={() => setNotesRefreshKey(k => k + 1)} />
          <NoteList key={notesRefreshKey} />
        </div>
      )}
      {activeTab === 'documents' && (
        <div>
          <DocumentUpload onDocumentUploaded={() => setDocsRefreshKey(k => k + 1)} />
          <DocumentList key={docsRefreshKey} />
        </div>
      )}
    </div>
  )
}

export default App
