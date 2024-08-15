from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Customize the list display, add fields as necessary
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
