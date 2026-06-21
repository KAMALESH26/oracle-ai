from app.main import app

from app.services.trends.momentum_score import (
    calculate_momentum
)

with app.app_context():

    results = calculate_momentum()

    for item in results[:20]:

        print(item)