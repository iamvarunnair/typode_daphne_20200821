from django.db import models
from profiles.models import Profile

# Create your models here.


class ChatRequestStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(
        max_length=100, default=None)  # Sent, Accepted, Rejected, Withdrawn

    def __str__(self):
        return str(self.status_id)


class ChatRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    requester_id = models.ForeignKey(
        Profile, on_delete=models.CASCADE, default=None, related_name='requester_id')
    respondent_id = models.ForeignKey(
        Profile, on_delete=models.CASCADE, default=None, related_name='respondent_id')
    status = models.ForeignKey(
        ChatRequestStatus, on_delete=models.CASCADE, default=None)
