from django.shortcuts import render
from weather.shared.forecast_5days import Forecast5days
from weather.shared.forecast_12hours import Forecast12hours
from weather.models import Forecast as Forecast_DB
from weather.shared.date_util import DateUtil
import logging

logger = logging.getLogger(__name__)


def index(request):
    """Show home page."""
    version = '1.0'

    try:
        # Retrieve the forecast for today, 'cosna' location.
        today_forecasts: Forecast_DB = Forecast_DB.objects.filter(location='cosna', date=DateUtil.get_date_today())

        # If forecast data exists, create 'Forecast' object from it.
        if today_forecasts:
            today_forecast = today_forecasts[0]
            forecast: Forecast5days = Forecast5days('cosna', raw_data=today_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast' object.
        else:
            forecast: Forecast5days = Forecast5days('cosna')
            today_forecast = Forecast_DB.objects.create(
                forecast=forecast.raw_data,
                date=DateUtil.get_date_today(),
                location='cosna'
            )
            today_forecast.save()

    # In case of an error, add the error message to context, to be displayed in UI.
    except Exception as err:
        logger.error(err)
        context = {
            "error_message": err,
            'version': version
        }

    # In case no errors occurred, create context for template.
    else:
        context = {
            "max_temperature": forecast.max_temperature[0],
            "max_temperature_date": forecast.max_temperature[1],
            "min_temperature": forecast.min_temperature[0],
            "min_temperature_date": forecast.min_temperature[1],
            "error_message": None,
            "forecast_length": len(forecast.forecast_list),
            "has_precipitations": forecast.has_precipitations(),
            "headline": forecast.headline,
            'version': version
        }

    return render(request, 'weather/index.html', context)


def cosna(request):
    """Show weather data about 'Cosna'."""
    try:
        # Retrieve the forecast for today, 'cosna' location.
        today_forecasts: Forecast_DB = Forecast_DB.objects.filter(location='cosna', date=DateUtil.get_date_today())
        current_hour_forecasts: Forecast_DB = Forecast_DB.objects.filter(location='cosna',
                                                                         date=DateUtil.get_date_hour_today())

        # If forecast day data exists, create 'Forecast5Days' object from it.
        if today_forecasts:
            today_forecast = today_forecasts[0]
            forecast: Forecast5days = Forecast5days('cosna', raw_data=today_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast5Days' object.
        else:
            forecast: Forecast5days = Forecast5days('cosna')
            today_forecast = Forecast_DB.objects.create(
                forecast=forecast.raw_data,
                date=DateUtil.get_date_today(),
                location='cosna'
            )
            today_forecast.save()

        # If forecast hour data exists, create 'Forecast12Hours' object from it.
        if current_hour_forecasts:
            current_hour_forecast = current_hour_forecasts[0]
            forecast_12hours: Forecast12hours = Forecast12hours('cosna', raw_data=current_hour_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast12Hours' object.
        else:
            forecast_12hours: Forecast12hours = Forecast12hours('cosna')
            current_hour_forecast = Forecast_DB.objects.create(
                forecast=forecast_12hours.raw_data,
                date=DateUtil.get_date_hour_today(),
                location='cosna'
            )
            current_hour_forecast.save()

    # In case of an error, add the error message to context, to be displayed in UI.
    except Exception as err:
        logger.error(err)
        context = {
            "error_message": err
        }

    # In case no errors occurred, create context for template.
    else:
        context = {
            "forecast_list": forecast.forecast_list,
            "forecast_hour_list": forecast_12hours.forecast_list,
            "forecast_length": len(forecast.forecast_list),
            "error_message": None
        }

    return render(request, 'weather/cosna.html', context)


def vatra_dornei(request):
    """Show weather data about 'Vatra Dornei'."""
    try:
        # Retrieve the forecast for today, 'vatra_dornei' location.
        today_forecasts: Forecast_DB = Forecast_DB.objects.filter(
            location='vatra_dornei', date=DateUtil.get_date_today())
        current_hour_forecasts: Forecast_DB = Forecast_DB.objects.filter(location='vatra_dornei',
                                                                         date=DateUtil.get_date_hour_today())

        # If forecast data exists, create 'Forecast' object from it.
        if today_forecasts:
            today_forecast = today_forecasts[0]
            forecast: Forecast5days = Forecast5days('vatra_dornei', raw_data=today_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast' object.
        else:
            forecast: Forecast5days = Forecast5days('vatra_dornei')
            today_forecast = Forecast_DB.objects.create(
                forecast=forecast.raw_data,
                date=DateUtil.get_date_today(),
                location='vatra_dornei'
            )
            today_forecast.save()

        # If forecast hour data exists, create 'Forecast12Hours' object from it.
        if current_hour_forecasts:
            current_hour_forecast = current_hour_forecasts[0]
            forecast_12hours: Forecast12hours = Forecast12hours('vatra_dornei', raw_data=current_hour_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast12Hours' object and save it to DB.
        else:
            forecast_12hours: Forecast12hours = Forecast12hours('vatra_dornei')
            current_hour_forecast = Forecast_DB.objects.create(
                forecast=forecast_12hours.raw_data,
                date=DateUtil.get_date_hour_today(),
                location='vatra_dornei'
            )
            current_hour_forecast.save()

    # In case of an error, add the error message to context, to be displayed in UI.
    except Exception as err:
        logger.error(err)
        context = {
            "error_message": err
        }

    # In case no errors occurred, create context for template.
    else:
        context = {
            "forecast_list": forecast.forecast_list,
            "forecast_hour_list": forecast_12hours.forecast_list,
            "forecast_length": len(forecast.forecast_list),
            "error_message": None
        }

    return render(request, 'weather/vatra_dornei.html', context)


def ilisesti(request):
    """Show weather data about 'Ilisesti'."""
    try:
        # Retrieve the forecast for today, 'ilisesti' location.
        today_forecasts: Forecast_DB = Forecast_DB.objects.filter(
            location='ilisesti', date=DateUtil.get_date_today())
        current_hour_forecasts: Forecast_DB = Forecast_DB.objects.filter(location='ilisesti',
                                                                         date=DateUtil.get_date_hour_today())

        # If forecast data exists, create 'Forecast' object from it.
        if today_forecasts:
            today_forecast = today_forecasts[0]
            forecast: Forecast5days = Forecast5days('ilisesti', raw_data=today_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast' object.
        else:
            forecast: Forecast5days = Forecast5days('ilisesti')
            today_forecast = Forecast_DB.objects.create(
                forecast=forecast.raw_data,
                date=DateUtil.get_date_today(),
                location='ilisesti'
            )
            today_forecast.save()

        # If forecast hour data exists, create 'Forecast12Hours' object from it.
        if current_hour_forecasts:
            current_hour_forecast = current_hour_forecasts[0]
            forecast_12hours: Forecast12hours = Forecast12hours('ilisesti', raw_data=current_hour_forecast.forecast)

        # Otherwise send request to the API, and then create 'Forecast12Hours' object and save it to DB.
        else:
            forecast_12hours: Forecast12hours = Forecast12hours('ilisesti')
            current_hour_forecast = Forecast_DB.objects.create(
                forecast=forecast_12hours.raw_data,
                date=DateUtil.get_date_hour_today(),
                location='ilisesti'
            )
            current_hour_forecast.save()

    # In case of an error, add the error message to context, to be displayed in UI.
    except Exception as err:
        logger.error(err)
        context = {
            "error_message": err
        }

    # In case no errors occurred, create context for template.
    else:
        context = {
            "forecast_list": forecast.forecast_list,
            "forecast_hour_list": forecast_12hours.forecast_list,
            "forecast_length": len(forecast.forecast_list),
            "error_message": None
        }

    return render(request, 'weather/ilisesti.html', context)
