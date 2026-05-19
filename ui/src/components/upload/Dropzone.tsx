import { useDropzone } from 'react-dropzone'

interface Props {
  onFile: (file: File) => void
  fileName: string | null
}

export function Dropzone({ onFile, fileName }: Props) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: { 'text/csv': ['.csv'] },
    maxFiles: 1,
    onDropAccepted: ([file]) => onFile(file),
  })

  return (
    <div
      {...getRootProps()}
      style={{
        border: `2px dashed ${isDragActive ? 'var(--accent)' : 'var(--border)'}`,
        borderRadius: 'var(--radius-lg)', padding: '48px 32px',
        textAlign: 'center', cursor: 'pointer',
        background: isDragActive ? 'var(--bg-elevated)' : 'var(--bg-surface)',
        transition: 'all 0.2s',
      }}
    >
      <input {...getInputProps()} />
      <p style={{ fontSize: 32, marginBottom: 8 }}>📁</p>
      {fileName
        ? <p style={{ color: 'var(--accent)', fontWeight: 600 }}>{fileName}</p>
        : <p style={{ color: 'var(--text-secondary)' }}>
            {isDragActive ? 'Drop it here' : 'Drag & drop a CSV, or click to browse'}
          </p>
      }
    </div>
  )
}
