from django.urls import path
from . import views


urlpatterns = [
    path('', views.Roulette.as_view(), name='roulette-twist'),
]