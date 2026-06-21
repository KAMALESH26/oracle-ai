from app.services.ai.trend_analyst import (
    generate_ai_report
)

from app.services.trends.momentum_score import (
    calculate_momentum
)


class OracleAgent:

    def answer(self, question):

        momentum = calculate_momentum()

        trend_data = "\n".join(

            [
                f"{x['keyword']} "
                f"(growth={x['growth']}%)"

                for x in momentum[:20]
            ]
        )

        prompt = f"""
You are ORACLE AI.

Current trend data:

{trend_data}

Question:

{question}

Answer using the trend data.
"""

        from app.services.ai.gemini_client import model

        response = model.generate_content(
            prompt
        )

        return response.text