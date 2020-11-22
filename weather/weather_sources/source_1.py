import requests
from decouple import config


class Source1:
    """
    Source: 'https://developer.accuweather.com/'
    """
    @staticmethod
    def today(location_id):
        """
        Read weather forecast for today.

        :return: The forecast in Json format.
        """
        url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + location_id + "" \
              "?apikey=" + config('ACC_WEATHER_KEY') + "&language=ro&details=true&metric=true"

        response = requests.request("GET", url)

        # Raise exception if no more requests for today!
        if response.status_code == 503:
            raise Exception('A fost depășit numărul de cereri pe ziua de azi')

        return response

    @staticmethod
    def forecast_5days(location_id):
        """
        Read weather forecast for 5 days.

        :return: The forecast in Json format.
        """
        url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" + location_id + "" \
              "?apikey=" + config('ACC_WEATHER_KEY') + "&language=ro&details=true&metric=true"

        response = requests.request("GET", url)

        # Raise exception if no more requests for today!
        if response.status_code == 503:
            raise Exception('A fost depășit numărul de cereri pe ziua de azi')

        return response
