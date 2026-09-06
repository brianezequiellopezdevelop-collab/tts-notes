# backend/test_piper.py

import wave
from piper import PiperVoice

voice = PiperVoice.load("voices/es_ES-davefx-medium.onnx")

with wave.open("test_output.wav", "wb") as wav_file:
    voice.synthesize_wav("Hola, esta es una prueba del motor de texto a voz.", wav_file)
    print("Audio generado en test_output.wav")
