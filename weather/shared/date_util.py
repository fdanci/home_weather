from datetime import datetime


class DateUtil:
    """Utility class used to get different required date information & formats."""

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
        """Return string date in 'yyyy-mm-dd' e.g. (2020-11-30) format."""
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def get_date_hour_today() -> str:
        """Return string date in 'yyyy-mm-ddTH' e.g. (2020-11-30T16) format."""
        return datetime.now().strftime("%Y-%m-%dT%H")

    @staticmethod
    def get_hour_today() -> str:
        """Return string date in 'H' e.g. (06) format."""
        return datetime.now().strftime("%H")
