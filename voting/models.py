from django.contrib.auth.models import AbstractUser
from django.db import models

class Voter(AbstractUser):
    # Add your custom fields if needed
    has_voted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Voter"
        verbose_name_plural = "Voters"
