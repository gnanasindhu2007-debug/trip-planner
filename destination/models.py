from django.db import models

class Destination(models.Model):
    destination_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=100)
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.destination_name

# Create your models here.
