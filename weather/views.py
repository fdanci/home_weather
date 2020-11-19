from django.shortcuts import render
from weather.shared.forecast import Forecast


def index(request):
    """Show home page."""
    version = '0.1'
    return render(request, 'weather/index.html', {'version': version})


def cosna(request):
    """Show weather data about 'Cosna'."""
    try:
        forecast = Forecast()
    except Exception as ex:
        context = {
            "error_message": ex
        }
    else:
        context = {
            "forecast_list": forecast.forecast_list,
            "error_message": None
        }
    return render(request, 'weather/cosna.html', context)


def vatra_dornei(request):
    """Show weather data about 'Vatra Dornei'."""
    return render(request, 'weather/vatra_dornei.html', {})
