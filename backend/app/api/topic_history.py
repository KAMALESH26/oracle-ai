from flask import Blueprint
from flask import jsonify

from app.models.topic_history import (
    TopicHistory
)

topic_history_bp = Blueprint(
    "topic_history",
    __name__
)


@topic_history_bp.route(
    "/api/topic-history/<topic>"
)
def topic_history(topic):

    rows = (

        TopicHistory.query

        .filter_by(
            topic=topic
        )

        .order_by(
            TopicHistory.collected_at
        )

        .all()

    )

    data = []

    for row in rows:

        data.append({

            "time":
            row.collected_at.strftime(
                "%H:%M"
            ),

            "mentions":
            row.mentions

        })

    return jsonify(data)