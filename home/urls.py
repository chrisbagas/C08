from django.urls import path
from .views import feedback, index, get_on_json, add

urlpatterns = [
    #Menambahkan path sesuai dengan urls
    path('', index, name='homepage'),
    path('feedback', feedback, name='feedback'),
    path('feedback/json/', get_on_json, name='json'),
    path('feedback/post/', add, name='add')
]