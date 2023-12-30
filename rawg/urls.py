from django.urls import path

from . import views
app_name = "rawg"

urlpatterns = [
    path("", views.rawg_index)

]