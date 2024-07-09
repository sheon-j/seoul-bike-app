from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer

class TodoList(generics.ListCreateAPIView):
  """리스트 view"""
  pagination_class = None
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
  """디테일 view"""
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  lookup_url_kwarg = "id"

