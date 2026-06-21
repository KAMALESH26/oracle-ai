from app.services.trends.momentum_score import (
    calculate_momentum
)


def calculate_confidence():

    momentum = calculate_momentum()

    results = []

    for item in momentum:

        confidence = min(

            100,

            item["momentum"] * 2
        )

        results.append({

            "keyword":
            item["keyword"],

            "confidence":
            round(confidence, 2)
        })

    return results