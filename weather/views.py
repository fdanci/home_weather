from django.shortcuts import render
from weather.shared.forecast import Forecast


def index(request):
    """Show home page."""
    version = '0.1'
    return render(request, 'weather/index.html', {'version': version})


def cosna(request):
    """Show weather data about 'Cosna'."""

    # Todo: Read 5 days forecast from weather API.

    forecast_list = []

    forecast = Forecast()

    context = {
        "forecast_list": forecast_list
    }

    return render(request, 'weather/cosna.html', context)


def vatra_dornei(request):
    """Show weather data about 'Vatra Dornei'."""
    return render(request, 'weather/vatra_dornei.html', {})
