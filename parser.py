import fitz  # this is PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

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

