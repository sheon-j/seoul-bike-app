from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from .serializers import BikeSerializer, BikeChartSerializer


class BikeList(generics.ListAPIView):
    '''Bike 리스트 View(서비스 로직)'''
    queryset = BikeSerializer.get_optimized_queryset()
    serializer_class = BikeSerializer
    filter_backends = (
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter,
    )
    ordering_fields = (
        'rental_date',
        'rental_time', 
        'travel_time', 
        'travel_distance', 
        'exercise', 
        'carbon', 
        'count',
    )
    ordering = (
        '-rental_date', 
        '-rental_time',
    )
    search_fields = ('place_name',)
    filterset_fields = {
        'rental_date': ['exact', 'lte', 'gte'], 
        'rental_time': ['exact', 'lt', 'gte'],
        'mark': ['exact'],
        'gender': ['exact'],
        'age': ['exact', 'contains'],
        'rental_category': ['contains'],
        'exercise': ['exact', 'lt', 'gte'],
        'carbon': ['exact', 'lt', 'gte'],
        'travel_distance': ['exact', 'lt', 'gte'],
        'travel_time': ['exact', 'lt', 'gte'],
    }

from rest_framework.response import Response

class BikeChart(BikeList):
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = BikeChartSerializer(queryset)
        data = serializer.data.values()
        return Response(data=data)

class BikeDetail(generics.RetrieveUpdateAPIView):
    '''Bike 디테일 View'''
    queryset = BikeSerializer.get_optimized_queryset()
    serializer_class = BikeSerializer
    lookup_url_kwarg = 'id'
