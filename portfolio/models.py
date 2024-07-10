from django.db import models
# models.py
from django.conf import settings
#from core.models import CustomUser  # Import the CustomUser model

class DesignerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()
    previous_work = models.TextField()
    education = models.TextField()
    experience = models.CharField(max_length=255)
    specialization=models.CharField(max_length=255)
    portfolio_image = models.ImageField(upload_to='item_images', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Create your models here.
