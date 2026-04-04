import os
import time
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# ---------------------------
# Load Environment Variables
# ---------------------------
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY", "").strip()

# Stable model for free tier
MODEL_NAME = "gemini-2.5-flash"

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="Gemini Chat", layout="centered")

# ---------------------------
# Initialize Gemini once
# ---------------------------
if "model" not in st.session_state:
    if API_KEY:
        genai.configure(api_key=API_KEY)
        st.session_state.model = genai.GenerativeModel(MODEL_NAME)

# ---------------------------
# Dark UI Styling
# ---------------------------
st.markdown("""
<style>

html, body, .stApp {
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

# ---------------------------
# Title
# ---------------------------
st.markdown("## 🤖 Gemini Chatbot")

# ---------------------------
# Session State Messages
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I am your Gemini assistant. How can I help you today?"}
    ]

# ---------------------------
# Display Chat
# ---------------------------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
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

# ---------------------------
# Chat Input
# ---------------------------
if prompt := st.chat_input("Message Gemini..."):

    if not API_KEY:
        response_text = "❌ Missing GOOGLE_API_KEY in .env"

    else:
        try:

            model = st.session_state.model

            # Limit history to last 6 messages
            history = []
            for m in st.session_state.messages[-6:]:
                role = "user" if m["role"] == "user" else "model"
                history.append({"role": role, "parts": [m["content"]]})

            chat = model.start_chat(history=history)

            # Rate limit protection
            try:
                response = chat.send_message(prompt)

            except Exception as e:
                if "429" in str(e):
                    time.sleep(60)
                    response = chat.send_message(prompt)
                else:
                    raise

            response_text = response.text or "No response generated"

        except Exception as e:
            response_text = f"⚠️ Error: {str(e)}"

    # Save messages
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response_text})

    st.rerun()