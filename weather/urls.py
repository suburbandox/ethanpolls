from django.urls import path

from . import views
app_name = "weather"

urlpatterns = [
    path("", views.weather_index)

]