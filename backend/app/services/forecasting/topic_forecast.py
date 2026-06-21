import pandas as pd

from statsmodels.tsa.holtwinters import (
    ExponentialSmoothing
)

from app.models.topic_history import (
    TopicHistory
)


def forecast_topic(topic):

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

    if len(rows) < 3:

        return None

    values = [

        row.mentions

        for row in rows
    ]

    series = pd.Series(values)

    model = (
        ExponentialSmoothing(
            series
        )
        .fit()
    )

    forecast = (
        model.forecast(1)
    )

    return round(
        float(
            forecast.iloc[0]
        ),
        2
    )