from collections import Counter

from app.database.mongodb import (
    mongo_db
)


def get_unified_trends():

    counter = Counter()

    # RSS Articles

    articles = mongo_db[
        "rss_articles"
    ].find()

    for article in articles:

        title = article.get(
            "title",
            ""
        )

        words = title.lower().split()

        for word in words:

            if len(word) > 4:

                counter[word] += 1

    # GitHub Repositories

    repos = mongo_db[
        "github_trending"
    ].find()

    for repo in repos:

        name = repo.get(
            "repository",
            ""
        )

        words = (
            name.lower()
            .replace("/", " ")
            .split()
        )

        for word in words:

            if len(word) > 3:

                counter[word] += 1

    return counter.most_common(50)