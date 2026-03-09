# Build Instructions

This file describes how to set up, run, and verify the Gemini Streamlit chatbot locally.

## 1. Prerequisites
- Python `3.10` or newer
- `pip` available in your shell
- A valid Google Gemini API key

## 2. Install Dependencies
From the project root:

```bash
pip install -r requirements.txt
```

## 3. Configure Credentials
1. Copy template:

```bash
cp .env.example .env
```

2. Edit `.env`:

```env
GOOGLE_API_KEY=your_real_gemini_api_key
GEMINI_MODEL=gemini-1.5-flash
```

## 4. Run the App
```bash
streamlit run app.py
```

Default local URL is usually:
- `http://localhost:8501`

## 5. Validate the Build
Use this checklist:
- App opens with hero header and sidebar controls
- Sending a message returns Gemini response
- Assistant response text appears in black
- `Start New Chat` resets chat history
- Quick prompt buttons auto-send a starter prompt

## 6. Common Issues
- `Missing GOOGLE_API_KEY`:
  - Ensure key exists in `.env` and has no extra spaces
- Import errors:
  - Re-run `pip install -r requirements.txt`
- No response from model:
  - Verify API key access and selected model availability

## 7. Optional: Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 8. Production Notes
- Do not commit `.env`
- Rotate API keys regularly
- Pin dependency versions more strictly for deterministic deployments
