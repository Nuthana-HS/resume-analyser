# Resume Analyser — AI-Powered Resume Feedback Web App

A web application that analyses your resume using AI and gives you instant feedback including an ATS compatibility score, matched keywords, missing keywords, strengths, improvements, and rewrite tips.

**Live Demo:** https://resume-analyser-khw8.onrender.com

**GitHub:** https://github.com/Nuthana-HS/resume-analyser

---

## What Is This?

This is a **web app** — it runs in your browser like a website, but does intelligent AI-powered work like an app. You upload your resume PDF, and within seconds the AI analyses it and gives you detailed, personalised feedback.

---

## What It Does

- Gives you an **ATS Compatibility Score** out of 100
- Shows **matched keywords** found in your resume (green tags)
- Shows **missing keywords** you should add (red tags)
- Lists your **strengths** based on resume content
- Lists **areas to improve**
- Gives **specific rewrite tips** to strengthen your resume
- Writes a **personalised summary** of your profile
- Optionally compares against a **job description** for targeted analysis

---

## How It Works

```
User uploads PDF resume
        ↓
PyMuPDF extracts all text from the PDF
        ↓
Text is split into sections: Skills, Experience, Education, Projects
        ↓
Groq AI (Llama 3.3 70B) analyses the resume with a structured prompt
        ↓
AI returns: score, keywords, strengths, improvements, rewrite tips
        ↓
Flask renders the results on a beautiful dashboard
        ↓
User sees full analysis in the browser
```

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Flask | Web framework — runs the website |
| PyMuPDF (fitz) | Reads and extracts text from PDF files |
| Groq API | Free AI provider — fast inference |
| Llama 3.3 70B | AI model that analyses the resume |
| python-dotenv | Loads API key securely from .env file |
| Gunicorn | Production web server for deployment |
| Render.com | Free cloud hosting platform |
| GitHub | Version control and code hosting |

---

## Project Structure

```
resume-analyser/
├── app.py                  ← Main Flask web server (routes)
├── analyser.py             ← Groq AI integration and response parser
├── parser.py               ← PDF text extraction and section splitter
├── .env                    ← Secret API key (never share or push this)
├── .gitignore              ← Files to exclude from GitHub
├── Procfile                ← Tells Render how to start the app
├── requirements.txt        ← Python libraries needed
├── README.md               ← This file
└── templates/
    ├── index.html          ← Upload page (homepage)
    └── result.html         ← Results dashboard page
```

---

## File Explanations

### `app.py`
The main Flask application. Handles two routes:
- `GET /` — Shows the upload page
- `POST /analyse` — Receives the PDF, runs analysis, shows results
- Uses `/tmp/uploads` folder for temporary file storage (works on all servers)

### `parser.py`
Uses PyMuPDF to open PDF files and extract all text page by page. Then splits the text into sections (Skills, Experience, Education, Projects) using keyword detection on each line.

### `analyser.py`
Connects to Groq API using your API key. Sends a carefully structured prompt with the resume text and optional job description. Parses the AI's structured response into a Python dictionary with score, keywords, strengths, improvements, and rewrite tips.

### `templates/index.html`
A clean upload form where users choose their PDF resume and optionally paste a job description for targeted analysis.

### `templates/result.html`
Displays the full AI analysis: ATS score card, summary paragraph, keyword tag clouds (green = matched, red = missing), and bullet-point lists for strengths, improvements, and rewrite tips.

### `Procfile`
Tells Render.com to start the app using gunicorn: `web: gunicorn app:app`

### `.env`
Stores your secret Groq API key locally. Never push this to GitHub.

---

## Local Setup (Run on Your Computer)

### Requirements
- Ubuntu / Linux / Mac / Windows
- Python 3.10 or higher

### Step 1 — Clone the repository
```bash
git clone https://github.com/Nuthana-HS/resume-analyser.git
cd resume-analyser
```

### Step 2 — Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install libraries
```bash
pip install -r requirements.txt
```

### Step 4 — Get a free Groq API key
1. Go to **https://console.groq.com**
2. Sign up free (no credit card needed)
3. Click **API Keys** → **Create API Key**
4. Copy the key (starts with `gsk_...`)

### Step 5 — Add your API key
```bash
nano .env
```
Add this line:
```
GROQ_API_KEY=gsk_your_actual_key_here
```
Save: `Ctrl+O` → Enter → `Ctrl+X`

### Step 6 — Run the app
```bash
python3 app.py
```

### Step 7 — Open in browser
Go to: **http://127.0.0.1:5000**

---

## How to Use

1. Open the app in your browser
2. Click **Choose File** and select your resume PDF
3. Optionally paste a job description for targeted scoring
4. Click **Analyse My Resume**
5. Wait 5-10 seconds for the AI to analyse
6. View your complete results on the dashboard

---

## Deployment (Render.com — Free)

This app is deployed on Render.com for free.

### Steps to deploy your own instance:

1. Push your code to GitHub
2. Go to **render.com** → sign up with GitHub
3. Click **New** → **Web Service**
4. Connect your GitHub repo
5. Set these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add Environment Variable:
   - Key: `GROQ_API_KEY`
   - Value: your `gsk_...` key
7. Click **Create Web Service**
8. Wait 2-3 minutes → get your live URL!

---

## API Used — Groq

- **Website:** https://console.groq.com
- **Free tier:** Yes — 14,400 requests/day free
- **Model used:** `llama-3.3-70b-versatile`
- **Why Groq:** Fastest free AI API available, results in ~2 seconds

---

## Common Errors and Fixes

| Error | Cause | Fix |
|---|---|---|
| `command 'python' not found` | Ubuntu uses python3 | Use `python3` instead of `python` |
| `429 RESOURCE_EXHAUSTED` | Gemini quota exceeded | Switch to Groq API (free) |
| `model_decommissioned` | Old Groq model removed | Use `llama-3.3-70b-versatile` |
| `FileNotFoundError: uploads/` | Folder doesn't exist on server | Use `/tmp/uploads` in app.py |
| `ModuleNotFoundError` | Library not installed | Run `pip install -r requirements.txt` |
| `(venv) not showing` | Virtual env not active | Run `source venv/bin/activate` |
| App slow on first load | Render free tier sleeps | Wait 30-50 seconds, then it's fast |

---

## Future Improvements

- Export analysis report as a downloadable PDF
- Let AI rewrite weak bullet points automatically
- Upload two resumes and compare them side by side
- Auto-fetch job description from a LinkedIn or Indeed URL
- Save and track multiple resume analyses with user accounts
- Support DOCX files in addition to PDF
- Show score improvement chart over multiple submissions

---

## What I Learned Building This

- How to extract text from PDF files using Python
- How to integrate AI APIs (Groq + Llama 3) into a web app
- How to build a web app using Flask
- How to use environment variables to keep API keys secure
- How to use Git and GitHub for version control
- How to deploy a Python web app to the internet using Render.com
- How to debug deployment errors (missing folders, dependency conflicts)

---

## Author

**Nuthana H S**
Built as a beginner Python + AI project — from zero to a fully deployed AI web app in one session.

- GitHub: https://github.com/Nuthana-HS
- Live App: https://resume-analyser-khw8.onrender.com
