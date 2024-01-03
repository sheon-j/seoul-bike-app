# :bicyclist: 서울시 공공자전거 이용정보 실습

![](https://blog.kakaocdn.net/dn/32N09/btqwOA4U9in/uNZIaP2L8af84EnJS6KxF1/img.png)

## 데이터 출처

- [서울 열린데이터 광장 - 서울시 공공자전거 이용정보(시간대별)](http://data.seoul.go.kr/dataList/OA-15245/F/1/datasetView.do#)
- 서울특별시 공공자전거 이용정보(시간대별)_2017년.zip
  (2017-01-01~2017-01-11 데이터를 2024년으로 전처리 하였습니다. 교육용으로 참고하시면 감사하겠습니다.)



## Backend 실행

- api를 위한 django 앱 폴더입니다.
- 사용된 db는 sqlite 입니다.

```shell
# backend 프로젝트 폴더로 이동합니다.
cd backend

# 패키지를 설치합니다.
pip install -r requirements.txt

# django 구동을 위한 최초 DB 설정을 합니다.
python manage.py migrate

# 최초계정 supseruser을 만듭니다.
python manage.py createsuperuser
> Username: admin
> Email address: [Enter]
> Password: 1234
> Password (again): 1234
> Bypass password validation and create user anyway? [y/N]: y

# db에 샘플데이터를 생성합니다.
python -m data.create_data
```



## Frontend 실행

- 새로운 터미널을 엽니다.
- 화면 개발을 위한 프론트서버를 실행합니다.

```shell
# frontend 프로젝트 서버로 이동합니다.
cd frontend

# 패키지를 설치합니다.
yarn

# 서버를 실행합니다.
yarn dev
```

