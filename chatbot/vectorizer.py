from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = None

def fit_tfidf(faq_questions):
    global vectorizer
    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    vectors = vectorizer.fit_transform(faq_questions)
    return vectors


def transform_text(text):
    global vectorizer
    return vectorizer.transform([text])