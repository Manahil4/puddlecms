from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm,LoginForm
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request, 'core/index.html', {
        'categories':categories,
        'items':items,})
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
    items = Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request, 'core/new&cat.html', {
        'categories':categories,
        'items':items,})