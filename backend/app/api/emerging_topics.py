from flask import Blueprint
from flask import jsonify

from app.services.topics.emerging_topics import (
    get_emerging_topics
)

emerging_bp = Blueprint(
    "emerging",
    __name__
)


@emerging_bp.route(
    "/api/emerging-topics"
)
def emerging_topics():

    return jsonify(
        get_emerging_topics()
    )