
from . import views
from django.urls import path

app_name = 'order'

# Create your views here.
urlpatterns = [
    path('<int:item_id>/order', views.order_view, name='order_view'),
   
]
    