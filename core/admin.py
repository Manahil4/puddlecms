from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Contact

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_designer']  # Customize display fields

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'is_designer')}),  # Include is_designer field
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact)
# Register your models here.
