from django.db import models

class About(models.Model):
    title = models.TextField(blank=False)
    content = models.TextField(blank=False)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title