from django.urls import path
from . import views
app_name='portfolio'
urlpatterns = [
    path("",views.index ,name="index"),
    path('proflie/designerlist', views.designer_list, name='designer_list'),
    path('profile/<int:profile_id>/', views.profile_view, name='profile_view'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/<int:profile_id>/edit/', views.edit_profile, name='edit_profile'),
    # Other URLs as needed
]
    