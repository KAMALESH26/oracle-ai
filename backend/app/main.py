from flask import Flask, jsonify
from flask_cors import CORS

from app.config.settings import Config
from app.database.postgres import db

from app.api.trends import trends_bp

from app.api.momentum import momentum_bp

from app.api.forecast import forecast_bp

from app.api.report import report_bp

from app.api.topic_history import (
    topic_history_bp
)

from app.api.ai_report import ai_report_bp

from app.api.github import github_bp

from app.api.topics import topics_bp

from app.api.chat import chat_bp

from app.api.confidence import confidence_bp

from app.api.insights import insights_bp

from app.api.topic_forecast import (
    topic_forecast_bp
)

from app.api.emerging_topics import (
    emerging_bp
)

app = Flask(__name__)

CORS(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = (
    f"postgresql://"
    f"{Config.POSTGRES_USER}:"
    f"{Config.POSTGRES_PASSWORD}@"
    f"{Config.POSTGRES_HOST}:"
    f"{Config.POSTGRES_PORT}/"
    f"{Config.POSTGRES_DB}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(
    trends_bp
)

app.register_blueprint(
    topic_forecast_bp
)

app.register_blueprint(
    momentum_bp
)

app.register_blueprint(
    topic_history_bp
)



app.register_blueprint(
    forecast_bp
)

app.register_blueprint(
    report_bp
)

app.register_blueprint(
    ai_report_bp
)

app.register_blueprint(
    github_bp
)

app.register_blueprint(
    topics_bp
)

app.register_blueprint(
    chat_bp
)

app.register_blueprint(
    confidence_bp
)

app.register_blueprint(
    insights_bp
)

app.register_blueprint(
    emerging_bp
)

@app.route("/health")
def health():

    return jsonify({
        "status": "healthy",
        "project": "ORACLE AI"
    })


from app.models import *

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)