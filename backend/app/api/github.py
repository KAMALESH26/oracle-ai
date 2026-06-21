from flask import Blueprint, jsonify

from app.database.mongodb import (
    mongo_db
)

github_bp = Blueprint(
    "github",
    __name__
)


@github_bp.route("/api/github")
def github_trends():

    repos = list(

        mongo_db[
            "github_trending"
        ].find(

            {},
            {
                "_id": 0
            }
        ).limit(50)
    )

    return jsonify(repos)