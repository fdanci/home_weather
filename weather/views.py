from django.shortcuts import render
from weather.shared.forecast import Forecast


def index(request):
    """Show home page."""
    version = '0.1'
    try:
        forecast: Forecast = Forecast('cosna', test=True)
    except Exception as ex:
        context = {
            "error_message": ex,
            'version': version
        }
    else:
        context = {
            "max_temperature": forecast.max_temperature[0],
            "max_temperature_date": forecast.max_temperature[1],
            "min_temperature": forecast.min_temperature[0],
            "min_temperature_date": forecast.min_temperature[1],
            "error_message": None,
            "forecast_length": len(forecast.forecast_list),
            "headline": forecast.headline,
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
