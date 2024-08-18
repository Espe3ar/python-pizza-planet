import pytest
from unittest.mock import patch
from app.controllers import ReportController

@pytest.fixture
def report_uri():
    return '/report/'

@pytest.fixture
def report_data():
    return {
        "most_requested_ingredient": "Tomato",
        "month_with_most_revenue": "June",
        "top_customers": ["John Doe", "Jane Smith"]
    }

@pytest.fixture
def mock_report_controller_success(report_data):
    with patch.object(ReportController, 'get_report', return_value=(report_data, 200)) as mock:
        yield mock

@pytest.fixture
def mock_report_controller_failure():
    with patch.object(ReportController, 'get_report', return_value=({"error": "Database error"}, 500)) as mock:
        yield mock

@pytest.fixture
def get_report_success(client, report_uri, mock_report_controller_success):
    response = client.get(report_uri)
    return response

@pytest.fixture
def get_report_failure(client, report_uri, mock_report_controller_failure):
    response = client.get(report_uri)
    return response
