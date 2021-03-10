from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/category/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.name

class Subcategories(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/services/%Y/%m/%d', blank=False)
    category = models.ForeignKey(Categories, related_name='subcategories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name