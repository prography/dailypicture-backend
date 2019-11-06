FROM python:3.7

ENV PYTHONUNBUFFERED=0

RUN apt-get update && apt-get -y install libpq-dev
RUN apt-get -y install postgresql-client

COPY ./requirements.txt /app/requirements.txt
RUN    pip install -r /app/requirements.txt

WORKDIR /app

COPY . /app