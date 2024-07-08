from django.urls import path

from .views import TodoList, TodoDetail

urlpatterns = [
    path(route='todo/', view=TodoList.as_view(), name='todo_list'),
    path(route='todo/<int:id>/', view=TodoDetail.as_view(), name='todo_detail'),
]
