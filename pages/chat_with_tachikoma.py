import streamlit as st
from pathlib import Path
import streamlit as st
from PIL import Image
import requests
import base64
import os
from openai import OpenAI
from assistant import ai_assistant

css_file = "styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.header("Chat with Tachikoma")
st.markdown("""Chat with my virtual assistant, Tachikoma. Her personality is based on the AI from the anime Ghost in the Shell. 
She is has knowledge of my work experience and can answer questions about my resume with you. Enter your queries below!""")

# YouTube video ID
video_id = "jRJiY8UjpOU"

# Embed YouTube video using Markdown and HTML with loop
st.markdown(f"""
    <div style="text-align:center;">
        <iframe width="700" height="393" src="https://www.youtube.com/embed/{video_id}?playlist={video_id}&loop=1&autoplay=1&mute=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="margin: auto; display: block;"></iframe>
    </div>
    """, unsafe_allow_html=True)
st.markdown("#")


# Load API key from environment variable
# Check if the API key is not already in the session state
if 'api_key' not in st.session_state:
    # Load the API key from the environment variables
    st.session_state['api_key'] = os.getenv('OPENAI_API_KEY')

# Use the API key from the session state
api_key = st.session_state['api_key']

# Optional: Check if the API key is loaded and display a message
if api_key is None:
    st.error("API key is not set!")
else:
    st.success("API key loaded successfully.")

client = OpenAI(api_key=st.session_state.api_key)

# Initialize session state for messages and thread_id if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

if 'thread_id' not in st.session_state:
    thread = client.beta.threads.create() 
    st.session_state['thread_id'] = thread.id

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])


# Chat input
user_input = st.chat_input('Type your query here and hit enter')

# Handle the chat interaction
if user_input:  # Check if there is an input to send
    user_message = {"role": "user", "content": user_input}
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        st.markdown(user_input)

    # Assume ai_assistant is a function that sends the message to the OpenAI API and gets a response
    text_response = ai_assistant(user_input=user_input, thread_id=st.session_state.thread_id, client=client)
    assistant_message = {"role": "assistant", "content": text_response}
    assistant_response = st.chat_message(name=assistant_message['role'])
    assistant_response.markdown(text_response)
    st.session_state.messages.append(assistant_message)
