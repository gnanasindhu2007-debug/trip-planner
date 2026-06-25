from django.db import models

class Weather(models.Model):
    destination = models.CharField(max_length=100)
    temperature = models.FloatField()
    weather_condition = models.CharField(max_length=100)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    weather_date = models.DateField()

    def __str__(self):
        return self.destination

# Create your models here.
