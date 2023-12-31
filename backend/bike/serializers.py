from rest_framework import serializers
from .models import Bike

class BikeSerializer(serializers.ModelSerializer):
  rental_date = serializers.DateField(format='%Y.%m.%d')
  gender = serializers.SerializerMethodField()
  travel_distance = serializers.SerializerMethodField()
  travel_time = serializers.SerializerMethodField()

  class Meta:
    model = Bike
    exclude = ("id", "created_at", "updated_at")
    read_only_fields = ("id", "created_at", "updated_at")

  def get_gender(self, obj):
    gender_mapper = {'F': '여', 'M': '남'}
    return gender_mapper.get(obj.gender)
  
  def get_travel_distance(self, obj):
    travel_distance = obj.travel_distance
    if travel_distance > 1000:
      return f'{(travel_distance/1000):.2f}km'
    return f'{travel_distance}m'
      
  def get_travel_time(self, obj):
    travel_time = obj.travel_time
    if travel_time > 60:
      return f'{travel_time//60}시간 {travel_time%60}분'
    return f'{travel_time}분'