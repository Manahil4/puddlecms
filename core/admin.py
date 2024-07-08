from django.contrib import admin
# core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Role',
            {
                'fields': (
                    'is_designer',
                ),
            },
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
