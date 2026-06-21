from app.database.postgres import db

from app.models.topic_history import (
    TopicHistory
)


def save_topic_snapshot(
    topics
):

    for topic in topics:

        row = TopicHistory(

            topic=topic["topic"],

            mentions=topic["mentions"]
        )

        db.session.add(row)

    db.session.commit()