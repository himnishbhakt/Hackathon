from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from logger import log_response
from question_gen import generate_questions

app = Flask(__name__)
CORS(app)

STUDENTS_CSV = "backend/data/students.csv"
UNITS_CSV = "backend/data/units.csv"
RESPONSES_CSV = "backend/data/responses.csv"

@app.route("/students", methods=["GET"])
def get_students():
    df = pd.read_csv(STUDENTS_CSV)
    return jsonify(df.to_dict(orient="records"))

@app.route("/units", methods=["GET"])
def get_units():
    df = pd.read_csv(UNITS_CSV)
    return jsonify(df.to_dict(orient="records"))

@app.route("/log_response", methods=["POST"])
def log_student_response():
    data = request.json
    log_response(
        student_id=data["student_id"],
        class_name=data["class"],
        subject=data["subject"],
        unit_id=data["unit_id"],
        level=data["understanding_level"]
    )
    diff_map = {"green": ["medium", "hard"], "yellow": ["easy", "medium"], "red": ["easy"]}
    diffs = diff_map[data["understanding_level"]]
    all_questions = {}
    for d in diffs:
        all_questions[d] = generate_questions(data["unit_name"], d)
    return jsonify({"status": "success", "questions": all_questions})

@app.route("/teacher_dashboard", methods=["GET"])
def get_dashboard_data():
    df = pd.read_csv(RESPONSES_CSV)
    summary = df.groupby(["class","unit_id","understanding_level"]).size().unstack(fill_value=0)
    return jsonify(summary.to_dict())

if __name__ == "__main__":
    app.run(debug=True)
