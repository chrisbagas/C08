from django.urls import path

from forum.views import createComment, createForum, deleteForum, detailView, homeView

urlpatterns = [
    path("", homeView, name="home"),
    path('create',  createForum.as_view(), name='forum_create'),
    path('comment/create',  createComment.as_view(), name='comment_create'),
    path('delete',  deleteForum.as_view(), name='forum_delete'),
    path("<int:pk>", detailView, name="forum_detail"),
    path('api/posts/', json, name='json'),
]
