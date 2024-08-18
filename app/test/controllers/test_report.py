import unittest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import SQLAlchemyError

from app.controllers.report import ReportController

class TestReportController(unittest.TestCase):

    @patch('app.controllers.report.ReportManager')
    def test_get_report_exception(self, mock_manager):
        mock_manager.get_most_requested_ingredient.side_effect = SQLAlchemyError("Database error")

        report, status_code = ReportController.get_report()

        self.assertEqual(status_code, 500)
        self.assertIn('error', report)
        self.assertIn('OperationalError', report['error'])

        mock_manager.get_month_with_most_revenue.assert_not_called()
        mock_manager.get_top_customers.assert_not_called()

if __name__ == '__main__':
    unittest.main()


