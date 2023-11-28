"""
URL configuration for ethanpolls project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse

from django.urls import include, path
from polls.views import index_view
def debug_view(request):
    return HttpResponse()
urlpatterns = [
    path("", index_view),

    path("__debug__/", include("debug_toolbar.urls")),

    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
