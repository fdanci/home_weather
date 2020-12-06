class StrUtil:
    """Utility class used to format strings."""

    @staticmethod
    def format_location(location: str) -> str:
        """Return location neatly formatted."""
        if location == 'cosna':
            location = 'Coșna'
        elif location == 'vatra_dornei':
            location = 'Vatra Dornei'
        else:
            location = 'Ilișești'
        return location
