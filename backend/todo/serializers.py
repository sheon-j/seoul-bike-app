from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'is_checked', 'username', 'text', 'created_date',)
    read_only_fields = ("id", "created_date", "updated_date")