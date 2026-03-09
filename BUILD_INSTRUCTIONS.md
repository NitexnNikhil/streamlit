# Build Instructions

This document covers setup, run, and troubleshooting for the current Streamlit Gemini chatbot.

## 1. Prerequisites
- Python `3.10` or newer
- `pip`
- Gemini API key

## 2. Install Dependencies
From project root:

```bash
pip install -r requirements.txt
```

## 3. Configure Environment
Create `.env` from template:

```bash
cp .env.example .env
```

Update `.env`:

```env
GOOGLE_API_KEY=your_real_gemini_api_key
GEMINI_MODEL=gemini-2.0-flash
```

## 4. Run Application
```bash
streamlit run app.py
```

Default local URL:
- `http://localhost:8501`

## 5. Verify
- App opens with dark background
- You can type in chat input at bottom
- User message appears in chat
- Gemini response appears after sending

## 6. Troubleshooting
- `Missing GOOGLE_API_KEY in .env`
  - Add `GOOGLE_API_KEY` to `.env`
- `404 model ... not found`
  - Change `GEMINI_MODEL` in `.env` to a model your API key supports
- Import/module errors
  - Reinstall dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 7. Optional Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 8. Security
- Never commit `.env`
- Rotate API keys if exposed
