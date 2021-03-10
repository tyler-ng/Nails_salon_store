from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import datetime, date

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    date = models.DateField(default=date.today)
    time = models.TimeField(default=datetime.now)
    message = models.TextField(blank=True)
    services = ArrayField(ArrayField(models.CharField(max_length=100)))

    def __str__(self):
        return self.name