from django.urls import path
from .views import index,event_detail

urlpatterns = [
    #Menambahkan path sesuai dengan urls
    path('', index, name='index'),
    path('/<int:id>/', event_detail, name='event'),
]