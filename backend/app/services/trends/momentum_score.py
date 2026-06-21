from app.services.trends.growth_analysis import (
    calculate_growth
)


def calculate_momentum():

    growth_data = calculate_growth()

    results = []

    for item in growth_data:

        momentum = (
            item["current"] *
            (1 + item["growth"] / 100)
        )

        results.append({

            "keyword": item["keyword"],

            "current": item["current"],

            "growth": item["growth"],

            "momentum": round(
                momentum,
                2
            )
        })

    results.sort(
        key=lambda x: x["momentum"],
        reverse=True
    )

    return results