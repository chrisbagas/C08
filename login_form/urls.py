from django.urls import path
from .views import signupPage, loginPage

urlpatterns = [
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login')
]