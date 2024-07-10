from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_designer = models.BooleanField(default=False)

    def __str__(self):
        return self.username