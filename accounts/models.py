from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=False, blank=False)
