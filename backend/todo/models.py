from django.db import models

class Todo(models.Model):
  '''
  Bike 테이블 필드에 타입을 지정하여 
  ORM이 정상 수행될 수 있도록 합니다.
  '''
  text = models.TextField()
  is_checked = models.BooleanField(default=False)
  username = models.CharField(max_length=50, default='개발용')
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  