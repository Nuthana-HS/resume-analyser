# Resume Analyser — AI-Powered Resume Feedback Tool

A web application that analyses your resume using AI (Groq + Llama 3) and gives you an ATS compatibility score, matched/missing keywords, strengths, improvements, and rewrite tips — all in seconds.

---

## What This Project Does

Upload any PDF resume and (optionally) paste a job description. The app will:

- Give you an **ATS Compatibility Score** out of 100
- Show **matched keywords** found in your resume (green tags)
- Show **missing keywords** you should add (red tags)
- List your **strengths** based on the resume content
- List **areas to improve**
- Give **specific rewrite tips** to make your resume stronger
- Write a **personalised summary** of your resume

---

## Project Structure

```
resume-analyser/
├── app.py                  ← Main Flask web server (routes and logic)
├── analyser.py             ← Groq AI integration and response parsing
├── parser.py               ← PDF text extraction and section splitting
├── .env                    ← Secret API key (never share this file)
├── requirements.txt        ← All Python libraries needed
├── templates/
│   ├── index.html          ← Upload page (the homepage)
│   └── result.html         ← Results dashboard page
└── uploads/                ← Temporary folder for uploaded PDFs
```

---

## How It Works — Step by Step

```
User uploads PDF resume
        ↓
parser.py reads the PDF (using PyMuPDF)
        ↓
Text is split into sections: Skills, Experience, Education, Projects
        ↓
analyser.py sends the text + job description to Groq AI (Llama 3.3 70B model)
        ↓
AI returns structured analysis: score, keywords, strengths, tips
        ↓
Flask renders result.html with the full analysis
        ↓
User sees their results in the browser
```

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Main programming language |
| Flask | Web framework (runs the local website) |
| PyMuPDF (fitz) | Reads and extracts text from PDF files |
| Groq API | AI provider — fast and free |
| Llama 3.3 70B | The AI model that analyses the resume |
| python-dotenv | Loads the API key from the .env file securely |
| HTML + CSS | Frontend UI (upload page and results page) |

---

## Setup Instructions (Ubuntu/Linux)

### Step 1 — Install Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### Step 2 — Clone or create the project folder

```bash
mkdir resume-analyser
cd resume-analyser
```

### Step 3 — Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

You will see `(venv)` appear in your terminal. This means the virtual environment is active.

### Step 4 — Install all required libraries

```bash
pip install flask pymupdf python-dotenv groq
```

Or if a `requirements.txt` is provided:

```bash
pip install -r requirements.txt
```

### Step 5 — Get a free Groq API key

1. Go to **https://console.groq.com**
2. Sign up for a free account
3. Click **API Keys** → **Create API Key**
4. Copy the key (starts with `gsk_...`)

### Step 6 — Add your API key

Create a `.env` file in the project root:

```bash
nano .env
```

Add this line (replace with your actual key):

```
GROQ_API_KEY=gsk_your_actual_key_here
```

Save: `Ctrl+O` → Enter → `Ctrl+X`

### Step 7 — Create required folders

```bash
mkdir uploads templates
```

### Step 8 — Run the app

```bash
python3 app.py
```

### Step 9 — Open in browser

Go to: **http://127.0.0.1:5000**

---

## How to Use

1. Open **http://127.0.0.1:5000** in your browser
2. Click **Choose File** and select your resume PDF
3. (Optional) Paste a job description in the text box
4. Click **Analyse My Resume**
5. Wait 5–10 seconds for the AI to analyse
6. View your full results on the results page

---

## File Explanations

### `app.py`
The main Flask application. It handles two routes:
- `GET /` — Shows the upload page (index.html)
- `POST /analyse` — Receives the uploaded PDF, runs the analysis, and shows results

### `parser.py`
Uses PyMuPDF to open the PDF and extract all text page by page. Then splits the text into sections (Skills, Experience, Education, Projects) using keyword detection.

### `analyser.py`
Connects to the Groq API using your API key. Sends a carefully written prompt with the resume text and job description. Parses the AI's structured response into a Python dictionary with score, keywords, strengths, improvements, and tips.

### `templates/index.html`
A clean HTML form where users upload their PDF resume and paste an optional job description.

### `templates/result.html`
Displays the AI analysis results using HTML cards: ATS score, summary, keyword tags, bullet-point lists for strengths/improvements/tips.

### `.env`
Stores your secret Groq API key. This file should **never** be shared or pushed to GitHub.

---

## Requirements File

Create a `requirements.txt` with:

```
flask
pymupdf
python-dotenv
groq
```

---

## Common Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| `command 'python' not found` | Ubuntu uses `python3` | Use `python3` instead of `python` |
| `429 RESOURCE_EXHAUSTED` | Gemini free quota exceeded | Switch to Groq API (free, generous limits) |
| `model_decommissioned` | Old Groq model removed | Change model to `llama-3.3-70b-versatile` |
| `ModuleNotFoundError` | Library not installed | Run `pip install <library-name>` |
| `(venv)` not showing | Virtual environment not active | Run `source venv/bin/activate` |

---

## API Used — Groq

- **Website:** https://console.groq.com
- **Free tier:** Yes — very generous daily limits
- **Model used:** `llama-3.3-70b-versatile`
- **Speed:** One of the fastest AI APIs available (results in ~2 seconds)

---

## Future Improvements (Ideas)

- Export analysis report as a PDF download
- Let AI rewrite weak bullet points directly
- Compare two resumes side by side
- Add login so users can save their previous analyses
- Deploy online using Render.com or Railway.app (free hosting)

---

## Author

Built step by step as a beginner Python + AI project.  
Uses Flask for the backend, PyMuPDF for PDF parsing, and Groq AI for intelligent resume analysis.
