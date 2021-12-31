from django.urls import path
from .views import profile, edit_profile, get_profile_info_flutter,edit_profile_flutter

urlpatterns = [
    path('', profile, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('user/<uname>', get_profile_info_flutter),
    path('profile/flutter/edit/', edit_profile_flutter)
]