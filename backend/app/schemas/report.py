from flask import Blueprint

from app.services.reports.generate_report import (
    generate_report
)

report_bp = Blueprint(
    "report",
    __name__
)


@report_bp.route("/api/report")
def report():

    return generate_report()