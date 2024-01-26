import streamlit as st
from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import base64
import os
from openai import OpenAI
from assistant import ai_assistant

st.header("Chat")
# Load API key from environment variable
if 'api_key' not in st.session_state:
    api_key = st.secrets["OPENAI_API_KEY"]

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
user_input = st.chat_input('type here')

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
