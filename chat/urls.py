from django.urls import path

from . import views
app_name = "chat"
# a ghost is typing in your computer

urlpatterns = [
    path('', views.index),
    path('create', views.post_chat),
    path('chats', views.get_chats)
]