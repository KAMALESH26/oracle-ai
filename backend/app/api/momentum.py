from flask import Blueprint, jsonify

from app.services.trends.momentum_score import (
    calculate_momentum
)

momentum_bp = Blueprint(
    "momentum",
    __name__
)


@momentum_bp.route("/api/momentum")
def get_momentum():

    results = calculate_momentum()

    return jsonify(results[:20])