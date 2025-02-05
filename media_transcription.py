import os
import whisper
import json

# Function to transcribe media file using Whisper
def transcribe_media_file(file_path):
    model = whisper.load_model("tiny")  # Load the smallest Whisper model for transcription
    result = model.transcribe(file_path)
    return result["text"]

# Function to save transcription as JSON
def save_transcription_as_json(file_path, transcription, output_folder=None):
    if output_folder is None:
        output_folder = os.path.dirname(file_path)
    
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_folder, f"{base_name}_transcription.json")
    
    with open(output_path, 'w') as f:
        json.dump({"file_path": file_path, "transcription": transcription}, f, indent=4)

# Function to parse folders recursively and process media files
def process_media_folder(media_folder, output_folder=None):
    # Supported media file extensions (audio and video files)
    media_extensions = ['.mp3', '.wav', '.mp4', '.avi', '.mov', '.mkv']
    
    # Scan the folder and its subfolders
    for root, dirs, files in os.walk(media_folder):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if file is a supported media file
            if any(file.lower().endswith(ext) for ext in media_extensions):
                print(f"Processing: {file_path}")
                transcription = transcribe_media_file(file_path)
                save_transcription_as_json(file_path, transcription, output_folder)

if __name__ == "__main__":
    # Example usage
    media_folder = '/path/to/media/folder'  # Path to your media folder
    output_folder = '/path/to/output/folder'  # Path to where you want transcriptions saved
    process_media_folder(media_folder, output_folder)
