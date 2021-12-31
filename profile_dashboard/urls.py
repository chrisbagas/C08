from django.urls import path
from .views import profile, edit_profile, get_profile_info_flutter,edit_profile_flutter, edit_profile_flutter_noPic

urlpatterns = [
    path('', profile, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('user/<uname>', get_profile_info_flutter),
    path('edit/flutter/', edit_profile_flutter),
    path('edit/flutter/nopic', edit_profile_flutter_noPic)
]