from django.contrib import admin
from .models import TripPlan

@admin.register(TripPlan)
class TripPlanAdmin(admin.ModelAdmin):
    list_display = (
        'trip_name',
        'destination',
        'travel_date',
        'return_date',
        'budget',
        'activity'
    )

    search_fields = (
        'trip_name',
        'destination',
        'activity'
    )

    list_filter = (
        'destination',
        'travel_date',
        'return_date'
    )
# Register your models here.
