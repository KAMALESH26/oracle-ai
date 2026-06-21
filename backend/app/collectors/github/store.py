from app.database.mongodb import mongo_db

github_collection = (
    mongo_db["github_trending"]
)


def save_repositories(repositories):

    if repositories:

        github_collection.insert_many(
            repositories
        )

        print(

            f"Inserted "
            f"{len(repositories)} repos"
        )