from flask import Flask, render_template, request, redirect, url_for
import os
from parser import extract_text_from_pdf, parse_sections
from analyser import analyse_resume

import os
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs("uploads", exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/analyse", methods=["POST"])
def analyse():
    if "resume" not in request.files:
        return redirect(url_for("index"))

    file = request.files["resume"]
    job_description = request.form.get("job_description", "")

    if file.filename == "":
        return redirect(url_for("index"))

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    raw_text = extract_text_from_pdf(filepath)
    sections = parse_sections(raw_text)
    result = analyse_resume(sections["full_text"], job_description)

    os.remove(filepath)

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
