from django.urls import path
from .api.loginprofile.views_loginprofile import LoginProfileAPI, TempAPI
from .api.logoutprofile.views_logoutprofile import LogoutProfileAPI
profileurlpatterns = [
    path('login/', LoginProfileAPI.as_view()),
    path('logout/', LogoutProfileAPI.as_view()),
    path('temp/', TempAPI.as_view()),
]
