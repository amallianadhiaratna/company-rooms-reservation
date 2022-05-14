FROM ubuntu:bionic
ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y netcat \
    mysql-client \
    libmysqlclient-dev \
    python3 \
    python3-pip

# RUN python3 pip install -r requirements.txt

# FROM python:3.8.5-alpine
# ENV PYTHONUNBUFFERED 1

# COPY . /app
# WORKDIR /app

# # RUN apk add --no-cache mariadb-connector-c-dev
# # RUN apk update && apk add python3 python3-dev mariadb-dev build-base \
# #     && pip3 install mysqlclient \
# #     && apk del python3-dev mariadb-dev build-base 

# RUN apk add netcat-openbsd
# RUN python -m pip install --upgrade pip
# RUN pip --default-timeout=600 install -r requirements.txt