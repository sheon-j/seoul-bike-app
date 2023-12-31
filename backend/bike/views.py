from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.response import Response

from .models import Bike
from .serializers import BikeSerializer


class BikeList(generics.ListCreateAPIView):
    serializer_class = BikeSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('rental_date', 'rental_time', 'updated_at')
    ordering = ('-rental_date', '-rental_time',)
    search_fields = ('place_name', 'rental_category')
    model = Bike
    queryset = Bike.objects.all()
    filterset_fields = ['rental_date', 'rental_time', 'place_code', 'rental_category', 'place_name',]

    def delete(self, request, *args, **kwargs):
        queryset = self.model.all()
        delete_ids = request.data['ids']
        if delete_ids:
            queryset.filter(pk__in=delete_ids).delete()
        else:
            queryset.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    lookup_url_kwarg = 'id'
