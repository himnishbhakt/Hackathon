from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

def generate_questions(unit_topic, difficulty="easy"):
    prompt = f"Generate 3 {difficulty} level questions for the topic: {unit_topic}"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    questions = [q.strip() for q in result.split("\n") if q.strip()]
    return questions
