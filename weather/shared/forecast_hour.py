
class ForecastHour:
    """Forecast model for a single hour.

    All members are not intended to be modified afterwards so are private."""

    def __init__(self,
                 date,

                 temperature,

                 real_feel_temperature,

                 rain_probability,
                 snow_probability,
                 ice_probability,

                 phrase,  # Used to determine which icon to use

                 is_daylight
                 ):
        self.__date = date

        self.__temperature = temperature

        self.__real_feel_temperature = real_feel_temperature

        self.__rain_probability = rain_probability
        self.__snow_probability = snow_probability
        self.__ice_probability = ice_probability

        self.__phrase = phrase

        self.__is_daylight = is_daylight

    @property
    def date(self):
        return self.__date

    def hour(self):
        return self.__date[11:13]

    @property
    def temperature(self):
        return self.__temperature

    @property
    def real_feel_temperature(self):
        return self.__real_feel_temperature

    @property
    def rain_probability(self):
        if self.__rain_probability == 0:
            return None
        return self.__rain_probability

    @property
    def snow_probability(self):
        if self.__snow_probability == 0:
            return None
        return self.__snow_probability

    @property
    def ice_probability(self):
        if self.__ice_probability == 0:
            return None
        return self.__ice_probability

    @property
    def icon(self):
        return self.__phrase

    @property
    def is_daylight(self):
        return self.__is_daylight

    def __str__(self):
        """Return all forecast data neatly formatted."""
        return f"\nDate: {self.date}" \
               f"\nTemperature: {self.__temperature}" \
               f"\nFelt temperature: {self.__real_feel_temperature}" \
               f"\nRain chance: {self.__rain_probability}" \
               f"\nSnow chance: {self.__snow_probability}" \
               f"\nIce chance: {self.__ice_probability}" \
               f"\nPhrase: {self.__phrase}" \
               f"\nIs day light: {self.__is_daylight}"
