import whisper
import os
import time

def transcribe(file_path, output_file="WNL_lezione2.txt"): 
    model = whisper.load_model("base") 
    if os.path.exists(output_file):
        os.remove(output_file) 

    with open(output_file, "a") as f:
        print("Start transcription...")
        start_time = time.time()

        # Transcribe the audio
        result = model.transcribe(file_path, task="transcribe")
        for segment in result["segments"]:
            text = segment["text"]
            f.write(text + "\n")

        print("Transcription completed.") 
        print(f"Total time required: {(time.time() - start_time) / 60:.2f} minutes")

# Path to the audio file
file_path = "Desktop/WNL lezione 2.m4a"
transcribe(file_path)