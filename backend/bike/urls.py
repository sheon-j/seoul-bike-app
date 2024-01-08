from django.urls import path
from .views import BikeList, BikeDetail

'''
특정 path에 view를 매핑합니다.
'''
urlpatterns = [
    path(
        route='bike/',           # 연결할 path
        view=BikeList.as_view(), # 연결할 view
        name='bike_list'         # 명칭 정의
    ),
    path(route='bike/<int:id>/', view=BikeDetail.as_view(), name='bike_detail'),
]