import json
import re
from chatbot.preprocess import clean_text
from chatbot.vectorizer import fit_tfidf, transform_text
from chatbot.similarity import get_best_answer

with open("faq_dataset.json") as f:
    faq_data = json.load(f)

faq_questions = []
faq_answers = []
for faq in faq_data:
    faq_questions.append(clean_text(faq["question"]))
    faq_answers.append(faq["answer"])

faq_vectors = fit_tfidf(faq_questions)

print("\n\n======= E-commerce FAQ Chatbot (CLI) =======")
print("Ask questions about orders, returns, payments, shipping, etc")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("\nYou: ")
    
    if user_input.lower() == "exit":
        break

    clean_q = clean_text(user_input)
    user_vector = transform_text(clean_q)

    answer = get_best_answer(user_vector, faq_vectors, faq_answers)
    answer = re.sub(r"[*_`]", "", answer)
    answer = answer.replace("\n", "\n     ").strip()

    print("Bot:", answer)