from django.contrib import admin
from .models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'subtitle'
    )

    search_fields = (
        'title',
        'subtitle'
    )

# Register your models here.
