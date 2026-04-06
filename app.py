import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from parser import extract_text, parse_sections
from analyser import analyse_resume, rewrite_bullet

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

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

    raw_text = extract_text(filepath)
    sections = parse_sections(raw_text)
    result = analyse_resume(sections["full_text"], job_description)

    os.remove(filepath)

    return render_template("result.html", result=result)

@app.route("/rewrite", methods=["POST"])
def rewrite():
    bullet = request.form.get("bullet", "")
    if not bullet:
        return jsonify({"rewritten": "No text provided"}), 400
    result = rewrite_bullet(bullet)
    return jsonify({"rewritten": result})

if __name__ == "__main__":
    app.run(debug=True)