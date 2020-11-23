from datetime import datetime


class ForecastItem:
    """Forecast model for a single day.

    All members are not intended to be modified afterwards so are private."""

    def __init__(self,
                 date,

                 min_temperature,
                 max_temperature,

                 min_real_feel_temperature,
                 max_real_feel_temperature,

                 thunderstorm_probability_day,
                 rain_probability_day,
                 snow_probability_day,
                 ice_probability_day,

                 thunderstorm_probability_night,
                 rain_probability_night,
                 snow_probability_night,
                 ice_probability_night,

                 long_phrase_day,
                 long_phrase_night,

                 phrase_day,
                 phrase_night,

                 has_precipitations_day,
                 has_precipitations_night,

                 today=False,
                 tomorrow=False
                 ):
        self.__date = date

        self.__min_temperature = min_temperature
        self.__max_temperature = max_temperature

        self.__min_real_feel_temperature = min_real_feel_temperature
        self.__max_real_feel_temperature = max_real_feel_temperature

        self.__thunderstorm_probability_day = thunderstorm_probability_day
        self.__rain_probability_day = rain_probability_day
        self.__snow_probability_day = snow_probability_day
        self.__ice_probability_day = ice_probability_day

        self.__thunderstorm_probability_night = thunderstorm_probability_night
        self.__rain_probability_night = rain_probability_night
        self.__snow_probability_night = snow_probability_night
        self.__ice_probability_night = ice_probability_night

        self.__long_phrase_day = long_phrase_day
        self.__long_phrase_night = long_phrase_night

        self.__phrase_day = phrase_day
        self.__phrase_night = phrase_night

        self.__has_precipitations_day = has_precipitations_day
        self.__has_precipitations_night = has_precipitations_night

        self.__today = today
        self.__tomorrow = tomorrow

    @property
    def date(self):
        current_day = datetime.now().day
        forecast_day = int((self.__date.split('-'))[2])

        # If today or tomorrow or the day after tomorrow return word instead of date.
        if current_day == forecast_day:
            return 'Astăzi'
        elif current_day + 1 == forecast_day:
            return 'Mâine'
        elif current_day + 2 == forecast_day:
            return 'Poimâine'
        return self.__date

    @property
    def min_temperature(self):
        return self.__min_temperature

    @property
    def max_temperature(self):
        return self.__max_temperature

    @property
    def min_real_feel_temperature(self):
        return self.__min_real_feel_temperature

    @property
    def max_real_feel_temperature(self):
        return self.__max_real_feel_temperature

    @property
    def thunderstorm_probability_day(self):
        return self.__thunderstorm_probability_day

    @property
    def rain_probability_day(self):
        return self.__rain_probability_day

    @property
    def snow_probability_day(self):
        return self.__snow_probability_day

    @property
    def ice_probability_day(self):
        return self.__ice_probability_day

    @property
    def thunderstorm_probability_night(self):
        return self.__thunderstorm_probability_night

    @property
    def rain_probability_night(self):
        return self.__rain_probability_night

    @property
    def snow_probability_night(self):
        return self.__snow_probability_night

    @property
    def ice_probability_night(self):
        return self.__ice_probability_night

    @property
    def long_phrase_day(self):
        return self.__long_phrase_day

    @property
    def long_phrase_night(self):
        return self.__long_phrase_night

    @property
    def phrase_day(self):
        return self.__phrase_day

    @property
    def phrase_night(self):
        return self.__phrase_night

    @property
    def has_precipitations_day(self):
        return self.__has_precipitations_day

    @property
    def has_precipitations_night(self):
        return self.__has_precipitations_night

    @property
    def today(self):
        """Return true if forecast represents current day."""
        return self.__today

    @property
    def tomorrow(self):
        """Return true if forecast represents tomorrow."""
        return self.__tomorrow

    def __str__(self):
        """Return all forecast data neatly formatted."""
        return f"\nDate: {self.date}" \
               f"\nMin temperature: {self.min_temperature}" \
               f"\nMax temperature: {self.__max_temperature}" \
               f"\nMin felt temperature: {self.min_real_feel_temperature}" \
               f"\nMax feld temperature: {self.max_real_feel_temperature}" \
               f"\nThunderstorm chance day: {self.__thunderstorm_probability_day}" \
               f"\nRain chance day: {self.__rain_probability_day}" \
               f"\nSnow chance day: {self.__snow_probability_day}" \
               f"\nIce chance day: {self.__ice_probability_day}" \
               f"\nThunderstorm chance night: {self.__thunderstorm_probability_night}" \
               f"\nRain chance night: {self.__rain_probability_night}" \
               f"\nSnow chance night: {self.__snow_probability_night}" \
               f"\nIce chance night: {self.__ice_probability_night}" \
               f"\nLong phrase day: {self.long_phrase_day}" \
               f"\nLong phrase Night: {self.long_phrase_night}" \
               f"\nPhrase day: {self.phrase_day}" \
               f"\nPhrase night: {self.phrase_night}" \
               f"\nHas precipitations during day: {self.__has_precipitations_day}" \
               f"\nHas precipitations during night: {self.__has_precipitations_night}" \
               f"\nToday: {self.__today}" \
               f"\nTomorrow: {self.__tomorrow}"
