import streamlit as st

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
            st.write(f"- [{key}]({value})")
            
    else: 
        st.write(f"[{project}]({links})\n\n")
