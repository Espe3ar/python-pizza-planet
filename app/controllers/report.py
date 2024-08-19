from sqlalchemy.exc import SQLAlchemyError

from app.controllers.base import BaseController

from ..repositories.managers import ReportManager


class ReportController(BaseController):
    manager = ReportManager

    @classmethod
    def get_report(cls):
        try:
            most_requested_ingredient = cls.manager.get_most_requested_ingredient()
            month_with_most_revenue = cls.manager.get_month_with_most_revenue()
            top_customers = cls.manager.get_top_customers()

            entire_report = {
                "most_requested_ingredient": most_requested_ingredient,
                "month_with_most_revenue": month_with_most_revenue,
                "top_customers": top_customers,
            }

            return entire_report,200
        except Exception as e:
            print(f"Error: {e}")
            return {"error": str(e)}, 500