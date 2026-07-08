from flask import Flask, render_template, request, jsonify
import json

from chatbot.preprocess import clean_text
from chatbot.vectorizer import fit_tfidf, transform_text
from chatbot.similarity import get_best_answer

app = Flask(__name__)

with open("faq_dataset.json") as f:
    faq_data = json.load(f)

faq_questions = []
faq_answers = []
for faq in faq_data:
    faq_questions.append(clean_text(faq["question"]))
    faq_answers.append(faq["answer"])

faq_vectors = fit_tfidf(faq_questions)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    user_question = request.json.get("question", "")
    clean_question = clean_text(user_question)
    user_vector = transform_text(clean_question)
    answer = get_best_answer(user_vector, faq_vectors, faq_answers)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True, port=5001)