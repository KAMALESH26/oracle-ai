from app.services.topics.topic_summary import (
    get_topic_summary
)

from app.services.forecasting.time_series import (
    forecast_keyword
)


def forecast_topics():

    results = []

    topics = (
        get_topic_summary()
    )

    for topic in topics:

        prediction = (
            forecast_keyword(
                topic["topic"]
            )
        )

        results.append({

            "topic":
            topic["topic"],

            "current":
            topic["mentions"],

            "predicted":
            prediction
        })

    return results