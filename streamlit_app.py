# import streamlit as st
# from transcribe_module import get_transcription
# from ai_model import process_with_ai_model

# # Streamlit app title
# st.title("YouTube Video Transcript Processor")
# st.write("Enter a YouTube URL to fetch its transcript and process it with AI.")

# # Input field for YouTube URL
# url = st.text_input("Enter YouTube Video URL:")

# # Fetch Transcript button
# if st.button("Fetch Transcript"):
#     if url:
#         with st.spinner("Fetching transcript..."):
#             transcription_text = get_transcription(url)
        
#         if transcription_text and not transcription_text.startswith("An error occurred"):
#             # Display the fetched transcript
#             st.subheader("Transcript Text")
#             st.text_area("Transcript", transcription_text, height=300)

#             # Process with AI Model button
#             if st.button("Process with AI Model"):
#                 with st.spinner("Processing with AI model..."):
#                     processed_output = process_with_ai_model(transcription_text)
#                 # Display the AI-processed output
#                 st.subheader("AI Processed Output")
#                 st.write(processed_output)
#         else:
#             # Display an error message if transcription failed
#             st.error(transcription_text)
#     else:
#         st.warning("Please enter a valid YouTube URL.")















import streamlit as st
from transcribe_module import get_transcription
from ai_model import process_with_ai_model

# Streamlit app title
st.title("YouTube Video Transcript Processor")
st.write("Enter a YouTube URL to fetch its transcript and process it with AI.")

# Session state to retain data
if "transcription_text" not in st.session_state:
    st.session_state.transcription_text = None
if "processed_output" not in st.session_state:
    st.session_state.processed_output = None

# Input field for YouTube URL
url = st.text_input("Enter YouTube Video URL:")

# Fetch Transcript button
if st.button("Fetch Transcript"):
    if url:
        with st.spinner("Fetching transcript..."):
            transcription_text = get_transcription(url)
        
        if transcription_text and not transcription_text.startswith("An error occurred"):
            st.session_state.transcription_text = transcription_text
            st.success("Transcript fetched successfully!")
        else:
            st.error(transcription_text)

# Display transcript if available
if st.session_state.transcription_text:
    st.subheader("Transcript Text")
    st.text_area("Transcript", st.session_state.transcription_text, height=300)

    # Process with AI Model button
    if st.button("Process with AI Model"):
        with st.spinner("Processing with AI model..."):
            processed_output = process_with_ai_model(st.session_state.transcription_text)
            st.session_state.processed_output = processed_output
            st.success("Processing complete!")

# Display AI processed output if available
if st.session_state.processed_output:
    st.subheader("AI Processed Output")
    st.write(st.session_state.processed_output)
