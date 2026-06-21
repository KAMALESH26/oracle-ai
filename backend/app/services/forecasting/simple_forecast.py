from app.services.trends.growth_analysis import (
    calculate_growth
)


def forecast_next_period():

    growth_data = calculate_growth()

    forecasts = []

    for item in growth_data:

        predicted = round(

            item["current"] *

            (1 + item["growth"] / 100),

            2
        )

        forecasts.append({

            "keyword": item["keyword"],

            "current": item["current"],

            "growth": item["growth"],

            "predicted_mentions": predicted
        })

    forecasts.sort(

        key=lambda x: x["predicted_mentions"],

        reverse=True
    )

    return forecasts