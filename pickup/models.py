from django.db import models


class Pickup(models.Model):
    pickupPlotNo = models.CharField(max_length=300)
    pickupStreet = models.CharField(max_length=300)
    pickupCity = models.CharField(max_length=300)
    pickupState = models.CharField(max_length=300)
    pickupPin = models.IntegerField()
