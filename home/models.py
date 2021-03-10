from django.db import models


class BannerSlider(models.Model):
    photo = models.ImageField(upload_to='photos/banner_slider/%Y/%m/%d', blank=False)
    title = models.TextField()
    content = models.TextField()
    promotion_description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    content = models.TextField()
    photo_1 = models.ImageField(upload_to='photos/why_choose_us/%Y/%m/%d', blank=False)
    photo_2 = models.ImageField(upload_to='photos/why_choose_us/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.content


class ServiceImage(models.Model):
    photo = models.ImageField(upload_to='photos/services_banner/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.photo.url


class Testimonials(models.Model):
    message = models.TextField()
    client_name = models.CharField(max_length=100)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name


class SpecialPrice(models.Model):
    name = models.CharField(max_length=100)
    time_estimation = models.TextField()
    price = models.IntegerField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name