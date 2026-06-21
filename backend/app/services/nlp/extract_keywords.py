# app/services/nlp/extract_keywords.py

from keybert import KeyBERT

model = KeyBERT()


def extract_keywords(text):

    keywords = model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=5
    )

    return keywords