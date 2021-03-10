from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone',)
    list_display_links = ('first_name',)
    list_filter = ('email', 'phone')
    search_fields = ('email', 'phone')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)