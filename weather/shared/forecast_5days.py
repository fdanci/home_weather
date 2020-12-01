from .forecast_day import ForecastDay
from weather.weather_sources.source_1 import Source1
import json
import logging

logger = logging.getLogger(__name__)


class Forecast5days:
    """List of forecast day items. It contains data 5 days worth."""

    def __init__(self, location, raw_data=None):
        """Initialize the forecast list, read from weather api, or load data from DB if present."""

        # Create json from already existent response, stored in DB.
        if raw_data:
            json_data = json.loads(raw_data)

        # Request the weather API for a new response.
        else:
            if location == 'cosna':
                self.__raw_data = Source1.forecast_5days('280811').text  # The response as it is received from the API
                json_data = json.loads(self.__raw_data)
            elif location == 'vatra_dornei':
                self.__raw_data = Source1.forecast_5days('275841').text  # The response as it is received from the API
                json_data = json.loads(self.__raw_data)

        self.__headline = json_data['Headline']['Text']
        self.__headline_category = json_data['Headline']['Category']
        # This list contains all forecast items.
        self.__forecast_list = []

        # These two will be of type tuple '(temperature<float>, date<str>)'.
        self.__max_temperature = None
        self.__min_temperature = None

        # Parse each forecast json, create forecast items, add them to the list.
        for forecast in json_data['DailyForecasts']:
            forecast_item: ForecastDay = self.__extract_forecast(forecast)

            self.__forecast_list.append(forecast_item)

            # Determine highest & lowest temperatures.
            if not self.__max_temperature and not self.__min_temperature:
                self.__max_temperature = (float(forecast_item.max_temperature), forecast_item.date)
                self.__min_temperature = (float(forecast_item.min_temperature), forecast_item.date)
            else:
                if float(forecast_item.max_temperature) > self.__max_temperature[0]:
                    self.__max_temperature = (float(forecast_item.max_temperature), forecast_item.date)
                if float(forecast_item.min_temperature) < self.__min_temperature[0]:
                    self.__min_temperature = (float(forecast_item.min_temperature), forecast_item.date)

    @property
    def headline(self):
        """Returns headline for current 5 day forecast."""
        return self.__headline

    @property
    def headline_category(self):
        """Returns the headline category for current 5 days.
        Used to determine which icon."""
        return self.__headline_category

    @staticmethod
    def __extract_forecast(forecast):
        """
        Create forecast item from given json data.

        :param forecast: Forecast data json
        :return: Forecast item
        """
        date = forecast['Date']

        sunrise = forecast['Sun']['Rise']
        sunset = forecast['Sun']['Set']

        min_temperature = forecast['Temperature']['Minimum']['Value']
        max_temperature = forecast['Temperature']['Maximum']['Value']

        min_real_feel_temperature = forecast['RealFeelTemperature']['Minimum']['Value']
        max_real_feel_temperature = forecast['RealFeelTemperature']['Maximum']['Value']

        thunderstorm_probability_day = forecast['Day']['ThunderstormProbability']
        rain_probability_day = forecast['Day']['RainProbability']
        snow_probability_day = forecast['Day']['SnowProbability']
        ice_probability_day = forecast['Day']['IceProbability']

        thunderstorm_probability_night = forecast['Night']['ThunderstormProbability']
        rain_probability_night = forecast['Night']['RainProbability']
        snow_probability_night = forecast['Night']['SnowProbability']
        ice_probability_night = forecast['Night']['IceProbability']

        long_phrase_day = forecast['Day']['LongPhrase']
        long_phrase_night = forecast['Night']['LongPhrase']

        icon_day = forecast['Day']['Icon']
        icon_night = forecast['Night']['Icon']

        phrase_day = forecast['Day']['IconPhrase']
        phrase_night = forecast['Night']['IconPhrase']

        has_precipitations_day = forecast['Day']['HasPrecipitation']
        has_precipitations_night = forecast['Night']['HasPrecipitation']

        forecast_item = ForecastDay(
            date=date[:10],
            sunrise=sunrise,
            sunset=sunset,
            min_temperature=min_temperature,
            max_temperature=max_temperature,
            min_real_feel_temperature=min_real_feel_temperature,
            max_real_feel_temperature=max_real_feel_temperature,
            thunderstorm_probability_day=thunderstorm_probability_day,
            rain_probability_day=rain_probability_day,
            snow_probability_day=snow_probability_day,
            ice_probability_day=ice_probability_day,
            thunderstorm_probability_night=thunderstorm_probability_night,
            rain_probability_night=rain_probability_night,
            snow_probability_night=snow_probability_night,
            ice_probability_night=ice_probability_night,
            long_phrase_day=long_phrase_day,
            long_phrase_night=long_phrase_night,
            icon_day=icon_day,
            icon_night=icon_night,
            phrase_day=phrase_day,
            phrase_night=phrase_night,
            has_precipitations_day=has_precipitations_day,
            has_precipitations_night=has_precipitations_night
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
