from datetime import datetime


class DateUtil:
    """Utility class used to get different required date information."""

    @staticmethod
    def get_current_day() -> int:
        """Return current day as number."""
        return datetime.now().day

    @staticmethod
    def get_current_month() -> int:
        """Return current month as number."""
        return datetime.now().month

    @staticmethod
    def get_current_year() -> int:
        """Return current year as number."""
        return datetime.now().year

    @staticmethod
    def get_date_today() -> str:
        """Return string date in 'yyyy-mm-dd' format."""
        return datetime.now().strftime("%Y-%m-%d")
