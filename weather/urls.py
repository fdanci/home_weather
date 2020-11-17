from django.urls import path

from . import views

app_name = 'weather'
urlpatterns = [
    path('', views.index, name='index'),
    path('cosna/', views.cosna, name='cosna'),
    path('vatra_dornei/', views.vatra_dornei, name='vatra_dornei'),
]
