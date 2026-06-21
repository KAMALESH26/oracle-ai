from flask import Blueprint
from flask import jsonify

from app.services.forecasting.topic_forecast_api import (
    get_topic_forecasts
)

topic_forecast_bp = Blueprint(
    "topic_forecast",
    __name__
)


@topic_forecast_bp.route(
    "/api/topic-forecast"
)
def topic_forecast():

    return jsonify(
        get_topic_forecasts()
    )