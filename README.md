# TTS Notes

Aplicación local de notas de texto con conversión a voz, usando síntesis de texto a voz totalmente offline.

## Funcionalidades

- Crear, editar y eliminar notas de texto
- Subir documentos PDF y extraer su texto automáticamente
- Convertir notas y documentos a audio usando síntesis de voz local (sin conexión a internet ni servicios en la nube)
- Descargar o reproducir el audio generado
- Selector de temas (claro, oscuro, y un tema inspirado en Gruvbox)
- Almacenamiento 100% local — tus notas, documentos y audios nunca salen de tu computadora
- Multiplataforma: funciona en Windows y Linux

## Requerimientos

- Python 3.10 o superior
- Node.js 18 o superior (solo necesario para la instalación de desarrollo, ver más abajo)
- ~100 MB de espacio libre para el modelo de voz

## Instalación

Hay dos formas de instalar TTS Notes, según lo que necesites.

### Opción A: Instalación rápida (recomendada para uso normal)

No requiere git, Node.js, ni herramientas de desarrollo — solo Python.

#### Windows

1. Descargá el archivo `tts-notes.zip` desde la [página de Releases](https://github.com/brianezequiellopezdevelop-collab/tts-notes/releases)
2. Descomprimilo en cualquier carpeta
3. Abrí una terminal (`cmd` o PowerShell) dentro de esa carpeta y ejecutá: python3 scripts\setup.py

4. Listo — de ahora en adelante, hacé doble clic en `iniciar.bat` para abrir la aplicación

#### Linux

1. Descargá el archivo `tts-notes.zip` desde la [página de Releases](https://github.com/brianezequiellopezdevelop-collab/tts-notes/releases)
2. Descomprimilo:
```bash
   unzip tts-notes.zip -d tts-notes
   cd tts-notes
```
3. Instalá:
```bash
   python3 scripts/setup.py
```
4. Iniciá la aplicación:
```bash
   python3 scripts/run.py
```

### Opción B: Instalación para desarrollo

Requiere git y Node.js además de Python — usá esta vía si querés modificar el código o contribuir al proyecto.

```bash
git clone https://github.com/brianezequiellopezdevelop-collab/tts-notes.git
cd tts-notes

# Backend
cd backend
python3 -m venv venv
source venv/bin/activate       # En Windows: venv\Scripts\activate
pip install -r requirements.txt

# Descargar modelo de voz
mkdir -p voices
cd voices
curl -L -o es_ES-davefx-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx"
curl -L -o es_ES-davefx-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx.json"
cd ../..

# Frontend
cd frontend
npm install
npm run dev
```

Con el backend corriendo (`uvicorn app.main:app --reload` desde `backend/`) y el frontend con `npm run dev`, la app queda disponible en `http://localhost:5173` con recarga automática al editar código.

## Documentación adicional

Ver la carpeta [`docs/`](./docs) para arquitectura del proyecto y guía de contribución.

## Licencia

MIT
