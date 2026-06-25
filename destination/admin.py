from django.contrib import admin
from .models import Destination

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = (
        'destination_name',
        'state',
        'country',
        'best_time_to_visit',
        'estimated_budget'
    )

    search_fields = (
        'destination_name',
        'state',
        'country'
    )

    list_filter = (
        'country',
        'best_time_to_visit'
    )

# Register your models here.
