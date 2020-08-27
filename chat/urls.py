from django.urls import path
from .api.sendchatrequest.views_sendchatrequest import SendChatRequestAPI
from .api.respondtochatrequest.views_respondtochatrequest import RespondToChatRequestAPI
from .api.withdrawchatrequest.views_withdrawchatrequest import WithdrawChatRequestAPI
from .api.removechatcontact.views_removechatcontact import RemoveChatContactAPI


chaturlpatterns = [
    path('send_chat_request/', SendChatRequestAPI.as_view()),
    path('respond_to_chat_request/', RespondToChatRequestAPI.as_view()),
    path('withdraw_chat_request/', WithdrawChatRequestAPI.as_view()),
    path('remove_chat_contact/', RemoveChatContactAPI.as_view()),
]
