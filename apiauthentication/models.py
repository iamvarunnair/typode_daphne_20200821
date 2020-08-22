from django.db import models

# Create your models here.


class TokenStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    # Active, Inactive, Pending Activation, Suspended
    status_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.status_id)


class TokenType(models.Model):
    type_id = models.AutoField(primary_key=True)
    # Website, Mobile App, Api Client
    type_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.type_id)


class ApiTokens(models.Model):
    token_id = models.AutoField(primary_key=True)
    token_string = models.CharField(max_length=100, default="")
    token_type = models.ForeignKey(
        TokenType, on_delete=models.CASCADE, default=None)
    status = models.ForeignKey(
        TokenStatus, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.token_id)
