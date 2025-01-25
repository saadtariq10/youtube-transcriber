# main.py
from transcribe_module import get_transcription
from ai_model import process_with_ai_model

# Enter the YouTube video ID you want to transcribe
video_id = "https://www.youtube.com/watch?v=Tuw8hxrFBH8"  # Replace with the actual YouTube video ID

# Step 1: Get transcription
transcription_text = get_transcription(video_id)
print(transcription_text)
if transcription_text:
    # Step 2: Pass transcription to the AI model for processing
    ai_response = process_with_ai_model(transcription_text)

    # Print or store the processed AI output
    print("Processed Output from AI Model:")
    print(ai_response)
else:
    print("Failed to get transcription.")
