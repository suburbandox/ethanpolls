from django.urls import path

from . import views
app_name = "blog"
# a ghost is typing in your computer

urlpatterns = [
    path("", views.blog_list_view),
    path("<int:pk>",views.blog_detail_view),
    path("create",views.blog_create_view)

   
]