from app.database.mongodb import rss_collection
from app.services.nlp.extract_keywords import (
    extract_keywords
)

articles = rss_collection.find().limit(5)

for article in articles:

    print("\nTITLE:")
    print(article["title"])

    print("\nKEYWORDS:")

    keywords = extract_keywords(
        article["title"]
    )

    for keyword, score in keywords:

        print(keyword)