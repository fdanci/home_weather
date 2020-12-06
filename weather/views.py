from django.http import HttpResponse
from django.shortcuts import render, redirect
from weather.models import Settings

import logging

from weather.shared.forecast import Forecast
from weather.shared.str_util import StrUtil

logger = logging.getLogger(__name__)


def index(request):
    """Home page."""
    try:
        forecast_5days = Forecast.get_forecast_5days(Settings.objects.all()[0].location)
    except Exception as err:
        logger.error('weather.views.index')
        logger.error(err)
        context = {
            "error_message": err,
            'version': '2.1'
        }
    else:  # In case no errors occurred, create context for template.
        context = {
            "max_temperature": forecast_5days.max_temperature[0],
            "max_temperature_date": forecast_5days.max_temperature[1],
            "min_temperature": forecast_5days.min_temperature[0],
            "min_temperature_date": forecast_5days.min_temperature[1],
            "error_message": None,
            "forecast_length": len(forecast_5days.forecast_list),
            "has_precipitations": forecast_5days.has_precipitations(),
            "headline": forecast_5days.headline,
            'version': '2.1',
            'alarm_status': Settings.objects.all()[0].alarm_status,
            'alarm_status_sms': Settings.objects.all()[0].alarm_status_sms,
            'location': StrUtil.format_location(Settings.objects.all()[0].location)
        }

    return render(request, 'weather/index.html', context)


def cosna(request):
    """Show weather data about 'Cosna'."""
    try:
        forecast_5days = Forecast.get_forecast_5days('cosna')
        forecast_12hours = Forecast.get_forecast_12hours('cosna')
    except Exception as err:
        logger.error('weather.views.cosna')
        logger.error(err)
        context = {"error_message": err}
    else:  # In case no errors occurred, create context for template.
        context = {
            "forecast_list": forecast_5days.forecast_list,
            "forecast_hour_list": forecast_12hours.forecast_list,
            "forecast_length": len(forecast_5days.forecast_list),
            "error_message": None
        }

    return render(request, 'weather/cosna.html', context)


def vatra_dornei(request):
    """Show weather data about 'Vatra Dornei'."""
    try:
        forecast_5days = Forecast.get_forecast_5days('vatra_dornei')
        forecast_12hours = Forecast.get_forecast_12hours('vatra_dornei')
    except Exception as err:
        logger.error('weather.views.vatra_dornei')
        logger.error(err)
        context = {"error_message": err}
    else:  # In case no errors occurred, create context for template.
        context = {
            "forecast_list": forecast_5days.forecast_list,
            "forecast_hour_list": forecast_12hours.forecast_list,
            "forecast_length": len(forecast_5days.forecast_list),
            "error_message": None
        }

    return render(request, 'weather/vatra_dornei.html', context)


def ilisesti(request):
    """Show weather data about 'Ilisesti'."""
    try:
        forecast_5days = Forecast.get_forecast_5days('ilisesti')
        forecast_12hours = Forecast.get_forecast_12hours('ilisesti')
    except Exception as err:
        logger.error('weather.views.ilisesti')
        logger.error(err)
        context = {"error_message": err}
    else:  # In case no errors occurred, create context for template.
        context = {
            "forecast_list": forecast_5days.forecast_list,
            "forecast_hour_list": forecast_12hours.forecast_list,
            "forecast_length": len(forecast_5days.forecast_list),
            "error_message": None
        }

    return render(request, 'weather/ilisesti.html', context)


def blank(_):
    """
    Empty page, used to wake up the app and thus prevent it
    from going to sleep and shutting down the celery workers.
    """
    return HttpResponse("<p>blank</p>")


def update_email_alarm(_, alarm_status: str):
    """View used to update the email alarm on or off."""
    setting = Settings.objects.filter(pk=1)[0]
    setting.alarm_status = alarm_status

    # Save changes made to db.
    setting.save()

    return redirect('/')


def update_sms_alarm(_, alarm_status_sms: str):
    """View used to update the sms alarm on or off."""
    setting = Settings.objects.filter(pk=1)[0]
    setting.alarm_status_sms = alarm_status_sms

    # Save changes made to db.
    setting.save()

    return redirect('/')


def update_settings_email_alarm(_, alarm_status: str):
    """View used to update the email alarm on or off."""
    setting = Settings.objects.filter(pk=1)[0]
    setting.alarm_status = alarm_status

    # Save changes made to db.
    setting.save()

    return redirect('/settings')


def update_settings_sms_alarm(_, alarm_status_sms: str):
    """View used to update the sms alarm on or off."""
    setting = Settings.objects.filter(pk=1)[0]
    setting.alarm_status_sms = alarm_status_sms

    # Save changes made to db.
    setting.save()

    return redirect('/settings')


def update_settings_location(_, location: str):
    """View used to update the default location."""
    setting = Settings.objects.filter(pk=1)[0]
    setting.location = location

    # Save changes made to db.
    setting.save()

    return redirect('/settings')


def update_settings_day(_, day: str):
    """View used to update the default location."""
    setting = Settings.objects.filter(pk=1)[0]
    setting_day = setting.day
    setting_day_list: list[str] = setting_day.split(',')

    if '' in setting_day_list:
        setting_day_list.remove('')

    # If setting already contains this day,
    # it must be removed from the list, else it will be added.
    if day not in setting_day_list:
        setting_day_list.append(day)
    else:
        setting_day_list.remove(day)
    setting_day_list.sort()

    # Convert list of str to str, where days separated by comma.
    setting_day = ','.join(setting_day_list)
    setting.day = setting_day

    # Save changes made to db.
    setting.save()

    return redirect('/settings')


def settings(request):
    """View for the 'Settings' page."""
    setting = Settings.objects.all()[0]

    context = {
        'alarm_status': setting.alarm_status,
        'alarm_status_sms': setting.alarm_status_sms,
        'location': setting.location,
        'hour': setting.hour,
        'day_list': setting.day.split(','),
        "error_message": None
    }

    return render(request, 'weather/settings.html', context)
