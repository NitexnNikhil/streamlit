# Gemini Chat UI with Streamlit

A clean, ChatGPT-style chatbot interface built with Streamlit and Python, powered by Google Gemini.

## Features
- Chat-style interface with persistent in-session history
- Gemini model integration via `google-generativeai`
- Streaming responses for better perceived speed
- Sidebar controls for model, temperature, and max tokens
- Quick prompt buttons for common tasks
- Secure credential loading from `.env`

## Tech Stack
- Python 3.10+
- Streamlit
- Google Gemini API (`google-generativeai`)
- `python-dotenv`

## Project Structure
- `app.py`: Main Streamlit application
- `requirements.txt`: Python dependencies
- `.env.example`: Environment variable template
- `BUILD_INSTRUCTIONS.md`: Full setup/build/run guide

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure environment:
   ```bash
   cp .env.example .env
   ```
3. Add your key in `.env`:
   ```env
   GOOGLE_API_KEY=your_real_gemini_api_key
   GEMINI_MODEL=gemini-1.5-flash
   ```
4. Run app:
   ```bash
   streamlit run app.py
   ```

## Environment Variables
- `GOOGLE_API_KEY` (required): Your Gemini API key
- `GEMINI_MODEL` (optional): Default model used on startup

## Notes
- Keep `.env` private. It is already listed in `.gitignore`.
- Use sidebar controls to tune output behavior without code changes.
