from django.contrib import admin

from .models import Bike


class BikeAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'rental_date', 'rental_time', 'exercise')
    ordering = ('rental_date', 'rental_time')
    search_fields = ('place_name',)

admin.site.register(Bike, BikeAdmin)
