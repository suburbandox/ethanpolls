from django.urls import path

from . import views
app_name = "cocktails"

urlpatterns = [
    path("", views.cocktailindex),
    path("api", views.cocktailapi),
    
]