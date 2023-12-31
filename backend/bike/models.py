from django.db import models

class Bike(models.Model):
  rental_date = models.DateField()
  rental_time = models.IntegerField()
  place_code = models.IntegerField()
  place_name = models.CharField(max_length=100)
  rental_category = models.CharField(max_length=10)
  gender = models.CharField(max_length=10)
  age = models.CharField(max_length=10)
  count = models.IntegerField()
  exercise = models.FloatField()
  carbon = models.FloatField()
  travel_distance = models.IntegerField()
  travel_time = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  