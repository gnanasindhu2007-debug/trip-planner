from django.db import models

class Budget(models.Model):
    destination = models.CharField(max_length=100)
    transportation = models.DecimalField(max_digits=10, decimal_places=2)
    accommodation = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    activities = models.DecimalField(max_digits=10, decimal_places=2)
    shopping = models.DecimalField(max_digits=10, decimal_places=2)
    others = models.DecimalField(max_digits=10, decimal_places=2)

    def total_budget(self):
        return (
            self.transportation +
            self.accommodation +
            self.food +
            self.activities +
            self.shopping +
            self.others
        )

    def __str__(self):
        return self.destination

# Create your models here.
