from django.db import models
from categories.models import Subcategories

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True, null=True)
    full =  models.IntegerField(blank=True, null=True)
    refill = models.IntegerField(blank=True, null=True)
    time_estimation = models.CharField(max_length=200, blank=True)
    description = models.TextField( blank=True)
    is_public = models.BooleanField(default=True)
    subcategory = models.ForeignKey(Subcategories, related_name='services', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
