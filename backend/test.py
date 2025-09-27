from question_gen import generate_questions

# Test with a topic
topic = "Quadratic Equations"
questions = generate_questions(topic, difficulty="easy")
print("Easy Questions:", questions)

questions = generate_questions(topic, difficulty="hard")
print("Hard Questions:", questions)