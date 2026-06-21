from flask import Blueprint, jsonify

from app.services.confidence.calculate import (
    calculate_confidence
)

confidence_bp = Blueprint(
    "confidence",
    __name__
)


@confidence_bp.route(
    "/api/confidence"
)
def confidence():

    return jsonify(
        calculate_confidence()
    )