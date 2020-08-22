from django.db import models
from datetime import datetime

# Create your models here.


class ProfileStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(
        max_length=100, default=None)  # active,inactive
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.status_id)


class Avatar(models.Model):
    avatar_id = models.AutoField(primary_key=True)
    avatar_name = models.CharField(
        max_length=100, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.avatar_id)


class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=14)
    avatar_id = models.ForeignKey(
        Avatar, on_delete=models.CASCADE, default=None)
    status = models.ForeignKey(
        ProfileStatus, on_delete=models.CASCADE, default=None)
    added_date = models.DateTimeField(default=datetime.now)
    last_modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.user_id)
