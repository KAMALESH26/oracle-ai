from collections import Counter

from app.database.mongodb import (
    mongo_db
)

from app.services.sentiment.analyzer import (
    analyze_sentiment
)


def analyze_articles():

    articles = mongo_db[
        "rss_articles"
    ].find()

    counter = Counter()

    for article in articles:

        text = article.get(
            "title",
            ""
        )

        result = analyze_sentiment(
            text
        )

        counter[
            result["label"]
        ] += 1

    return counter