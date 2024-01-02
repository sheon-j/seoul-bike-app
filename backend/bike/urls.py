from django.urls import path
from .views import BikeList, BikeDetail

urlpatterns = [
    path(route='bike/', view=BikeList.as_view(), name='bike_list'),
    path(route='bike/<int:id>', view=BikeDetail.as_view(), name='bike_detail'),
]