# Python 이미지 기반 선택 (예: Python 3.8)
FROM python:3.8.13-slim-bullseye

# 패키지 설치
RUN apt-get update \
    && apt-get install -y --no-install-recommends git vim lsof curl\
    && curl -sL https://deb.nodesource.com/setup_16.x | bash -E - \
    && apt-get install -y nodejs \
    && npm install -g yarn \
    && git config --global url."https://github.com/".insteadOf git://github.com/ \
    && mkdir -p /app/seoul-bike-app \
    && apt-get clean

# 앱 소스 코드를 복사
COPY . /app/seoul-bike-app

# 볼륨 설정
VOLUME /app/seoul-bike-app

# 작업 디렉토리 설정
WORKDIR /app