from .forecast_item import ForecastItem
from weather.weather_sources.source_1 import Source1
import json


class Forecast:
    """List of forecast items."""

    def __init__(self, location, test=False):
        """Initialize the forecast list, read from weather api."""
        self.__test = test

        if not self.__test:
            if location == 'cosna':
                self.__json_data = json.loads(Source1.forecast_5days('280811').text)
            elif location == 'vatra_dornei':
                self.__json_data = json.loads(Source1.forecast_5days('275841').text)

            self.__headline = self.__json_data['Headline']['Text']
            self.__headline_category = self.__json_data['Headline']['Category']
        else:
            self.__json_data = {'DailyForecasts': [1, 2, 3, 4, 5]}
            self.__headline = 'Headline'
            self.__headline_category = 'Headline category'

        # This list contains all forecast items.
        self.__forecast_list = []

        self.__max_temperature = None
        self.__min_temperature = None

        # Parse each forecast json, create forecast items, add them to the list.
        for forecast in self.__json_data['DailyForecasts']:
            if not self.__test:
                forecast_item: ForecastItem = self.__extract_forecast(forecast)
            else:
                forecast_item: ForecastItem = self.__create_test_data()
            self.__forecast_list.append(forecast_item)

            # Determine highest & lowest temperatures.
            if not self.__test:
                if not self.__max_temperature and not self.__min_temperature:
                    self.__max_temperature = (float(forecast_item.max_temperature), forecast_item.date)
                    self.__min_temperature = (float(forecast_item.min_temperature), forecast_item.date)
                else:
                    if float(forecast_item.max_temperature) > self.__max_temperature[0]:
                        self.__max_temperature = (float(forecast_item.max_temperature), forecast_item.date)
                    if float(forecast_item.min_temperature) < self.__min_temperature[0]:
                        self.__min_temperature = (float(forecast_item.min_temperature), forecast_item.date)
            else:
                self.__max_temperature = (float(5.7), forecast_item.date)
                self.__min_temperature = (float(-5.7), forecast_item.date)

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

        phrase_day = forecast['Day']['IconPhrase']
        phrase_night = forecast['Night']['IconPhrase']

        has_precipitations_day = forecast['Day']['HasPrecipitation']
        has_precipitations_night = forecast['Night']['HasPrecipitation']

        forecast_item = ForecastItem(
            date=date[:10],
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
            phrase_day=phrase_day,
            phrase_night=phrase_night,
            has_precipitations_day=has_precipitations_day,
            has_precipitations_night=has_precipitations_night
        )
        return forecast_item

    @staticmethod
    def __create_test_data():
        """
        Create forecast item from given json data.

        :param forecast: Forecast data json
        :return: Forecast item
        """
        date = '12-04-2032'

        min_temperature = '-0.6'
        max_temperature = '5.3'

        min_real_feel_temperature = '-0.1'
        max_real_feel_temperature = '6.8'

        thunderstorm_probability_day = '30'
        rain_probability_day = '20'
        snow_probability_day = '1'
        ice_probability_day = '0'

        thunderstorm_probability_night = '45'
        rain_probability_night = '45'
        snow_probability_night = '12'
        ice_probability_night = '89'

        long_phrase_day = 'Frumos dar nu prea'
        long_phrase_night = 'Senin, dar norii vin'

        phrase_day = 'Frumos'
        phrase_night = 'Nu asa frumos'

        has_precipitations_day = 'True'
        has_precipitations_night = 'False'

        forecast_item = ForecastItem(
            date=date[:10],
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
