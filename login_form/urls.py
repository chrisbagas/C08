from django.urls import path
from .views import loginPage, loginWithFlutter, logout, logoutFlutter, signupPage, signupWithFlutter

urlpatterns = [
    path('signup/', signupPage, name='signup'),
    path('login/', loginPage, name='login'),
    path('logout/', logout, name='logout'),
    path('loginflutter/', loginWithFlutter, name='loginFlutter'),
    path('signupflutter/', signupWithFlutter, name='registerFlutter'),
    path('logoutflutter/', logoutFlutter, name='logoutFlutter'),
]
