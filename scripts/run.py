# scripts/run.py

import subprocess
import sys
import webbrowser
import time
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
BACKEND = ROOT / "backend"
VENV = BACKEND / "venv"

URL = "http://127.0.0.1:8000"


def venv_python():
    if sys.platform == "win32":
        return VENV / "Scripts" / "python.exe"
    return VENV / "bin" / "python"


def main():
    if not VENV.exists():
        print("No se encontro el entorno virtual. Ejecuta primero 'python scripts/setup.py'.")
        sys.exit(1)

    env = os.environ.copy()
    env["TTS_NOTES_STANDALONE"] = "1"

    process = subprocess.Popen(
        [str(venv_python()), "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=str(BACKEND),
        env=env
    )

    time.sleep(2)
    webbrowser.open(URL)

    try:
        process.wait()
    except KeyboardInterrupt:
        process.terminate()


if __name__ == "__main__":
    main()
