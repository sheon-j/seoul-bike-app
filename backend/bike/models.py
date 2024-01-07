from django.db import models

class Bike(models.Model):
  '''
  Bike 테이블 필드에 타입을 지정하여 
  ORM이 정상 수행될 수 있도록 합니다.
  '''
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
  