from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyse_resume(resume_text, job_description=""):
    prompt = f"""
You are an expert resume analyser and career coach.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description if job_description else "No job description provided. Do a general analysis."}

Please respond in this EXACT format:

ATS_SCORE: (number from 0 to 100)

MATCHED_KEYWORDS: (comma separated list)

MISSING_KEYWORDS: (comma separated list)

STRENGTHS:
- (strength 1)
- (strength 2)
- (strength 3)

IMPROVEMENTS:
- (improvement 1)
- (improvement 2)
- (improvement 3)

REWRITE_TIPS:
- (tip 1)
- (tip 2)

SUMMARY:
(2-3 sentence overall summary)
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return parse_response(response.choices[0].message.content)


def parse_response(text):
    result = {
        "ats_score": 0,
        "matched_keywords": [],
        "missing_keywords": [],
        "strengths": [],
        "improvements": [],
        "rewrite_tips": [],
        "summary": ""
    }

    lines = text.split("\n")
    current_key = None

    for line in lines:
        line = line.strip()
        if line.startswith("ATS_SCORE:"):
            try:
                result["ats_score"] = int(line.replace("ATS_SCORE:", "").strip())
            except:
                result["ats_score"] = 0
        elif line.startswith("MATCHED_KEYWORDS:"):
            val = line.replace("MATCHED_KEYWORDS:", "").strip()
            result["matched_keywords"] = [k.strip() for k in val.split(",") if k.strip()]
        elif line.startswith("MISSING_KEYWORDS:"):
            val = line.replace("MISSING_KEYWORDS:", "").strip()
            result["missing_keywords"] = [k.strip() for k in val.split(",") if k.strip()]
        elif line.startswith("STRENGTHS:"):
            current_key = "strengths"
        elif line.startswith("IMPROVEMENTS:"):
            current_key = "improvements"
        elif line.startswith("REWRITE_TIPS:"):
            current_key = "rewrite_tips"
        elif line.startswith("SUMMARY:"):
            current_key = "summary"
        elif line.startswith("- ") and current_key in ["strengths", "improvements", "rewrite_tips"]:
            result[current_key].append(line[2:])
        elif current_key == "summary" and line:
            result["summary"] += line + " "

    return result
