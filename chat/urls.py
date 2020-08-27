from django.urls import path
from .api.sendchatrequest.views_sendchatrequest import SendChatRequestAPI


chaturlpatterns = [
    path('send_chat_request/', SendChatRequestAPI.as_view()),
]
