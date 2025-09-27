from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

QUESTIONS_FILE = "data/questions.csv"
RESPONSES_FILE = "responses.csv"

# Initialize responses.csv if not exists
try:
    pd.read_csv(RESPONSES_FILE)
except FileNotFoundError:
    df = pd.DataFrame(columns=["student_id","class","subject","unit_id","topic","understanding_level","timestamp"])
    df.to_csv(RESPONSES_FILE,index=False)

# Get topics for a unit
@app.route("/get_topics", methods=["GET"])
def get_topics():
    unit_id = int(request.args.get("unit_id"))
    df = pd.read_csv(QUESTIONS_FILE)
    topics = df[df.unit_id == unit_id]["topic"].unique().tolist()
    return jsonify(topics)

# Log student topic ranking
@app.route("/log_response", methods=["POST"])
def log_response():
    data = request.json
    df = pd.read_csv(RESPONSES_FILE)
    new_row = {
        "student_id": data["student_id"],
        "class": data["class"],
        "subject": data["subject"],
        "unit_id": data["unit_id"],
        "topic": data["topic"],
        "understanding_level": data["understanding_level"],
        "timestamp": datetime.now()
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(RESPONSES_FILE,index=False)
    return jsonify({"status":"success"})

# Teacher dashboard - aggregated data
@app.route("/teacher_dashboard", methods=["GET"])
def teacher_dashboard():
    df = pd.read_csv(RESPONSES_FILE)
    agg = df.groupby(["student_id","unit_id","topic"])["understanding_level"].apply(list).reset_index()
    return jsonify(agg.to_dict(orient="records"))

# Generate homework CSV for a student
@app.route("/generate_homework", methods=["POST"])
def generate_homework():
    data = request.json
    student_id = data["student_id"]
    unit_id = data["unit_id"]
    num_questions = data.get("num_questions", 5)

    questions_df = pd.read_csv(QUESTIONS_FILE)
    unit_questions = questions_df[questions_df.unit_id == unit_id]

    # Randomly select questions
    hw_questions = unit_questions.sample(min(len(unit_questions), num_questions))
    hw_questions["student_id"] = student_id

    filename = f"homework_student_{student_id}_unit_{unit_id}.csv"
    hw_questions.to_csv(filename, index=False)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
