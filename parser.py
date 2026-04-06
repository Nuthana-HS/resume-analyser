import fitz
import docx
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        return ""

def parse_sections(text):
    sections = {
        "skills": "",
        "experience": "",
        "education": "",
        "projects": "",
        "full_text": text
    }
    lines = text.split("\n")
    current_section = "full_text"
    for line in lines:
        line_lower = line.lower().strip()
        if "skill" in line_lower:
            current_section = "skills"
        elif "experience" in line_lower or "work" in line_lower:
            current_section = "experience"
        elif "education" in line_lower or "qualification" in line_lower:
            current_section = "education"
        elif "project" in line_lower:
            current_section = "projects"
        else:
            sections[current_section] += line + "\n"
    return sections