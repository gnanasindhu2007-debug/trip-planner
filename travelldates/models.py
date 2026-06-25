from django.db import models

class TravelDate(models.Model):
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_days = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.destination} ({self.start_date} - {self.end_date})"

# Create your models here.
