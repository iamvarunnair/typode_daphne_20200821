from django.contrib import admin
from .models import ProfileStatus, Profile, Avatar
# Register your models here.

admin.site.register(ProfileStatus)
admin.site.register(Profile)
admin.site.register(Avatar)
