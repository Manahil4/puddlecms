# portfolio/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DesignerProfileForm
from .models import DesignerProfile
from core.models import CustomUser  # Import CustomUser
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

@login_required
def index(request):
    profiles = DesignerProfile.objects.all()
    
    return render(request, 'portfolio/index.html', {'profiles': profiles})

from django.shortcuts import render, redirect

def create_profile(request):
    if request.method == 'POST':
        form = DesignerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Assuming user is authenticated
            profile.save()
            messages.success(request,('Your Profile is Successfully Created, Your Profile looks like this'))
            return redirect('portfolio:profile_view', profile_id=profile.pk)
    else:
        form = DesignerProfileForm()
    
    return render(request, 'portfolio/form.html', {'form': form})

def edit_profile(request, profile_id):
    profile = get_object_or_404(DesignerProfile, pk=profile_id)
    
    if request.method == 'POST':
        form = DesignerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('portfolio:profile_view', profile_id=profile.pk)
    else:
        form = DesignerProfileForm(instance=profile)
    
    return render(request, 'portfolio/form.html', {'form': form})



# def create_profile(request, profile_id):
#     # Check if the user already has a portfolio
#     if DesignerProfile.objects.filter(user=request.user).exists():
#         # Redirect to profile view or any other page since the portfolio already exists
#         return redirect('portfolio:profile_view', profile_id=profile_id)

#     if request.method == 'POST':
#         form = DesignerProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user
#             profile.save()
#             messages.success(request,('Your Profile is Successfully Created, Your Profile looks like this'))
                
#             return redirect('portfolio:profile_view', profile_id=profile.id)
#     else:
#         form = DesignerProfileForm()
    
#     return render(request, 'portfolio/create_profile.html',{'form': form} )

def profile_view(request, profile_id):
    profile = DesignerProfile.objects.get(id=profile_id)
    return render(request, 'portfolio/profile_view.html', {'profile': profile})

def designer_list(request):
    designers = DesignerProfile.objects.all()
    return render(request, 'portfolio/designer_list.html', {'designers': designers})

# def portfolio_form(request):
#     profile = None
#     try:
#         profile = DesignerProfile.objects.get(user=request.user)
#     except DesignerProfile.DoesNotExist:
#         pass
#     if request.method == 'POST':
#         form = DesignerProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user  # Assign the current user
#             profile.save()
#             messages.success(request,('Your Profile/Portfolio is Successfully Created, Now login in your Account'))
                
#             return redirect('core:login')  # Redirect to login after portfolio is saved
#     else:
#         form = DesignerProfileForm(instance=profile)
    
#     return render(request, 'portfolio/form.html', {'form': form})

