from django.urls import path, include
from .views import index, post, add_post, edit_post, delete_post, json
import blog.urls as blog

urlpatterns = [
    path('', index, name='index'),
    path('add-post/', add_post, name='add-post'),
    path('api/posts/', json, name='json'),
    path('<slug:slug>/', post, name='post'),
    path('<slug:slug>/edit-post/', edit_post, name='edit-post'),
    path('<slug:slug>/delete-post/', delete_post, name='delete-post'),
]