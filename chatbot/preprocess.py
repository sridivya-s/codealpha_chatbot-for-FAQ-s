import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()

    text = re.sub(r"[^\w\s]", "", text)

    tokens = word_tokenize(text)

    filtered = []
    for word in tokens:
        if word not in stop_words:
            filtered.append(word)
    
    return " ".join(filtered)
