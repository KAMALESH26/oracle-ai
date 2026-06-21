from flask import (
    Blueprint,
    request,
    jsonify
)

from app.agents.oracle_agent import (
    OracleAgent
)

chat_bp = Blueprint(
    "chat",
    __name__
)

agent = OracleAgent()


@chat_bp.route(
    "/api/chat",
    methods=["POST"]
)
def chat():

    question = request.json[
        "question"
    ]

    answer = agent.answer(
        question
    )

    return jsonify({

        "answer": answer
    })