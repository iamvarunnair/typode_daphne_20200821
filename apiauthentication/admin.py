from django.contrib import admin
from .models import TokenStatus, TokenType, ApiTokens
# Register your models here.


admin.site.register(TokenStatus)
admin.site.register(TokenType)
admin.site.register(ApiTokens)
