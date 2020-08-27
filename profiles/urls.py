from django.urls import path
from .api.loginprofile.views_loginprofile import LoginProfileAPI, TempAPI
from .api.logoutprofile.views_logoutprofile import LogoutProfileAPI
from .api.checkuserpresence.views_checkuserpresence import CheckUserPresenceAPI
from .api.signupprofile.views_signupprofile import SignupProfileAPI

profileurlpatterns = [
    path('login/', LoginProfileAPI.as_view()),
    path('logout/', LogoutProfileAPI.as_view()),
    path('check_email_presence/', CheckUserPresenceAPI.as_view()),
    path('signup_profile/', SignupProfileAPI.as_view()),
    path('temp/', TempAPI.as_view()),
]
