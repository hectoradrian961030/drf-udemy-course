from django.db import models

# Create your models here.

class Passenger(models.Model):

    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)
    travelPoints = models.CharField(max_length=256)

    def __str__(self):
        return self.firstName + " " + self.lastName