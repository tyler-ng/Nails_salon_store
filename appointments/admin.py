from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'services', 'date', 'time')
    list_filter = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 25

admin.site.register(Appointment, AppointmentAdmin)
