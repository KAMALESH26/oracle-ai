# app/services/nlp/test_keywords.py

from app.services.nlp.extract_keywords import (
    extract_keywords
)

text = """
OpenAI is still working on that super app
"""

keywords = extract_keywords(text)

print(keywords)