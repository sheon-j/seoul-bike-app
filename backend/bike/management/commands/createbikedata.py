from tqdm import tqdm
from faker import Faker
import pandas as pd

from django.core.management import BaseCommand

from bike.models import Bike

fake = Faker()
path = "data/example.csv"
df = pd.read_csv(path)


class Command(BaseCommand):
  """샘플 데이터 생성"""

  def handle(self, *args, **options):
    qs = Bike.objects.all()
    if len(qs) >= 10000:
      raise ValueError("이미 샘플 데이터가 생성되었습니다.")
    
    for _, row in tqdm(df.iterrows(), desc="데이터 생성", total=len(df)):
      rental_date = fake.date_this_year()
      obj, created = Bike.objects.get_or_create(
        rental_date=rental_date,
        rental_time=row["rental_time"],
        place_code=row["place_code"],
        place_name=row["place_name"],
        rental_category=row["rental_category"],
        gender=row["gender"],
        age=row["age"],
        count=row["count"],
        exercise=row["exercise"],
        carbon=row["carbon"],
        travel_distance=row["travel_distance"],
        travel_time=row["travel_time"],
      )
