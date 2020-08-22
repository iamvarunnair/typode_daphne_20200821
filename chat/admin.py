from django.contrib import admin
from .models import ChatRequest, ChatRequestStatus
# Register your models here.
admin.site.register(ChatRequestStatus)
admin.site.register(ChatRequest)
