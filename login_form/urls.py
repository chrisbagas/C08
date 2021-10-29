from django.urls import path
from .views import signupPage, loginPage

urlpatterns = [
    path('', signupPage, name='signup'),
    path('login', loginPage, name='login')
]