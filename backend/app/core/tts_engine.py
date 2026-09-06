# backend/app/core/tts_engine.py

from abc import ABC, abstractmethod


class TTSEngine(ABC):
    @abstractmethod
    def synthesize(self, text: str, output_path: str) -> None:
        pass
