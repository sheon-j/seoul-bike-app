from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.response import Response

from .models import Bike
from .serializers import BikeSerializer


class BikeList(generics.ListCreateAPIView):
    '''
    Bike 리스트 View(서비스 로직)
    '''
    model = Bike                       # 모델 등록
    queryset = Bike.objects.all()      # 기본 쿼리셋
    serializer_class = BikeSerializer  # 시리얼라이저 등록
    filter_backends = (                # 필터 클래스 등록
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    )
    ordering_fields = (                # 소팅 대상 필드 등록
        'rental_date',
        'rental_time', 
        'travel_time', 
        'travel_distance', 
        'exercise', 
        'carbon', 
    )
    ordering = (                       # 기본 정렬 필드 등록
        '-rental_date', 
        '-rental_time',
    )
    search_fields = ('place_name',)    # 검색 대상 필드 등록
    filterset_fields = {               # 필터링 필드, 방식 등록
        'rental_date': ['exact', 'lte', 'gte'], 
        'rental_time': ['exact', 'lt', 'gte'],
        'gender': ['exact'],
        'age': ['contains'],
        'rental_category': ['contains'],
        'exercise': ['exact', 'lt', 'gte'],
        'carbon': ['exact', 'lt', 'gte'],
        'travel_distance': ['exact', 'lt', 'gte'],
        'travel_time': ['exact', 'lt', 'gte'],
    }

    def delete(self, request, *args, **kwargs):
        '''
        특정 요청 메소드를 정의 할 수 있습니다.
        '''
        queryset = self.model.all()
        delete_ids = request.data['ids']
        if delete_ids:
            queryset.filter(pk__in=delete_ids).delete()
        else:
            queryset.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BikeDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Bike 디테일 View
    '''
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    lookup_url_kwarg = 'id'
