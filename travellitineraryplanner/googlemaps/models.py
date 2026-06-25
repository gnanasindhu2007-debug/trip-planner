from django.db import models

class GoogleMap(models.Model):
    place_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.place_name

# Create your models here.
