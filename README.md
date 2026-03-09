# Gemini Chatbot (Streamlit)

A lightweight Gemini chatbot built with Streamlit and Python.

## Current UI/UX
- Dark theme chat interface
- User and assistant chat bubbles
- In-session chat memory (until app refresh/restart)
- Single conversation flow (no sidebar/history manager)

## Tech Stack
- Python 3.10+
- Streamlit
- Google Gemini API (`google-generativeai`)
- `python-dotenv`

## Project Files
- `app.py`: Main Streamlit app
- `requirements.txt`: Dependencies
- `.env.example`: Environment variable template
- `BUILD_INSTRUCTIONS.md`: Full setup and run guide

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Create `.env`:
   ```bash
   cp .env.example .env
   ```
3. Add Gemini credentials in `.env`:
   ```env
   GOOGLE_API_KEY=your_real_gemini_api_key
   GEMINI_MODEL=gemini-2.0-flash
   ```
4. Run app:
   ```bash
   streamlit run app.py
   ```

## Environment Variables
- `GOOGLE_API_KEY` (required): Gemini API key
- `GEMINI_MODEL` (optional): Gemini model name (default in app if missing)

## Notes
- `.env` is already ignored via `.gitignore`.
- If you get a model `404` error, set `GEMINI_MODEL` in `.env` to a model available for your API key/project.
