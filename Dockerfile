FROM python:3
ENV PYTHONUNBUFFERED=0
RUN apt-get update && apt-get -y install libpq-dev

COPY ./requirements.txt /app/requirements.txt
RUN    pip install -r /app/requirements.txt

WORKDIR /app

COPY . /app

CMD [ "./entry_point.sh" ]