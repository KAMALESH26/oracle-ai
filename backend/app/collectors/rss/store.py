from backend.app.core.database.mongodb import rss_collection


def save_articles(articles):

    if articles:

       for article in articles:

            try:

                rss_collection.insert_one(
                    article
                )

            except Exception:

                pass

    print(
            f"Inserted {len(articles)} articles"
        )