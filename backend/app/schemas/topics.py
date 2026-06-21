from flask import Blueprint
from flask import jsonify

from app.services.topics.topic_summary import (
    get_topic_summary
)

topics_bp = Blueprint(
    "topics",
    __name__
)


@topics_bp.route(
    "/api/topics"
)
def topics():

    return jsonify(
        get_topic_summary()
    )