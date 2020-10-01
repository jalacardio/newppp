from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    has_premium = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


