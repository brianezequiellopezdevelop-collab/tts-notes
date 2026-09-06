# backend/app/core/piper_engine.py

import wave
from piper import PiperVoice
from app.core.tts_engine import TTSEngine


class PiperEngine(TTSEngine):
    def __init__(self, model_path: str):
        self.voice = PiperVoice.load(model_path)

    def synthesize(self, text: str, output_path: str) -> None:
        with wave.open(output_path, "wb") as wav_file:
            self.voice.synthesize_wav(text, wav_file)
