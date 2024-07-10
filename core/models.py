from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime

class CustomUser(AbstractUser):
    is_designer = models.BooleanField(default=False)

    def __str__(self):
        return self.username
 
class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', on_delete = models.CASCADE)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)


    def _str_(self):
        return f"{self.user}"   