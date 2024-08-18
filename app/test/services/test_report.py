import unittest
from unittest.mock import patch
from flask import Flask
import pytest

from app.services import report

class TestReportRoute(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(report, url_prefix='/report')
        self.client = self.app.test_client()


def test_get_report_success(client, report_uri, mock_report_controller_success):
    response = client.get(report_uri)
    pytest.assume(response.status_code == 200)
    data = response.json

    pytest.assume(data['most_requested_ingredient'] == 'Tomato')
    pytest.assume(data['month_with_most_revenue'] == 'June')
    pytest.assume(data['top_customers'] == ["John Doe", "Jane Smith"])

    mock_report_controller_success.assert_called_once()