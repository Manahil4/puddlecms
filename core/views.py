from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
# views.py
from django.contrib.auth.decorators import login_required

from .forms import DesignerProfileForm
from .models import DesignerProfile

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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    else:
        
        form = SignupForm()
    return render(request, 'core/signup.html',{
        'form': form})
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

@login_required
def create_or_update_profile(request):
    try:
        profile = DesignerProfile.objects.get(user=request.user)
    except DesignerProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = DesignerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_view', profile_id=profile.id)
    else:
        form = DesignerProfileForm(instance=profile)
    
    return render(request, 'core/create_or_update_profile.html', {'form': form})

def profile_view(request, profile_id):
    profile = DesignerProfile.objects.get(id=profile_id)
    return render(request, 'core/profile_view.html', {'profile': profile})

def home(request):
    profiles = DesignerProfile.objects.all()
    return render(request, 'core/home_profiles.html', {'profiles': profiles})

