# #code to run in terminal

# from youtube_transcript_api import YouTubeTranscriptApi
# import re

# # Function to extract video ID from YouTube URL
# def get_video_id(url):
#     # YouTube URL regex pattern
#     pattern = r"(?:https?://)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*\?v=)|(?:youtu\.be\/))([^""&?=]*)"
#     match = re.match(pattern, url)
#     if match:
#         return match.group(1)
#     return None

# # Function to get transcription text from YouTube video
# def get_transcription(url):
#     # Extract video ID from URL
#     video_id = get_video_id(url)
    
#     if video_id:
#         try:
#             # Fetch transcript for the video
#             transcript = YouTubeTranscriptApi.get_transcript(video_id)
            
#             # Combine and return the transcript text
#             transcription_text = " ".join([entry['text'] for entry in transcript])
#             return transcription_text
        
#         except Exception as e:
#             return f"An error occurred: {str(e)}"
#     else:
#         return "Invalid YouTube URL. Please enter a valid URL."

# # Input: YouTube video URL
# url = input("Enter YouTube Video URL: ")

# # Get the transcription text
# transcription_text = get_transcription(url)

# # Display the transcription text
# if transcription_text:
#     print("\nTranscript Text:")
#     print(transcription_text)

















#code for streamlit

from youtube_transcript_api import YouTubeTranscriptApi
import re

# Function to extract video ID from YouTube URL
def get_video_id(url):
    pattern = r"(?:https?://)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*\?v=)|(?:youtu\.be\/))([^\"&?=]*)"
    match = re.match(pattern, url)
    if match:
        return match.group(1)
    return None

# Function to get transcription text from YouTube video
def get_transcription(url):
    video_id = get_video_id(url)
    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcription_text = " ".join([entry['text'] for entry in transcript])
            return transcription_text
        except Exception as e:
            return f"An error occurred: {str(e)}"
    else:
        return "Invalid YouTube URL. Please enter a valid URL."
