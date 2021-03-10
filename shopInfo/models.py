from django.db import models
import datetime

class ShopInformation(models.Model):
    about_us = models.TextField()
    open_hour_in_week_from = models.TimeField(default=datetime.time(9, 00))
    open_hour_in_week_to = models.TimeField(default=datetime.time(7, 30))
    open_hour_in_saturday_from = models.TimeField(default=datetime.time(9, 00))
    open_hour_in_saturday_to = models.TimeField(default=datetime.time(6, 00))
    open_hour_in_sunday_from = models.TimeField(default=datetime.time(9, 00))
    open_hour_in_sunday_to = models.TimeField(default=datetime.time(5, 00))
    address = models.TextField(blank=False)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.about_us