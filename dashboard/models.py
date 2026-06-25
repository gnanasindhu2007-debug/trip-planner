from django.db import models

class Dashboard(models.Model):
    trip_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.trip_name

# Create your models here.
