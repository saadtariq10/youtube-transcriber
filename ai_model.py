# #code to run in terminal

# # ai_model.py
# from groq import Groq
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # Fetch the API key
# api_key = os.getenv("GROQ_API_KEY")

# # Initialize the Groq client
# client = Groq(api_key=api_key)

# def process_with_ai_model(transcription_text):
#     # Define the system message to tailor the behavior of the assistant
#     system_message = "You are an AI that extracts and processes relevant information from video transcriptions, focusing on key points, questions, action items, and important takeaways."

#     # Make a request to the Groq model
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": "system", "content": system_message},
#             {"role": "user", "content": transcription_text}  # Pass the transcription as input to the AI model
#         ],
#         model="llama-3.3-70b-versatile",  # Replace with your specific model
#         temperature=0.5,
#         max_tokens=1024,
#         top_p=1,
#         stop=None,
#         stream=False,
#     )
    
#     # Return the AI model's response (i.e., processed output)
#     return chat_completion.choices[0].message.content
















#code to run streamlit

# from groq import Groq
# from dotenv import load_dotenv
# import os

# # Load environment variables
# load_dotenv()

# # Fetch the API key
# api_key = os.getenv("GROQ_API_KEY")

# # Initialize the Groq client
# client = Groq(api_key=api_key)

# # Function to process transcription using the AI model
# def process_with_ai_model(transcription_text):
#     system_message = (
#         "You are an AI that extracts and processes relevant information from "
#         "video transcriptions, focusing on key points, questions, action items, "
#         "and important takeaways."
#     )
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[
#                 {"role": "system", "content": system_message},
#                 {"role": "user", "content": transcription_text}
#             ],
#             model="llama-3.3-70b-versatile",  # Replace with your model
#             temperature=0.5,
#             max_tokens=1024,
#             top_p=1,
#             stop=None,
#             stream=False,
#         )
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return f"An error occurred while processing: {str(e)}"










#modified code for system prompt


from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Fetch the API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq client
client = Groq(api_key=api_key)

# Path to the system prompt file
SYSTEM_PROMPT_FILE = "system_prompt.txt"  # Ensure this file exists in your project directory

# Read the system prompt from the file
try:
    with open(SYSTEM_PROMPT_FILE, 'r') as file:
        system_message = file.read().strip()
except FileNotFoundError:
    raise FileNotFoundError(f"The system prompt file '{SYSTEM_PROMPT_FILE}' was not found.")
except Exception as e:
    raise Exception(f"An error occurred while reading the system prompt: {str(e)}")

# Function to process transcription using the AI model
def process_with_ai_model(transcription_text):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": transcription_text}
            ],
            model="llama-3.3-70b-versatile",  # Replace with your model
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred while processing: {str(e)}"
