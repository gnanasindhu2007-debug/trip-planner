from django.db import models

class TripPlan(models.Model):
    trip_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travel_date = models.DateField()
    return_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    activity = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.trip_name

# Create your models here.
