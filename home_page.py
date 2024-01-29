#--- Dependencies ---
from pathlib import Path
import streamlit as st
from PIL import Image

import requests
import base64
import os
from openai import OpenAI
from assistant import ai_assistant


# --- PATH Settings ---
current_dir = Path (__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"/ "main.css"
resume_file = current_dir / "assets"/ "Tech Resume 24-01-24.pdf"
profile_pic = current_dir / "assets"/ "profile_pic.jpg"

youtube_icon = current_dir/ "assets"/ "yt.png"
ig_icon = current_dir/ "assets"/ "ig.png" 
ln_icon = current_dir/ "assets"/ "ln.png"
github_icon = current_dir/ "assets"/ "github.png"
hf_icon = current_dir/ "assets"/ "hf.png"
gmail_icon = current_dir/ "assets"/ "gmail.png"
x_icon = current_dir/ "assets"/ "x.png"
zengx = current_dir/ "assets"/ "ZenGX.png"
statascratch = current_dir/ "assets"/ "statascratch.png"

# --- Load Assets ---




# --- General Settings ---
page_title = 'Portfolio Site'
page_icon = ":wave:"
my_name = "Matthew Ogbuehi"
description = """ Freelance AI Engineer, utilizing the power of large language models to build powerful and customized AI tools
to help solve unique business problems"""

## --- Clickable Icons
# Function to convert file to Base64 
def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Define your social media icons and paths. This is also the order they appear in the footer
social_media_icons = {
    'YouTube': youtube_icon,
    'LinkedIn': ln_icon,
    'GitHub': github_icon,
    'HuggingFace': hf_icon,
    'Instagram': ig_icon,
    'X': x_icon,
    'GMail': gmail_icon,
    
}

# Corresponding URLs for your social media
social_media_urls = {
    'YouTube': "https://www.youtube.com/channel/UC-MU1n71xrDjdqNFwXv5CuQ",
    'LinkedIn': "https://www.linkedin.com/in/mogbuehi/",
    'GitHub': "https://github.com/mogbuehi",
    'HuggingFace': "https://huggingface.co/mogbuehi",
    'Instagram': "https://www.instagram.com",
    "X": "https://twitter.com/Matten_Zero",
    'GMail': "matt.ogbuehi@gmail.com"
}

# Client logos
client_logos = {
    'zengx' : zengx,
    'statascratch' : statascratch
    
}


gpts = {
    "Cosplay Fashion Advisor GPT": "https://chat.openai.com/g/g-G94o6SwHc-cosplay-fashion-advisor",
    "MistralGPT" : "https://chat.openai.com/g/g-gEXnaYplU-mistralgpt"
}

clients = {
    "Statascratch":"https://www.stratascratch.com/",
    "ZenG X": "https://www.zengx.io/"
}

# --- Layout of the Page
# Add custom CSS for the sticky header and sticky footer
st.markdown("""
    <style>
    .sticky-header {
        position: fixed;
        top: 45px;
        left: 0;
        right: 0;
        height: 50px;
        background-color: #111;  # Adjust the color to match your app's style
        color: white;
        line-height: 50px;  # Aligns text vertically;
        font-size: 24px; /* Increase font size here */;
        z-index: 99999;
        padding: 0 10px;
        text-align: right;  /* Align text to the right */
        padding-left: 20px;  /* Add padding to the left of the text */
    }
    /* Other styles here */
    </style>
""", unsafe_allow_html=True)

# Display the sticky header
st.markdown('<div class="sticky-header">Matthew Ogbuehi | AI Engineer </div>', unsafe_allow_html=True)



## --- Sidebar
with open (resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

with st.sidebar:
    st.download_button(
        label=""" 🗎 Download Resume""",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )

## --- Load CSS, PDF, and Profile Pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title(my_name)
st.write(description)
st.write("##")
st.markdown("###### Workshop building a MultiModal AI Application with Tina Huang")

# YouTube video embed with autoplay and mute
video_embed_code = """
    <iframe width="700" height="400" src="https://www.youtube.com/embed/mHbnEFxaDs4?autoplay=1&mute=1&start=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
"""

st.markdown(video_embed_code, unsafe_allow_html=True)

## --- About me ---
st. write("##") # adds a large space between sections the size of header level (think markdown format)
st.write("---")
st.subheader("About Me")
st.write(
    """
As a freelance AI Engineer with a year's experience, I specialize in
developing advanced tools using multiple AI models including OpenAI's GPT 
and Whisper models. My background includes a 6-year tenure in bioprocess engineering, 
and I've recently completed multiple successful AI projects to my clients.
Combining these experiences, I bring a unique, multidisciplinary
approach to AI engineering, ready to deliver innovative solutions.
"""
)
st.image(profile_pic)
## --- Skills ---
st.write('##')
st.subheader("Skills")
st.write("---")
st.write (""" 
- Python frameworks
    - Data (Pandas, Numpy, Matplotlib)
    - LLM SDKs (Mistral AI, OpenAI)
- AI Engineering 
    - OpenAI : ChatGPT, GPT Vision, Whisper, TTS, custom GPTs, Assistants
    - LastMile AI Workbooks and AI Config
    - Mistral AI
""")

# --- Work History and Previous Clients ---
st.write("##")
st.write("---")
st.subheader("Previous Clients")
st.write("#") # adds a large space between sections
cols = st.columns(len(clients))
for index, (site_name, link) in enumerate(clients.items()):
    cols[index].write(f"[{site_name}]({link})") # markdown format

cols = st.columns(len(client_logos))
for index, (name, logo) in enumerate(client_logos.items()):
    logo = Image.open(logo)
    cols[index].image(logo)



# --- GPTs ---
st.write('#')
st.write("---")
st.subheader("Custom GPTs on OpenAI's GPT Store")
for gpt, links in gpts.items():
    if type(links) == dict:
        st.write(f"{gpt}")
        for key, value in links.items():
            st.write(f"- [{key}]({value})")
            
    else: 
        st.write(f"[{gpt}]({link})\n\n")

## --- Contact Form ---
st.write("---")
st.header("Contact")
st.markdown(""" **Email me for a consultation or inquiry via email or on my social links  located at the bottom of the page**""")
st.write("##")

### Add custom CSS for the sticky footer
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0; /* Ensure the footer extends to the right edge */
        background-color: #111;  /* Adjust the color to match your app's style */
        color: white;
        text-align: center;
        z-index: 9999;  /* Ensures the footer is on top of other elements */
        padding-left: 60px;  /* Adjust if your sidebar is a different width */
        padding-right: 20px;  /* Add some padding on the right if needed */
    }
    .footer-container {
        display: flex;
        justify-content: flex-end;
        padding-right: 20px;
        align-items: center;
        padding: 10px 0;  /* Add some padding inside the footer */
        width: 100%;
    }
    .footer img {
        height: 40px;  /* Adjust the size as needed */
        margin: 0 10px;  /* Spacing between icons */
    }
    /* Add padding to the bottom of the Streamlit content to prevent overlap */
    .main .block-container {
        padding-bottom: 70px;  /* Adjust the size to match the footer's height */
    }
    </style>
""", unsafe_allow_html=True)

### Display the social media icons in the footer
footer_html = '<div class="footer"><div class="footer-container">'
for platform, icon_path in social_media_icons.items():
    url = social_media_urls[platform]
    base64_image = get_image_as_base64(icon_path)
    footer_html += f'<a href="{url}" target="_blank"><img src="data:image/png;base64,{base64_image}" alt="{platform}"></a>'
footer_html += '</div></div>'
st.markdown(footer_html, unsafe_allow_html=True)
