from django.shortcuts import render
from weather.shared.forecast import Forecast


def index(request):
    """Show home page."""
    version = '0.1'
    try:
        forecast = Forecast('cosna', test=True)
    except Exception as ex:
        context = {
            "error_message": ex,
            'version': version
        }
    else:
        context = {
            "max_temperature": forecast.max_temperature,
            "min_temperature": forecast.min_temperature,
            "error_message": None,
            'version': version
        }
    return render(request, 'weather/index.html', context)


def cosna(request):
    """Show weather data about 'Cosna'."""
    try:
        forecast = Forecast('cosna', test=True)
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
    try:
        forecast = Forecast('vatra_dornei', test=True)
    except Exception as ex:
        context = {
            "error_message": ex
        }
    else:
        context = {
            "forecast_list": forecast.forecast_list,
            "error_message": None
        }
    return render(request, 'weather/vatra_dornei.html', context)
