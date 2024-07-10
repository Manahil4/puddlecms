#changes
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import OrderForm
from django.utils import timezone

from item.models import Item  # Import the Item model from your item app
from django.contrib import messages
from .models import Orders
from django.contrib.auth.decorators import login_required

@login_required
def order_view(request, item_id):
    # item = get_object_or_404(Item, id=item_id)  # Get the item or return a 404 error
    item = Item.objects.get(pk=item_id)  # Fetch the item
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.item = item  # Set the item field of the order
            order.created_at = timezone.now()
            # Ensure created_at is timezone-aware
            order.price = item.price  # Set the price from the item
            order.user = request.user
            order.save()
            messages.success(request, 'Your order has been placed successfully!')
            
            
            return redirect(reverse('core:index'))  # Use reverse here else:
    else:
        form = OrderForm(initial={'price': item.price})
    
    
    context = {
        'item':item,
        'form': form,
    }
    return render(request, 'order/order.html', context)
   
def order(request):
    #return HttpResponse("We offer following services:")
    return render(request, "order/order.html")
