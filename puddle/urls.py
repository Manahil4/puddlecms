from django.conf import settings
from django.conf.urls.static import static
# Import the admin module from Django's contrib package, which provides the admin interface.
from django.contrib import admin

# Import the path function from Django's urls module, used to define URL patterns.
from django.urls import path,include

# Define the URL patterns list. Each entry in the list is a URL pattern that maps a URL to a view.
urlpatterns = [
    
    # This pattern routes requests to the root URL ('') to the index view.
    # Example: http://www.example.com/
    # 'name="index"' names this URL pattern as 'index', allowing it to be referred to by this name elsewhere in the project.
    path('', include('core.urls')),

    
    # This pattern routes requests with the 'admin/' URL to the Django admin interface.
    # Example: http://www.example.com/admin/
    path('admin/', admin.site.urls),
    path('Dashboard/', include('Dashboard.urls')),
    path('item/', include('item.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
