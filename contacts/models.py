from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)