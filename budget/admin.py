from django.contrib import admin
from .models import Budget

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        'destination',
        'transportation',
        'accommodation',
        'food',
        'activities',
        'shopping',
        'others'
    )

    search_fields = ('destination',)

# Register your models here.
