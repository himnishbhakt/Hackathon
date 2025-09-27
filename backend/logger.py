import csv
from datetime import datetime
import os

RESPONSES_FILE = "data/responses.csv"

if not os.path.exists(RESPONSES_FILE):
    with open(RESPONSES_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id","class","subject","unit_id","understanding_level","timestamp"])

def log_response(student_id, class_name, subject, unit_id, level):
    with open(RESPONSES_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([student_id, class_name, subject, unit_id, level, datetime.now()])
