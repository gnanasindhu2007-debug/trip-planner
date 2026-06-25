from django.contrib import admin
from .models import GoogleMap

@admin.register(GoogleMap)
class GoogleMapAdmin(admin.ModelAdmin):
    list_display = (
        'place_name',
        'location',
        'latitude',
        'longitude'
    )

    search_fields = (
        'place_name',
        'location'
    )

    list_filter = (
        'location',
    )

# Register your models here.
