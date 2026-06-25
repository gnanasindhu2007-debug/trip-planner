from django.contrib import admin
from .models import Itinerary

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = (
        'trip_name',
        'destination',
        'travel_date',
        'activity'
    )

    search_fields = (
        'trip_name',
        'destination',
        'activity'
    )

    list_filter = (
        'travel_date',
        'destination'
    )

# Register your models here.
