from transformers import pipeline
import pandas as pd

# Zero-shot classification pipeline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Read AP Chem questions
df = pd.read_csv("data/questions.csv")

# Define candidate topics and difficulties
topic_candidates = ["Stoichiometry", "Thermodynamics", "Equilibrium", "Acid-Base", "Redox", "Kinetics"]
difficulty_candidates = ["easy", "medium", "hard"]

classified = []
for q in df["question"]:
    topic_pred = classifier(q, topic_candidates)["labels"][0]
    diff_pred = classifier(q, difficulty_candidates)["labels"][0]
    classified.append({
        "question": q,
        "topic": topic_pred,
        "difficulty": diff_pred
    })

# Show results
for c in classified:
    print(c)