from django.contrib import admin
from .models import Categories, Subcategories

admin.site.register([Categories, Subcategories])
