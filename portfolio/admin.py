from django.contrib import admin
from .models import DesignerProfile

@admin.register(DesignerProfile)
class DesignerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'previous_work', 'education', 'experience', 'specialization']  # Display these fields in the admin list
    search_fields = ['user__username', 'bio']  # Add fields for searching in the admin
    list_filter = ['user__is_active']  # Add filters for the admin

    # Customize form fields or behaviors if needed
    # form = DesignerProfileForm

    # Optionally customize fields for adding or editing in the admin
    # fields = ['user', 'bio', 'previous_work', 'education', 'current_items']

    # Optionally customize readonly fields
    # readonly_fields = ['user']
