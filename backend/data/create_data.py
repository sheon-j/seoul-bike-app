import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from datetime import datetime
from time import time
import pandas as pd
from bike.models import Bike

def main():
  start_time = time()
  path = 'data/seoul-bike.csv'
  df = pd.read_csv(path)
  df_cnt = len(df)
  # create data
  for index, row in df.iterrows():
    # date parsing
    rental_date = datetime.strptime(row['rental_date'], '%Y-%m-%d').date()
    # get or create
    obj, created = Bike.objects.get_or_create(
      id=index,
      rental_date=rental_date,
      rental_time=row['rental_time'],
      place_code=row['place_code'],
      place_name=row['place_name'],
      rental_category=row['rental_category'],
      gender=row['gender'],
      age=row['age'],
      count=row['count'],
      exercise=row['exercise'],
      carbon=row['carbon'],
      travel_distance=row['travel_distance'],
      travel_time=row['travel_time'],
    )
    # pass
    if not created:
      print(f'Object with id {index} already exists. Skipping.')
    # done
    else:
      print(f'\r{index}/{df_cnt} created', end='')
  
  end_time = time()
  print(f'\ndata created! ({(end_time-start_time):.2f}s)')


if __name__ == '__main__':
  main()
