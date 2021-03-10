from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "refill", "full", "is_public" ,"subcategory")
    search_fields = ("name", "subcategory__name",)
    list_filter = ("name", "subcategory",)
    list_page = 25

admin.site.register(Service, ServiceAdmin)