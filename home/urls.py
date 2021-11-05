from django.urls import path
from .views import feedback, index

urlpatterns = [
    #Menambahkan path sesuai dengan urls
    path('', index, name='homepage'),
    path('feedback', feedback, name='feedback')
]