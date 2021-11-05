from django.urls import path
from .views import loginPage, logout, signupPage

urlpatterns = [
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logout, name='logout'),
]
