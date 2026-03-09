# Gemini Chatbot (Streamlit)

Simple Streamlit chatbot UI connected to Google Gemini.

## What This Project Is
- Single-chat conversational app
- Dark themed UI
- User message bubble on the left
- Assistant message bubble on the right
- Session-based memory (`st.session_state`)

## Stack
- Python 3.10+
- Streamlit
- `google-generativeai`
- `python-dotenv`

## Files
- `app.py` - Main application
- `requirements.txt` - Dependencies
- `.env.example` - Environment template
- `BUILD_INSTRUCTIONS.md` - Full setup + troubleshooting guide

## Quick Start
1. Install:
   ```bash
   pip install -r requirements.txt
   ```
2. Create env file:
   ```bash
   cp .env.example .env
   ```
3. Add credentials:
   ```env
   GOOGLE_API_KEY=your_real_gemini_api_key
   GEMINI_MODEL=gemini-2.0-flash
   ```
4. Run:
   ```bash
   streamlit run app.py
   ```

## Environment Variables
- `GOOGLE_API_KEY` (required)
- `GEMINI_MODEL` (optional, default: `gemini-2.0-flash`)

## Notes
- `.env` is ignored by git.
- If a model is unavailable for your key/project, set `GEMINI_MODEL` to a supported one.
