from django.db.models import QuerySet
from rest_framework import serializers

from .models import Bike


class BikeSerializer(serializers.ModelSerializer):
  """
  Frontend와 Backend의 api 요청과 응답을 위해
  데이터 타입을 Model <-> json으로 직렬화 또는 역직렬화를 수행합니다.
  """
  # 직접 데이터를 파싱할 수 있습니다.
  rental_date = serializers.DateField(format="%Y.%m.%d")
  gender = serializers.SerializerMethodField()
  travel_distance = serializers.SerializerMethodField()
  travel_time = serializers.SerializerMethodField()
  rental_time = serializers.SerializerMethodField()

  class Meta:
    # 시리얼라이저에 메타 속성을 정의합니다. 
    model = Bike
    exclude = ("created_at", "updated_at")
    read_only_fields = ("id", "created_at", "updated_at")

  def get_gender(self, obj): 
    """F -> 여, M -> 남"""
    gender_mapper = {"F": "여", "M": "남"}
    return gender_mapper.get(obj.gender)
  
  def get_travel_distance(self, obj):
    """이동거리 미터 단위 표현"""
    travel_distance = obj.travel_distance
    if travel_distance > 1000:
      return f"{(travel_distance/1000):.2f}km"
    return f"{travel_distance}m"
      
  def get_travel_time(self, obj):
    """이동시간 시간/분 표현"""
    travel_time = obj.travel_time
    if travel_time > 60:
      return f"{travel_time//60}시간 {travel_time%60}분"
    return f"{travel_time}분"
  
  def get_rental_time(self, obj):
    """렌탈한 시간 변환"""
    rental_time = obj.rental_time
    if rental_time == 0:
      return f"오전 12시"
    elif rental_time >= 12:
      return f"오후 {rental_time-12}시"
    else:
      return f"오전 {rental_time}시"