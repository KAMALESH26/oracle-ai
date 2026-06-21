from flask import Blueprint
from flask import jsonify

from app.services.trends.aggregate_keywords import (
    get_top_trends
)

insights_bp = Blueprint(
    "insights",
    __name__
)


@insights_bp.route(
    "/api/insights"
)
def insights():

    trends = get_top_trends()

    if not trends:

        return jsonify({})

    top = trends[0]

    return jsonify({

        "top_trend":
            top["keyword"],

        "fastest_growing":
            top["keyword"],

        "prediction":
            f"{top['keyword']} likely to remain active"

    })