from app.services.trends.trend_score import (
    calculate_trends
)

trends = calculate_trends()

print("\nTOP TRENDS\n")

for trend in trends[:20]:

    print(
        f"{trend['keyword']:30}"
        f"{trend['mentions']:5}"
        f"{trend['trend_score']:10}"
    )