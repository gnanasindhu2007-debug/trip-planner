from django.contrib import admin
from .models import TravelDate

@admin.register(TravelDate)
class TravelDateAdmin(admin.ModelAdmin):
    list_display = (
        'destination',
        'start_date',
        'end_date',
        'number_of_days'
    )

    search_fields = (
        'destination',
    )

    list_filter = (
        'start_date',
        'end_date'
    )

# Register your models here.
