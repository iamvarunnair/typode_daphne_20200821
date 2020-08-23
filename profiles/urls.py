from django.urls import path
from .api.loginprofile.views_loginprofile import LoginProfileAPI
profileurlpatterns = [
    path('login/', LoginProfileAPI.as_view()),
]
