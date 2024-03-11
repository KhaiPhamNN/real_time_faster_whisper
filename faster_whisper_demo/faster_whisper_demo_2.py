import wave
import os
import pyaudio
import numpy as np
from faster_whisper import WhisperModel

def record_chunk(stream, chunk_length=1):
    frames = []
    for _ in range(int(16000 / 1024 * chunk_length)):
        data = stream.read(1024)
        frames.append(data)
    return b''.join(frames)

def transcribe_chunk(model, audio_data):
    audio_np = np.frombuffer(audio_data, dtype=np.int16)
    segments, _ = model.transcribe(audio_np)
    return ' '.join(segment.text.strip() for segment in segments)

def main():
    # Choose your model settings from tiny, base, small, medium, large with or without .en
    model_size = "medium.en"
    
    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")
    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

    accumulated_transcription = ""

    print("Running...\n")  # Print "Running..." when the program starts

    try:
        while True:
            chunk_data = record_chunk(stream)
            transcription = transcribe_chunk(model, chunk_data)
            print(transcription)
            accumulated_transcription += transcription + " "

    except KeyboardInterrupt:
        print("Stopping...")
        with open("log.txt", "w") as log_file:
            log_file.write(accumulated_transcription)

    finally:
        print("LOG: " + accumulated_transcription)
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()