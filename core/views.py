from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
# views.py

# Create your views here.
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
    return render(request, 'core/index.html', context)
def contact(request):
    return render(request, 'core/contact.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
        
#         if form.is_valid():
#             form.save()
            
#             return redirect('/login/')
        
#     else:
        
#         form = SignupForm()
#     return render(request, 'core/signup.html',{
#         'form': form})
# def login_u(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password= request.POST['password']
#         user=authenticate(request, username=username, password=password)
#         if user is not None:
#             form= login(request, user)
#             return redirect('/index/')
#         else:
#             messages.success(request,("There was an error loggin"))
#             return redirect('/login/')
        
#     else:
#         return render(request,'core/login.html',{
#             'form': form})
def logout_u(request):
    logout(request)
    messages.success(request,("You were LOGOUT!!!"))
    return redirect('core:index')
def cat(request):
    item_list = Item.objects.all()
    category_list = Category.objects.all()
    paginator = Paginator(item_list, 6)  # Show 6 items per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'items': page_obj,
        'categories': category_list,
    }
    return render(request, 'core/new&cat.html', context)



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.set_password(form.cleaned_data['password'])
            user.save()
            
            if user.is_designer:
                return redirect("{%'url 'portfolio:portfolio_form'%}")
            else:
                return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})

