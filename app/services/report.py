from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    response, status_code = ReportController.get_report()
    return jsonify(response), status_code
