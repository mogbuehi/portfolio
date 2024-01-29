from pathlib import Path
import streamlit as st
from PIL import Image
import base64





# --- PATH Settings ---
project_root = Path(__file__).parent.parent

# Now you can access the 'assets' directory from the root
css_file = project_root / "assets" / "styles" / "main.css"
resume_file = project_root / "assets" / "Tech Resume 24-01-24.pdf"

youtube_icon = project_root/ "assets"/ "yt.png"
ig_icon = project_root/ "assets"/ "ig.png" 
ln_icon = project_root/ "assets"/ "ln.png"
github_icon = project_root/ "assets"/ "github.png"
hf_icon = project_root/ "assets"/ "hf.png"
gmail_icon = project_root/ "assets"/ "gmail.png"
x_icon = project_root/ "assets"/ "x.png"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

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

with st.sidebar:
    st.download_button(
        label=""" 🗎 Download Resume""",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )



# List of tuples with the name of the icon, the corresponding URL for attribution, and the creator's name
attributions = [
    ("LinkedIn", "https://www.flaticon.com/free-icons/linkedin", "Linkedin icons created by riajulislam - Flaticon"),
    ("YouTube", "https://www.flaticon.com/free-icons/youtube", "Youtube icons created by Freepik - Flaticon"),
    ("Facial Expression", "https://www.flaticon.com/free-icons/facial-expression", "Facial expression icons created by Pixel perfect - Flaticon"),
    ("GitHub", "https://www.flaticon.com/free-icons/github", "Github icons created by Pixel perfect - Flaticon"),
    ("GMail", "https://www.flaticon.com/free-icons/email", "Email icons created by Freepik - Flaticon"),
    ("X", "https://www.flaticon.com/free-icons/brands-and-logotypes", "Brands and logotypes icons created by Freepik - Flaticon")
    # Add more tuples for other icons and their attributions here
]

# Display each attribution under a subheader
st.subheader("Icon Attributions")

# Looping through each attribution and creating a markdown link for it
for name, url, description in attributions:
    attribution_html = f'<a href="{url}" title="{name} icons" target="_blank">{description}</a><br>'
    st.markdown(attribution_html, unsafe_allow_html=True)



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
