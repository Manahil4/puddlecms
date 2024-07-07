from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from . forms import AddNewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def detail(request,pk):
    item = get_object_or_404(Item, pk=pk)
    related_items= Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    # Debugging statement to confirm item details
    print(f"Displaying item: {item.name}, {item.description}, {item.price}")
    
    return render(request, 'item/detail.html' , {
        'item':item,
        'related_items':related_items})

@login_required
def new(request):
    if request.method =='POST':
        form = AddNewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = AddNewItemForm()
    return render(request, 'item/form.html',{
        'form':form,
        'title':'Add New item'})


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            print(f"Item updated: {item.name}, {item.description}, {item.price}")
            return redirect('item:detail', pk=item.id)
        else:
            # Debugging statement to see form errors
            print(f"Form errors: {form.errors}")
            print(f"Form data: {request.POST}")
    else:
        print('fef')
        form = EditItemForm(instance=item)

    # Debugging statement to check if form is being rendered
    print("Rendering form for editing item:", item.name)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item'
    })

     
        
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('Dashboard:index')