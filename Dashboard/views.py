from django.shortcuts import render, get_object_or_404
from item.models import Item, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

@login_required
def index(request):
    item_list = Item.objects.all()
    category_list = Category.objects.all()
    paginator = Paginator(item_list, 6)  # Show 6 items per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'items': page_obj,
        'categories': category_list,
    }
    return render(request, 'Dashboard/index.html', context)
