# scripts/setup.py

import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
BACKEND = ROOT / "backend"
VENV = BACKEND / "venv"
VOICES = BACKEND / "voices"

VOICE_URL_BASE = "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/es/es_ES/davefx/medium"
VOICE_FILES = ["es_ES-davefx-medium.onnx", "es_ES-davefx-medium.onnx.json"]


def venv_python():
    if sys.platform == "win32":
        return VENV / "Scripts" / "python.exe"
    return VENV / "bin" / "python"


def create_venv():
    if VENV.exists():
        print("El entorno virtual ya existe, se omite este paso.")
        return
    print("Creando entorno virtual...")
    subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)


def install_requirements():
    print("Instalando dependencias de Python...")
    subprocess.run(
        [str(venv_python()), "-m", "pip", "install", "-r", str(BACKEND / "requirements.txt")],
        check=True
    )


def download_voice():
    VOICES.mkdir(exist_ok=True)
    for filename in VOICE_FILES:
        target = VOICES / filename
        if target.exists():
            print(f"{filename} ya existe, se omite la descarga.")
            continue
        url = f"{VOICE_URL_BASE}/{filename}"
        print(f"Descargando {filename}...")
        urllib.request.urlretrieve(url, target)


def main():
    create_venv()
    install_requirements()
    download_voice()
    print("\nInstalacion completa. Ejecuta 'python scripts/run.py' para iniciar la aplicacion.")


if __name__ == "__main__":
    main()
