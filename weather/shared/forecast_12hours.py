from .forecast_hour import ForecastHour
from weather.weather_sources.source_1 import Source1
import json
import logging

logger = logging.getLogger(__name__)


class Forecast12hours:
    """List of forecast hour items. It contains accurate data 12 hours worth."""

    def __init__(self, location, raw_data=None):
        """Initialize the forecast list, read from weather api, or load data from DB if present."""

        # Create json from already existent response, stored in DB.
        if raw_data:
            json_data = json.loads(raw_data)

        # Request the weather API for a new response.
        else:
            if location == 'cosna':
                self.__raw_data = Source1.forecast_12hours('280811').text  # The response received from the API
                json_data = json.loads(self.__raw_data)
            elif location == 'vatra_dornei':
                self.__raw_data = Source1.forecast_12hours('275841').text  # The response received from the API
                json_data = json.loads(self.__raw_data)
            elif location == 'ilisesti':
                self.__raw_data = Source1.forecast_12hours('280883').text  # The response received from the API
                json_data = json.loads(self.__raw_data)

        self.__forecast_list = []

        # Parse each forecast hour json item, create forecast hour items, add them to the list.
        for forecast in json_data:
            forecast_item: ForecastHour = self.__extract_forecast(forecast)
            self.__forecast_list.append(forecast_item)

    @staticmethod
    def __extract_forecast(forecast):
        """
        Create forecast hour item from given json data.

        :param forecast: Forecast data json
        :return: Forecast hour item
        """
        date = forecast['DateTime']

        icon = forecast['WeatherIcon']

        temperature = forecast['Temperature']['Value']

        real_feel_temperature = forecast['RealFeelTemperature']['Value']

        rain_probability = forecast['RainProbability']
        snow_probability = forecast['SnowProbability']
        ice_probability = forecast['IceProbability']

        phrase = forecast['IconPhrase']

        is_daylight = forecast['IsDaylight']

        forecast_item = ForecastHour(
            date=date[:13],
            icon=icon,
            temperature=temperature,
            real_feel_temperature=real_feel_temperature,
            rain_probability=rain_probability,
            snow_probability=snow_probability,
            ice_probability=ice_probability,
            phrase=phrase,
            is_daylight=is_daylight
        )
        return forecast_item

    @property
    def forecast_list(self):
        return self.__forecast_list

    @property
    def min_temperature(self):
        return self.__min_temperature

    @property
    def max_temperature(self):
        return self.__max_temperature

    @property
    def raw_data(self):
        return self.__raw_data
