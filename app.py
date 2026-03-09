import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY", "").strip()
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

st.set_page_config(page_title="Gemini Chat", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
      .stApp {
        background: #f7f7f8;
      }
      .main .block-container {
        max-width: 860px;
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
      }
      .chat-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #202123;
        margin-bottom: 0.25rem;
      }
      .chat-subtitle {
        color: #6b7280;
        margin-bottom: 1rem;
      }
      .msg-bubble {
        border-radius: 14px;
        padding: 0.75rem 0.9rem;
        margin-bottom: 0.45rem;
        border: 1px solid #e5e7eb;
        width: 100%;
      }
      .msg-user {
        background: #ffffff;
      }
      .msg-assistant {
        background: #dbeafe;
      }
      .msg-bubble [data-testid="stMarkdownContainer"],
      .msg-bubble [data-testid="stMarkdownContainer"] * {
        color: #000000 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="chat-title">Gemini Chatbot</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="chat-subtitle">ChatGPT-style Streamlit UI powered by Gemini</div>',
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I am your Gemini assistant. How can I help you today?",
        }
    ]

def render_message(msg: dict) -> None:
    if msg["role"] == "user":
        left, right = st.columns([2, 1])
        with left:
            st.markdown('<div class="msg-bubble msg-user">', unsafe_allow_html=True)
            st.markdown(msg["content"])
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        left, right = st.columns([1, 2])
        with right:
            st.markdown('<div class="msg-bubble msg-assistant">', unsafe_allow_html=True)
            st.markdown(msg["content"])
            st.markdown("</div>", unsafe_allow_html=True)


for msg in st.session_state.messages:
    render_message(msg)

if prompt := st.chat_input("Message Gemini..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    if not API_KEY:
        error_text = "Missing GOOGLE_API_KEY. Add it to your .env file."
        st.session_state.messages.append({"role": "assistant", "content": error_text})
        st.rerun()

    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        chat_history = []
        for m in st.session_state.messages:
            if m["role"] == "user":
                chat_history.append({"role": "user", "parts": [m["content"]]})
            elif m["role"] == "assistant":
                chat_history.append({"role": "model", "parts": [m["content"]]})

        chat = model.start_chat(history=chat_history[:-1])
        response = chat.send_message(prompt)
        text = (response.text or "").strip() or "I couldn't generate a response."
        st.session_state.messages.append({"role": "assistant", "content": text})
    except Exception as exc:
        error_text = f"Gemini error: {exc}"
        st.session_state.messages.append({"role": "assistant", "content": error_text})

    st.rerun()
