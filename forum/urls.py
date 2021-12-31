from django.urls import path

from forum.views import *

urlpatterns = [
    path("", homeView, name="home"),
    path('create',  createForum, name='forum_create'),

    # Flutter
    path('create-flutter',  create_forum_flutter, name='forum_create_flutter'),
    
    path('comment/create',  createComment, name='comment_create'),
    path("<int:pk>", detailView, name="forum_detail"),
    path('<int:pk>/delete',  delete_forum, name='forum_delete'),
    path('api', get_json, name='json'),

    # path('delete',  deleteForum.as_view(), name='forum_delete'),
]
