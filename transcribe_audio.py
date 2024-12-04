import whisper
import os
import time

def transcribe(file_path, output_file="transcription.txt"):
    """
    Transcribes an audio file into text using OpenAI's Whisper model.

    Args:
        file_path (str): Path to the input audio file.
        output_file (str): Path to the output text file where transcription will be saved.

    Returns:
        None
    """
    # Load the Whisper model (use "base" for a balanced trade-off between speed and accuracy)
    model = whisper.load_model("base")
    
    # Remove the existing output file if it exists
    if os.path.exists(output_file):
        os.remove(output_file)

    # Open the output file in append mode to write the transcription
    with open(output_file, "a") as f:
        print("Start transcription...")
        start_time = time.time()  # Record the start time

        # Transcribe the audio file
        result = model.transcribe(file_path, task="transcribe")
        
        # Write each segment of transcription to the output file
        for segment in result["segments"]:
            text = segment["text"]
            f.write(text + "\n")
            print(f"Segment transcribed: {text}")

        # Print the completion message and total time taken
        print("Transcription completed.")
        print(f"Total time required: {(time.time() - start_time) / 60:.2f} minutes")

# Specify the path to the audio file
file_path = "path_to_your_audio_file/audio_file.m4a"

# Call the transcribe function
transcribe(file_path)