# TTS Notes

Aplicación local de notas de texto con conversión a voz, usando síntesis de texto a voz totalmente offline.

## Funcionalidades

- Crear, editar y eliminar notas de texto
- Convertir cualquier nota a audio usando síntesis de voz local (sin conexión a internet ni servicios en la nube)
- Descargar o reproducir el audio generado
- Almacenamiento 100% local — tus notas y audios nunca salen de tu computadora
- Multiplataforma: funciona en Windows y Linux

## Requerimientos

- Python 3.10 o superior
- Node.js 18 o superior (para el frontend)
- ~100 MB de espacio libre para el modelo de voz

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tts-notes.git
cd tts-notes
```

### 2. Configurar el backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate       # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Descargar un modelo de voz

Los modelos de voz no se incluyen en el repositorio por su tamaño. Descarga al menos una voz desde [Hugging Face - Piper Voices](https://huggingface.co/rhasspy/piper-voices):

```bash
mkdir -p voices
cd voices
curl -L -o es_ES-davefx-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx"
curl -L -o es_ES-davefx-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx.json"
cd ..
```

### 4. Iniciar el servidor backend

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`, con documentación interactiva en `http://127.0.0.1:8000/docs`.

## Documentación adicional

Ver la carpeta [`docs/`](./docs) para arquitectura del proyecto y guía de contribución.

## Licencia

MIT
