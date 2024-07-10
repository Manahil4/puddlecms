from django.db import models
from item.models import Item  # Import the Item model from your item app
import datetime
from django.conf import settings
#Adding 
# Create your models here.
class Orders(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order_items')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_who_orders')
    quantity_of_items = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add the price field here
    created_at = models.DateTimeField(default=datetime.datetime.now)
    order_id = models.AutoField(primary_key=True)  # Automatically assigns an ID
    payment_method=models.CharField(max_length=255)
    
    def __str__(self):
        return f"Order {self.pk} by {self.user.username}"