import whisper
import os
import time
import shutil
import sys

def check_ffmpeg():
    """
    Check if FFmpeg is installed and available in the PATH.
    """
    if shutil.which("ffmpeg") is None:
        print("Error: FFmpeg is not installed or not available in PATH.")
        print("Please install FFmpeg to handle audio formats correctly.")
        sys.exit(1)

def transcribe(file_path, output_file="transcription.txt", model_name="base"):
    """
    Transcribes an audio file into text using OpenAI's Whisper model.
    """

    model = whisper.load_model(model_name)
    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, "a") as f:
        print(f"Start transcription using the '{model_name}' model...")
        start_time = time.time()
        result = model.transcribe(file_path, task="transcribe")
        for segment in result["segments"]:
            text = segment["text"]
            f.write(text + "\n")

        print("Transcription completed.")
        print(f"Total time required: {(time.time() - start_time) / 60:.2f} minutes")

# Ensure FFmpeg is installed
check_ffmpeg()

# Path to the audio file
file_path = "path_to_your_audio_file/audio_file.m4a"

# Transcribe the audio
transcribe(file_path)