from django.contrib import admin

from .models import Bike


class BikeAdmin(admin.ModelAdmin):
    '''
    admin 페이지에 표현 방식을 정의합니다.
    '''
    list_display = ('place_name', 'rental_date', 'rental_time', 'exercise')
    ordering = ('rental_date', 'rental_time')
    search_fields = ('place_name',)

admin.site.register(Bike, BikeAdmin)
