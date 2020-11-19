import requests
from decouple import config


class Source1:
    """
    Source: 'https://developer.accuweather.com/'
    """

    @staticmethod
    def today():
        """
        Read weather forecast for today.

        :return: The forecast in Json format.
        """
        url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/280811" \
              "?apikey=" + config('ACC_WEATHER_KEY') + "&language=ro&details=true&metric=true"

        response = requests.request("GET", url)

        return response

    @staticmethod
    def forecast_5days():
        """
        Read weather forecast for 5 days.

        :return: The forecast in Json format.
        """
        url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/280811" \
              "?apikey=" + config('ACC_WEATHER_KEY') + "&language=ro&details=true&metric=true"

        response = requests.request("GET", url)

        # Raise exception if no more requests for today!
        if response.status_code == 503:
            raise Exception('The allowed number of requests has been exceeded.')

        return response
