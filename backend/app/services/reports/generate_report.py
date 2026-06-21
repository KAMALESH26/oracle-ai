from app.services.trends.momentum_score import (
    calculate_momentum
)


def generate_report():

    momentum = calculate_momentum()

    report = []

    report.append(
        "ORACLE AI TREND REPORT\n"
    )

    report.append(
        "=" * 40
    )

    for item in momentum[:10]:

        report.append(

            f"""
Topic: {item['keyword']}

Current Mentions:
{item['current']}

Growth:
{item['growth']}%

Momentum Score:
{item['momentum']}
"""
        )

    return "\n".join(report)