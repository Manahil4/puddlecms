# portfolio/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DesignerProfileForm
from .models import DesignerProfile
from core.models import CustomUser  # Import CustomUser

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
    
    return render(request, 'create_or_update_profile.html', {'form': form})

def profile_view(request, profile_id):
    profile = DesignerProfile.objects.get(id=profile_id)
    return render(request, 'profile_view.html', {'profile': profile})

def designer_list(request):
    designers = DesignerProfile.objects.all()
    return render(request, 'designer_list.html', {'designers': designers})

def portfolio_form(request):
    if request.method == 'POST':
        form = DesignerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Assign the current user
            profile.save()
            return redirect('/login/')  # Redirect to login after portfolio is saved
    else:
        form = DesignerProfileForm()
    
    return render(request, 'portfolio/form.html', {'form': form})

