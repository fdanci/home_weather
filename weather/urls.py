from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('cosna/', views.cosna, name='cosna'),
    path('vatra_dornei/', views.vatra_dornei, name='vatra_dornei'),
    path('ilisesti/', views.ilisesti, name='ilisesti'),
    path('blank/', views.blank, name='blank'),
    path('settings/', views.settings, name='settings'),
    path('update_email_alarm/<str:alarm_status>/', views.update_email_alarm, name='update_email_alarm'),
    path('update_sms_alarm/<str:alarm_status_sms>/', views.update_sms_alarm, name='update_sms_alarm'),
    path('update_settings_email_alarm/<str:alarm_status>/', views.update_settings_email_alarm,
         name='update_settings_email_alarm'),
    path('update_settings_sms_alarm/<str:alarm_status_sms>/', views.update_settings_sms_alarm,
         name='update_settings_sms_alarm'),
    path('update_settings_location/<str:location>/', views.update_settings_location, name='update_settings_location'),
    path('update_settings_day/<str:day>/', views.update_settings_day, name='update_settings_day'),
]
