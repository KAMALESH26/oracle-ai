from collections import Counter

from app.database.mongodb import rss_collection
from app.services.nlp.extract_keywords import (
    extract_keywords
)


def calculate_trends():

    counter = Counter()

    articles = rss_collection.find()

    total_articles = 0

    for article in articles:

        total_articles += 1

        keywords = extract_keywords(
            article["title"]
        )

        for keyword, score in keywords:

            counter[keyword.lower()] += 1

    trends = []

    for keyword, count in counter.items():

        trend_score = round(
            (count / total_articles) * 100,
            2
        )

        trends.append({
            "keyword": keyword,
            "mentions": count,
            "trend_score": trend_score
        })

    trends.sort(
        key=lambda x: x["trend_score"],
        reverse=True
    )

    return trends