from weather.shared.date_util import DateUtil
from weather.shared.forecast_12hours import Forecast12hours
from weather.shared.forecast_5days import Forecast5days
from weather.models import Forecast as Forecast_DB


class Forecast:
    """Class used to read from database or from api and write information to database, information about forecasts."""

    @staticmethod
    def get_forecast_5days(location: str) -> Forecast5days:
        """
        Read forecast from db if available, or request from api otherwise and write to db.
        """

        # Retrieve the forecast for today from database, if it exists.
        today_forecasts: Forecast_DB = Forecast_DB.objects.filter(location=location, date=DateUtil.get_date_today())

        # If forecast data exists, create 'Forecast' object from it.
        if today_forecasts:
            today_forecast = today_forecasts[0]
            forecast: Forecast5days = Forecast5days(location, raw_data=today_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast' object and also save it to database.
        else:
            forecast: Forecast5days = Forecast5days(location)
            today_forecast = Forecast_DB.objects.create(
                forecast=forecast.raw_data,
                date=DateUtil.get_date_today(),
                location=location
            )
            today_forecast.save()

        return forecast

    @staticmethod
    def get_forecast_12hours(location: str) -> Forecast5days:
        """
        Read forecast for 12 hours from db if available, or request from api otherwise and write to db.
        """

        # Retrieve the forecast for next 12 hours from database, if it exists.
        current_hour_forecasts: Forecast_DB = Forecast_DB.objects.filter(location=location,
                                                                         date=DateUtil.get_date_hour_today())

        # If forecast hour data exists, create 'Forecast12Hours' object from it.
        if current_hour_forecasts:
            current_hour_forecast = current_hour_forecasts[0]
            forecast_12hours: Forecast12hours = Forecast12hours(location, raw_data=current_hour_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast12Hours' object.
        else:
            forecast_12hours: Forecast12hours = Forecast12hours(location)
            current_hour_forecast = Forecast_DB.objects.create(
                forecast=forecast_12hours.raw_data,
                date=DateUtil.get_date_hour_today(),
                location=location
            )
            current_hour_forecast.save()

        return forecast_12hours
