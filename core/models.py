from django.db import models
# models.py
from django.contrib.auth.models import User

class DesignerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    previous_work = models.TextField()
    education = models.TextField()
    portfolio_image = models.ImageField(upload_to='puddlecms/item_images', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Create your models here.
