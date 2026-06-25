from django.contrib import admin
from .models import UserRegistration

@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'username'
    )

    search_fields = (
        'full_name',
        'email',
        'username'
    )

# Register your models here.
