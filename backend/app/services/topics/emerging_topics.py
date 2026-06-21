from collections import defaultdict

from app.models.topic_history import (
    TopicHistory
)


def get_emerging_topics():

    rows = (

        TopicHistory.query

        .order_by(
            TopicHistory.collected_at
        )

        .all()

    )

    history = defaultdict(list)

    for row in rows:

        history[
            row.topic
        ].append(
            row.mentions
        )

    results = []

    for topic, values in history.items():

        if len(values) < 2:

            continue

        growth = (

            values[-1]
            -
            values[0]

        )

        results.append({

            "topic":
            topic,

            "growth":
            growth
        })

    return sorted(

        results,

        key=lambda x:
        x["growth"],

        reverse=True
    )