from django.db import models

class Gallery(models.Model):
    type = models.CharField(max_length=100)
    photo_original = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.type