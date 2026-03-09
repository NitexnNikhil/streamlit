# Build Instructions

This guide matches the current `app.py` implementation.

## 1. Prerequisites
- Python `3.10+`
- `pip`
- Gemini API key

## 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 3. Configure Environment
```bash
cp .env.example .env
```

Edit `.env`:
```env
GOOGLE_API_KEY=your_real_gemini_api_key
GEMINI_MODEL=gemini-2.0-flash
```

## 4. Start the App
```bash
streamlit run app.py
```

Default URL:
- `http://localhost:8501`

## 5. Validation Checklist
- Dark background renders correctly
- Chat input appears at bottom
- User message appears left
- Assistant message appears right
- Gemini returns response after send

## 6. Troubleshooting
- `Missing GOOGLE_API_KEY in .env`
  - Add `GOOGLE_API_KEY` to `.env`
- `404 model ... not found`
  - Set `GEMINI_MODEL` to one supported by your Gemini project
- Import errors
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
