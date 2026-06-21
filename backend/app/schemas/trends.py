from flask import Blueprint, jsonify

from app.services.trends.trend_score import (
    calculate_trends
)

trends_bp = Blueprint(
    "trends",
    __name__
)


@trends_bp.route("/api/trends")
def get_trends():

    trends = calculate_trends()

    return jsonify(trends[:20])