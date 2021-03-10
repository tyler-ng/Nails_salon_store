from django.contrib import admin
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_per_page = 25

admin.site.register(Gallery, GalleryAdmin)