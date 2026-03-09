import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY", "").strip()
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

st.set_page_config(page_title="Gemini Chat", layout="centered")

st.markdown("""
<style>

html, body, .stApp {
    background:#212121 !important;
}

[data-testid="stAppViewContainer"]{
    background:#212121 !important;
}

header, footer,
[data-testid="stHeader"],
[data-testid="stToolbar"]{
    background:#212121 !important;
}

.st-emotion-cache-hzygls{
    background:#212121 !important;
}

.stBottom{
    background:#212121 !important;
}

[data-testid="stBottomBlockContainer"]{
    background:#212121 !important;
}

[data-testid="stChatInput"]{
    background:#212121 !important;
}

textarea{
    background:#303030 !important;
    color:white !important;
}

.chat-container{
    width:100%;
}

.user-msg{
    background:#303030;
    color:white;
    padding:12px 16px;
    border-radius:12px;
    margin:10px 0;
    max-width:70%;
    width:fit-content;
}

.assistant-msg{
    background:#2a2a2a;
    color:white;
    padding:12px 16px;
    border-radius:12px;
    margin:10px 0 10px auto;
    max-width:70%;
    width:fit-content;
}

</style>
""", unsafe_allow_html=True)

st.markdown("## 🤖 Gemini Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"assistant","content":"Hi! I am your Gemini assistant. How can I help you today?"}
    ]

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"]=="user":
        st.markdown(
            f'<div class="user-msg">{msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="assistant-msg">{msg["content"]}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

if prompt := st.chat_input("Message Gemini..."):

    st.session_state.messages.append({"role":"user","content":prompt})

    if not API_KEY:
        response_text="Missing GOOGLE_API_KEY in .env"
    else:
        try:
            genai.configure(api_key=API_KEY)
            model=genai.GenerativeModel(MODEL_NAME)

            history=[]
            for m in st.session_state.messages:
                role="user" if m["role"]=="user" else "model"
                history.append({"role":role,"parts":[m["content"]]})

            chat=model.start_chat(history=history[:-1])
            response=chat.send_message(prompt)

            response_text=response.text or "No response generated"

        except Exception as e:
            response_text=str(e)

    st.session_state.messages.append({"role":"assistant","content":response_text})

    st.rerun()