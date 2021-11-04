from django.urls import path

from forum.views import detailView, homeView

urlpatterns = [
    path("", homeView, name="home"),
    path("forum/<int:pk>", detailView, name="forum_detail"),
]
