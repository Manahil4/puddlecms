from django.shortcuts import render
from item.models import Item, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Exists, OuterRef

@login_required
def index(request):
    # Filter items created by the logged-in user
    item_list = Item.objects.filter(created_by=request.user)
    
    # Subquery to check if an item exists in the category created by the user
    items_exist = Item.objects.filter(category=OuterRef('pk'), created_by=request.user)

    # Filter categories where items created by the user exist
    category_list = Category.objects.annotate(
        has_items=Exists(items_exist)  # Annotate each category with a boolean indicating if it has items created by the user
    ).filter(has_items=True)  # Filter to include only categories with items created by the user

    # Paginator for items, showing 6 items per page
    paginator = Paginator(item_list, 6)
    page_number = request.GET.get('page')  # Get the current page number from the request
    page_obj = paginator.get_page(page_number)  # Get the items for the current page
    
    context = {
        'items': page_obj,  # Paginated items
        'categories': category_list,  # Filtered categories
    }
    
    # Render the template with the context data
    return render(request, 'Dashboard/index.html', context)
