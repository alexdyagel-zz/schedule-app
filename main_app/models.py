import datetime

from django.db import models


class Flight(models.Model):
    departure_date = models.DateField(default=datetime.date.today)
    departure_time = models.TimeField()
    destination = models.CharField(max_length=25)
    departure_railway = models.CharField(max_length=25)
    departure_platform = models.IntegerField()
    destination_railway = models.CharField(max_length=25)
    price_of_ticket = models.FloatField()

    class Meta:
        abstract = True


class BusFlight(Flight):
    route_number = models.IntegerField()
    bus_brand = models.CharField(max_length=25)
    travel_time = models.DurationField()


class TrainFlight(Flight):
    train_number = models.IntegerField()
    destination_date = models.DateField()
    destination_time = models.TimeField()
