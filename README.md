# real_time_faster_whisper

## Real-Time Speech Transcription using Faster-Whisper Model

This Python script facilitates real-time transcription of speech using the Faster-Whisper Model. The Whisper Model is a specialized model designed for efficient transcription of audio data. The script leverages the SpeechRecognition library for audio recording and transcription, along with the Faster-Whisper Model for transcribing the recorded audio.

### Features:
- Real-time transcription of speech from microphone input.
- Support for specifying the Faster-Whisper Model to be used.
- Adjustable energy threshold for microphone detection.
- Customizable timeouts for recording and phrase detection.
- Compatibility with both Linux and non-Linux platforms.

### Requirements:
- Python 3.8 or higher
- NumPy
- SpeechRecognition
- PyAudio
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (A library for the Whisper Model)

#### GPU Execution

GPU execution requires the following NVIDIA libraries to be installed:

- [cuBLAS for CUDA 11](https://developer.nvidia.com/cublas)
- [cuDNN 8 for CUDA 11](https://developer.nvidia.com/cudnn)

Please ensure that these libraries are properly installed on your system to enable GPU acceleration.

### Usage:
Run the script `faster_whisper_demo.py` using Python 3.8 or higher. Optionally, specify the following arguments:
 - `--model`: Specify the size of the Whisper Model to use (default is 'base.en').
 - `--energy_threshold`: Set the energy level for the microphone to detect (default is 1000).
 - `--record_timeout`: Set the duration of real-time recording in seconds (default is 2 seconds).
 - `--phrase_timeout`: Set the duration of empty space between recordings before considering it a new line in the transcription (default is 1 second).
 - `--default_microphone`: Specify the default microphone name for SpeechRecognition. Use 'list' to view available microphones.

### Workflow:
1. The script initializes with user-specified configurations and loads the Faster-Whisper Model.
2. It sets up the microphone for audio input and adjusts for ambient noise.
3. A background thread continuously records audio and pushes raw audio data into a thread-safe queue.
4. Recorded audio data is processed in chunks, converted to a format compatible with the Whisper Model, and transcribed.
5. The transcription is updated in real-time based on pauses in speech.
6. Press `Ctrl + C` to stop the transcription process.
7. The final transcription is displayed on the console.

### Note:
- Ensure that the microphone is properly connected and configured before running the script.
- The script provides a real-time transcription experience, updating the transcription dynamically as speech is detected.
- The Whisper Model size and other parameters can be adjusted based on the user's requirements.

Feel free to explore and modify the script according to your needs. For any issues or suggestions, please refer to the [GitHub repository](https://github.com/SYSTRAN/faster-whisper) or contact the developer.
