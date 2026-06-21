from app.main import app

from app.services.reports.generate_report import (
    generate_report
)

with app.app_context():

    print(
        generate_report()
    )