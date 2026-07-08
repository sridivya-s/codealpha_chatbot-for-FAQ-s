from sklearn.metrics.pairwise import cosine_similarity

def get_best_answer(user_vector, faq_vectors, faq_answers, threshold=0.4):
    similarities = cosine_similarity(user_vector, faq_vectors)
    best_idx = similarities.argmax()
    best_score = similarities[0, best_idx]

    if best_score >= threshold:
        return faq_answers[best_idx]
    else:
        return "Sorry, I couldn't understand your question."