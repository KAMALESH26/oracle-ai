from collections import Counter

from app.database.mongodb import rss_collection

from app.services.nlp.extract_keywords import (
    extract_keywords
)


def get_top_trends(limit=20):

    counter = Counter()

    articles = rss_collection.find()

    for article in articles:

        keywords = extract_keywords(
            article["title"]
        )

        for keyword, score in keywords:

            counter[
                keyword.lower()
            ] += 1

    trends = []

    for keyword, count in counter.most_common(limit):

        trends.append({

            "keyword": keyword,

            "mentions": count,

            "trend_score": float(count)

        })

    return trends