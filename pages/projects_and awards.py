#--- Dependencies ---
from pathlib import Path
import streamlit as st
from PIL import Image
import base64

css_file = "styles/main.css"
# --- PATH Settings ---
project_root = Path(__file__).parent.parent

css_file = project_root / "styles"/ "main.css"
resume_file = project_root / "assets"/ "Resume.pdf"
profile_pic = project_root / "assets"/ "profile_pic.jpg"

youtube_icon = project_root/ "assets"/ "yt.png"
ig_icon = project_root/ "assets"/ "ig.png" 
ln_icon = project_root/ "assets"/ "ln.png"
github_icon = project_root/ "assets"/ "github.png"
hf_icon = project_root/ "assets"/ "hf.png"
gmail_icon = project_root/ "assets"/ "gmail.png"
x_icon = project_root/ "assets"/ "x.png"
zengx = project_root/ "assets"/ "ZenGX.png"
statascratch = project_root/ "assets"/ "statascratch.png"

# --- Load Assets ---

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
    "X": "https://twitter.com/MattenZero",
    'GMail': "mailto:matt.ogbuehi@gmail.com"
}

# Client logos
client_logos = {
    'statascratch' : statascratch,
    'zengx' : zengx
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
with st.sidebar:
    # Page Navigation
    st.page_link(page=f'{project_root}/home_page.py', label='Home')
    st.page_link(page= 'pages/chat_with_tachikoma.py', label='Chat with my Assistant!')
    st.page_link(page= 'pages/wazabi_labs.py', label='Startup')
    st.page_link(page= 'pages/projects_and awards.py', label='Projects')
    st.page_link(page= 'pages/attributions.py', label='Attributions')

with open (resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with st.sidebar:
    st.download_button(
        label=""" 🗎 Download Resume""",
        data=PDFbyte,
        file_name='Resume_Matt_Ogbuehi.pdf',
        mime="application/octet-stream"
    )

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

projects = {
    "Mistral AI API Chatbot": "https://github.com/mogbuehi/Mistral_AI_Chatbot",
    
    " \"Chat with YouTube\" application" : {
        "Colab Notebook": "https://github.com/mogbuehi/chat_with_yt/blob/main/Chat_with_YT_version_2.ipynb",
        "Workshop with Tina Huang": "https://www.youtube.com/watch?v=mHbnEFxaDs4"
    },
    
    "🏆Job Seeker Workbook": {
        "Workbook": "https://lastmileai.dev/workbooks/cln0k7vr4018lpew58p32ptny",
        "Winning Announcement": "https://www.linkedin.com/feed/update/urn:li:activity:7116172175723696128/"
    },

    "AI YouTube Language Tutor (StreamLit AI Hackathon, 2023)": "https://huggingface.co/spaces/mogbuehi/YT_Language_Tutor",
    
    "AI Tutor for Data Science (Freelance Project for Statascratch)": {"Demo": "https://huggingface.co/spaces/mogbuehi/LO_AI_Tutor", 
                                                                       "Video Presentation" : "https://drive.google.com/file/d/1UHJvTDQ2SdpPJGkpwzs0AGnMplx_mdiP/view?usp=drive_link", 
                                                                       "Slide Deck": "https://docs.google.com/presentation/d/1kH8TqgbvjcZ-57-MGf6eioZ6nHlKnG7DwKd8ShbJJNs/edit?usp=drive_link"
                                                                      },
    
    "LLM classifier for generating synthetic data (Brembo Generative AI Hackathon, 2023)": "https://colab.research.google.com/drive/1-Pt8WuLWiSjEqWcaN5KvxXpUs5fdb7uz?usp=sharing",
    
}

# --- Projects ---
st.write('#')
st.write("---")
st.subheader("Projects and Accomplishments")


for project, links in projects.items():
    if type(links) == dict:
        st.write(f"{project}")
        for key, value in links.items():
            # st.write(f"- [{key}]({value})")
            st.page_link(page=value, label=f"🔗 {key}")
            
    else: 
        # st.write(f"[{project}]({links})\n\n")
        st.page_link(page=links, label=f"🔗 {project}")


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
