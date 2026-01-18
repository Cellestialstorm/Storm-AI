import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer

WAKE_WORD = "storm"
SAMPLE_RATE = 16000

model = Model("models/vosk/vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

def listen_for_wake_word():
    print("👂 Waiting for wake word...")

    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        dtype="int16",
        channels=1,
    ) as stream:
        while True:
            data, _ = stream.read(4000)
            data = bytes(data)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").lower()

                if WAKE_WORD in text:
                    print("🟢 Wake word detected!")
                    return