from django.contrib import admin
from .models import Dashboard

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = (
        'trip_name',
        'destination',
        'start_date',
        'end_date',
        'budget'
    )

    search_fields = (
        'trip_name',
        'destination'
    )

    list_filter = (
        'start_date',
        'end_date'
    )

# Register your models here.
