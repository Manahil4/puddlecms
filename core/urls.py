from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
app_name='core'
urlpatterns = [
    path("", views.index, name="index"),
    # This pattern routes requests to the root URL + contact/ ('contact/') to the contact view.
    # Example: http://www.example.com/contact/
    # 'name="contact"' names this URL pattern as 'contact', allowing it to be referred to by this name elsewhere in the project.
    path('new/', views.cat, name = "new&cat"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login'),
path('logout/', views.logout_u, name="logout"),
path('profile/create-or-update/', views.create_or_update_profile, name='create_or_update_profile'),
    path('profile/<int:profile_id>/', views.profile_view, name='profile_view'),
    path('designers/', views.home, name='home_profiles'),

    ]

    