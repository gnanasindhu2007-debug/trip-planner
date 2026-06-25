from django.db import models

class Activity(models.Model):
    activity_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.activity_name
# Create your models here.
