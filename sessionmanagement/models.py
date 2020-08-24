from django.db import models
from datetime import datetime
from profiles.models import Profile

# Create your models here.


class SessionStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(
        max_length=100, default=None)  # active,inactive, expired
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    profile_id = models.ForeignKey(
        Profile, on_delete=models.CASCADE, default=None)
    login_time = models.DateTimeField(default=datetime.now)
    logout_time = models.DateTimeField(default=datetime.now)
    session_key = models.CharField(max_length=100, default=None)
    login_source = models.CharField(
        max_length=100, default='mobile')  # website/iOS/Android
    # native/google/facebook/linkedIn
    login_type = models.CharField(max_length=100, default='native')
    # logout from all devices/logout from this device
    logout_type = models.CharField(max_length=100, default='current_session')
    last_activity_time = models.DateTimeField(default=datetime.now)
    status = models.ForeignKey(
        SessionStatus, on_delete=models.CASCADE, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.session_id)
