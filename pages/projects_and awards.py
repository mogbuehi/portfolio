import streamlit as st

projects = {
    "🏆Job Seeker Workbook": "",
    "AI Tutor for Data Science (Freelance Project for Statascratch)": {"Demo": "https://huggingface.co/spaces/mogbuehi/LO_AI_Tutor", 
                                                                       "Video Presentation" : "https://drive.google.com/file/d/1UHJvTDQ2SdpPJGkpwzs0AGnMplx_mdiP/view?usp=drive_link", 
                                                                       "Slide Deck": "https://docs.google.com/presentation/d/1kH8TqgbvjcZ-57-MGf6eioZ6nHlKnG7DwKd8ShbJJNs/edit?usp=drive_link"
},
    "AI YouTube Language Tutor (StreamLit AI Hackathon, 2023)": "",
    "LLM classifier for generating synthetic data (Brembo Generative AI Hackathon, 2023)": "",
    "Mistral AI API Chatbot": "https://github.com/mogbuehi/Mistral_AI_Chatbot"
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