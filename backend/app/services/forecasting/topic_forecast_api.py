from app.models.topic_history import (
    TopicHistory
)

from app.services.forecasting.topic_forecast import (
    forecast_topic
)


def get_topic_forecasts():

    topics = (

        TopicHistory.query
        .with_entities(
            TopicHistory.topic
        )
        .distinct()
        .all()

    )

    results = []

    for row in topics:

        topic = row[0]

        latest = (

            TopicHistory.query

            .filter_by(
                topic=topic
            )

            .order_by(
                TopicHistory.collected_at.desc()
            )

            .first()

        )

        prediction = (
            forecast_topic(
                topic
            )
        )

        results.append({

            "topic":
            topic,

            "current":
            latest.mentions,

            "predicted":
            prediction
        })

    return results