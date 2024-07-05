from django.conf import settings
from django.conf.urls.static import static
# Import the admin module from Django's contrib package, which provides the admin interface.
from django.contrib import admin

# Import the path function from Django's urls module, used to define URL patterns.
from django.urls import path,include

# Import the index and contact view from the core.views module. This view will handle requests to the root URL.
from core.views import index, contact


# Define the URL patterns list. Each entry in the list is a URL pattern that maps a URL to a view.
urlpatterns = [
    
    # This pattern routes requests to the root URL ('') to the index view.
    # Example: http://www.example.com/
    # 'name="index"' names this URL pattern as 'index', allowing it to be referred to by this name elsewhere in the project.
    path('', index, name="index"),

    
    # This pattern routes requests with the 'admin/' URL to the Django admin interface.
    # Example: http://www.example.com/admin/
    path('admin/', admin.site.urls),
    
    # This pattern routes requests to the root URL + contact/ ('contact/') to the contact view.
    # Example: http://www.example.com/contact/
    # 'name="contact"' names this URL pattern as 'contact', allowing it to be referred to by this name elsewhere in the project.
    path('contact/', contact, name = "contact"),
    path('myitems/', include("myitems.urls") ),
    path('item/', include('item.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
