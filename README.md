# transcribeAudio

This project uses OpenAI Whisper to convert audio files into text.

## Features

Whisper supports multiple models, each with a trade-off between speed and accuracy:
- tiny: Fastest, least accurate.
- base (default): Balanced speed and accuracy.
- small: More accurate but slower.
- medium: Even more accurate but slower.
- large: Most accurate but slowest.
 
## Supported Formats
OpenAI Whisper supports a wide range of audio formats, thanks to FFmpeg integration. Commonly supported formats include:

- **Uncompressed formats**: `.wav`
- **Lossless compressed formats**: `.flac`, `.alac`
- **Lossy compressed formats**: `.mp3`, `.aac`, `.m4a`, `.ogg`, `.wma`
- **Other formats**: `.amr`, `.opus`

## Requirements
- Python 3.x
- Libraries: `whisper`, `os`, `time`
- **FFmpeg**: Required for handling audio file formats like `.mp3`, `.m4a`, `.flac`, etc.

## Installation
1. Clone the repository.
2. Install dependencies: `pip install openai-whisper`.
3. To install FFmpeg, follow the instructions for your operating system:
- Linux : `sudo apt install ffmpeg`
- MacOS : `brew install ffmpeg`
- Windows :     
    1.    Download FFmpeg from the official website https://ffmpeg.org/download.html.
    2.    Extract the downloaded file.
    3.    Add the bin folder from the extracted directory to your system’s PATH:
        1. Open Control Panel > System > Advanced System Settings.
        2. Click on Environment Variables.
        3. Edit the Path variable and add the path to the bin folder.
4. Run the script with an audio file as input.

(If you see some warnings when you run it, don't worry the tool will work anyway)

## Usage
```bash
python transcribe_audio.py
