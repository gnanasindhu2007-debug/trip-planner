from django.contrib import admin
from .models import Weather

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = (
        'destination',
        'temperature',
        'weather_condition',
        'humidity',
        'wind_speed',
        'weather_date'
    )

    search_fields = (
        'destination',
        'weather_condition'
    )

    list_filter = (
        'weather_condition',
        'weather_date'
    )

# Register your models here.
