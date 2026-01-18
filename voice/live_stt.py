import queue
import sys
import numpy as np
import sounddevice as sd
import whisper
import torch

SAMPLE_RATE = 16000
BLOCK_SIZE = 8000
CHANNELS = 1

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("small", device=device)

audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())

def listen_and_transcribe():
    print("🎙️ Listening... Speak now (Ctrl+C to stop)\n")

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        channels=CHANNELS,
        callback=audio_callback,
    ):
        buffer = np.empty((0, 1), dtype=np.float32)

        while True:
            data = audio_queue.get()
            buffer = np.concatenate((buffer, data))

            if len(buffer) >= SAMPLE_RATE * 3:
                audio = buffer.flatten()
                buffer = np.empty((0, 1), dtype=np.float32)

                result = model.transcribe(
                    audio,
                    language="en",
                    fp16=(device == "cuda"),
                )

                text = result["text"].strip()
                if text:
                    print("🧠:", text)

def listen_once():
    SAMPLE_RATE = 16000
    DURATION = 4

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )
    sd.wait()

    audio = audio.flatten()

    result = model.transcribe(
        audio,
        fp16=torch.cuda.is_available()
    )

    return result["text"].strip()



if __name__ == "__main__":
    listen_and_transcribe()