import pandas as pd

from statsmodels.tsa.holtwinters import (
    ExponentialSmoothing
)

from app.models.trend_history import (
    TrendHistory
)


def forecast_keyword(keyword):

    rows = (

        TrendHistory.query

        .filter_by(
            keyword=keyword
        )

        .order_by(
            TrendHistory.collected_at
        )

        .all()

    )

    if len(rows) < 3:

        return None

    data = [

        row.mentions

        for row in rows
    ]

    series = pd.Series(data)

    model = (
        ExponentialSmoothing(
            series
        )
        .fit()
    )

    prediction = (
        model.forecast(1)
    )

    return float(
        prediction.iloc[0]
    )