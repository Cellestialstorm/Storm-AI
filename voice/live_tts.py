import subprocess
import tempfile
import os
import threading
import time
import sounddevice as sd
import soundfile as sf

from voice.interrupt import wait_for_interrupt

PIPER_DIR = r"C:\piper"
PIPER_EXE = os.path.join(PIPER_DIR, "piper.exe")
MODEL = os.path.join(PIPER_DIR, "models", "en_US-amy-medium.onnx")

def speak(text: str):
    if not text.strip():
        return
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        wav_path = f.name

    proc = subprocess.Popen(
        [
            PIPER_EXE,
            "--model", MODEL,
            "--output_file", wav_path
        ],
        cwd=PIPER_DIR,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    proc.stdin.write(text.encode("utf-8"))
    proc.stdin.close()
    proc.wait()

    data, samplerate = sf.read(wav_path, dtype="float32")

    stop_event = threading.Event()
    interrupt_thread = threading.Thread(
        target=wait_for_interrupt, args=(stop_event,), daemon=True
    )
    interrupt_thread.start()

    sd.play(data, samplerate)

    while sd.get_stream().active:
        if stop_event.is_set():
            sd.stop()
            break

    os.remove(wav_path)
    stop_event.set()