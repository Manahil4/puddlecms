from django.urls import path
from . import views
app_name='portfolio'
urlpatterns = [
    # This pattern routes requests to the root URL + contact/ ('contact/') to the contact view.
    # Example: http://www.example.com/contact/
    # 'name="contact"' names this URL pattern as 'contact', allowing it to be referred to by this name elsewhere in the project.
    path('profile/create/', views.create_profile, name='create_profile'),
    path('<int:profile_id>/profile', views.profile_view, name='profile_view'),
    path('designers/', views.designer_list, name='designer_list'),
    path('portfolioform/', views.portfolio_form, name=" portfolio_form"),
    ]

    