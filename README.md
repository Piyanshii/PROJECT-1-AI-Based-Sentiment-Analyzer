## AI-Based Sentiment Analyzer

A simple web app that uses a pretrained Hugging Face Transformers model to perform sentiment analysis on text.  
Built with **Flask** on the backend and a clean, responsive UI on the frontend.

---

## Features

- **Real‑time sentiment analysis** (positive / negative / neutral) for any input text
- **Confidence score** shown as a percentage
- **Modern, responsive UI** with a card-based layout
- Powered by the Hugging Face `pipeline("sentiment-analysis")`

---

## Tech Stack

- **Python**
- **Flask**
- **Hugging Face Transformers**
- **HTML / CSS**

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd "PROJECT 1 AI-Based Sentiment Analyzer"
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv

# On Windows (PowerShell)
.venv\Scripts\Activate.ps1

# On Windows (cmd)
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

The first run may also download the pretrained sentiment model from Hugging Face, so it can take a little while.

### 4. Run the app

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

---

## Usage

1. Open the app in your browser.
2. Paste or type the text you want to analyze into the text area.
3. Click **“Analyze sentiment”**.
4. The app will display:
   - The **predicted sentiment**
   - The **confidence** (percentage)
   - The **original text** that was analyzed

---

## Project Structure

```text
PROJECT 1 AI-Based Sentiment Analyzer/
├─ app.py               # Flask application and routing
├─ requirements.txt     # Python dependencies
├─ templates/
│  └─ index.html        # Main HTML template
└─ static/
   └─ style.css         # Styles for the UI
```

---

## Customization

- **Model**: In `app.py`, the line `pipeline("sentiment-analysis")` can be changed to use a specific model from Hugging Face (e.g., `"distilbert-base-uncased-finetuned-sst-2-english"`).
- **UI**: Adjust styles in `static/style.css` or modify the layout in `templates/index.html`.

---

## Troubleshooting

- **Slow first request**: The first run may be slow while the model downloads; subsequent runs should be much faster.
- **CUDA / GPU warnings**: If you don’t have a GPU configured, Transformers may show CUDA-related warnings; these are usually safe to ignore for simple CPU usage.
- **Port already in use**: If port 5000 is busy, set `app.run(debug=True, port=5001)` (or any free port) in `app.py`.

---

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)

