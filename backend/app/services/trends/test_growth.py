from app.main import app

from app.services.trends.growth_analysis import (
    calculate_growth
)

with app.app_context():

    growth = calculate_growth()

    for item in growth:

        print(item)