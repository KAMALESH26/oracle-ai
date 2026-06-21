from app.services.ai.gemini_client import model

from app.services.trends.momentum_score import (
    calculate_momentum
)


def generate_ai_report():

    trends = calculate_momentum()

    trend_text = "\n".join(

        [
            f"{t['keyword']} | "
            f"mentions={t['current']} | "
            f"growth={t['growth']}%"

            for t in trends[:20]
        ]
    )

    prompt = f"""
You are ORACLE AI.

Analyze the following trends.

{trend_text}

Provide:

1. Top emerging trends
2. Fastest growing trends
3. Important observations
4. Predictions for next 7 days

Keep report concise.
"""

    response = model.generate_content(
        prompt
    )

    return response.text