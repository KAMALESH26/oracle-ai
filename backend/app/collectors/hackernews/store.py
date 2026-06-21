from app.database.mongodb import mongo_db

hn_collection = (
    mongo_db["hackernews_posts"]
)


def save_posts(posts):

    if posts:

        hn_collection.insert_many(
            posts
        )

        print(
            f"Inserted {len(posts)} posts"
        )