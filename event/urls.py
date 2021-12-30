from django.urls import path
from .views import index,event_detail,event_form,json,add

app_name="event"
urlpatterns = [
    #Menambahkan path sesuai dengan urls
    path('', index, name='index'),
    path('detail/<int:id>/', event_detail, name='detail'),
    path('form/', event_form, name='event_form'),
    path('json/',json,name="JSON"),
    path('post/',add,name='post')
]