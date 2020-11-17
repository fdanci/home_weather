from .forecast_item import ForecastItem
from weather.weather_sources.source_1 import Source1
import json


class Forecast:
    """List of forecast items."""

    def __init__(self):
        """Initialize the forecast list, read from weather api."""
        self.__json_data = json.loads(Source1.forecast_5days().text)
        self.__headline = self.__json_data['Headline']['Text']
        self.__headline_category = self.__json_data['Headline']['Category']
        self.__forecasts = []

        # Parse each forecast json, create forecast items, add them to the list.
        for forecast in self.__json_data['DailyForecasts']:
            forecast_item = self.__extract_forecast(forecast)
            self.__forecasts.append(forecast_item)

    @property
    def headline(self):
        """Returns headline for current 5 day forecast."""
        return self.__headline

    @property
    def headline_category(self):
        """Returns the headline category for current 5 days.
        Used to determine which icon."""
        return self.__headline_category

    def __extract_forecast(self, forecast):
        """
        Create forecast item from given json data.

        :param forecast: Forecast data json
        :return: Forecast item
        """
        date = forecast['Date']

        min_temperature = forecast['Temperature']['Minimum']['Value']
        max_temperature = forecast['Temperature']['Maximum']['Value']

        min_real_feel_temperature = forecast['RealFeelTemperature']['Minimum']['Value']
        max_real_feel_temperature = forecast['RealFeelTemperature']['Maximum']['Value']

        thunderstorm_probability_day = forecast['Day']['ThunderstormProbability']
        rain_probability_day = forecast['Day']['RainProbability']
        snow_probability_day = forecast['Day']['SnowProbability']
        ice_probability_day = forecast['Day']['IceProbability']

        thunderstorm_probability_night = forecast['Night']['ThunderstormProbability']
        ice_probability_night = forecast['Night']['RainProbability']
        ice_probability_night = forecast['Night']['SnowProbability']
        ice_probability_night = forecast['Night']['IceProbability']

        long_phrase_day = forecast['Day']['LongPhrase']
        long_phrase_night = forecast['Night']['LongPhrase']

        phrase_day = forecast['Day']['IconPhrase']
        phrase_night = forecast['Night']['IconPhrase']

        has_precipitations_day = forecast['Day']['HasPrecipitation']
        has_precipitations_night = forecast['Night']['HasPrecipitation']

        # Todo: Create and return forecast item.
        return None

    # Todo: Make getter for forecast list
