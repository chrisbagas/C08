from django.urls import path
from .views import index,event_detail,event_form

urlpatterns = [
    #Menambahkan path sesuai dengan urls
    path('', index, name='index'),
    path('detail/<int:id>/', event_detail, name='detail'),
    path('form/', event_form, name='event_form')
]