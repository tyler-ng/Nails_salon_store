from django.contrib import admin
from .models import BannerSlider, WhyChooseUs, ServiceImage, Testimonials, SpecialPrice

class BannerSliderAdmin(admin.ModelAdmin):
    list_display = ("title", "promotion_description", "is_public")

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ("client_name", "is_public")

class SpecialPriceAdmin(admin.ModelAdmin):
    list_display = ("name", "time_estimation", "price", "is_public")

admin.site.register(Testimonials, TestimonialsAdmin)

admin.site.register(BannerSlider, BannerSliderAdmin)

admin.site.register(SpecialPrice, SpecialPriceAdmin)

admin.site.register(WhyChooseUs)

admin.site.register(ServiceImage)
