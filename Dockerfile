FROM python:3.7

##########################################################
# set timezone
##########################################################
ENV TZ="/usr/share/zoneinfo/Asia/Seoul"
ENV PYTHONUNBUFFERED 0

RUN apt-get update && apt-get -y install libpq-dev
RUN apt-get -y install postgresql-client

ARG PROJECT_DIR="/app"

##########################################################
# install dependencies via pip
##########################################################
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

##########################################################
# set working directory
##########################################################
WORKDIR ${PROJECT_DIR}

##########################################################
# add proejct files
##########################################################
COPY . $PROJECT_DIR

##########################################################
# expose port for single container(Elastic Beanstalk)
##########################################################
EXPOSE 8000

##########################################################
# command
##########################################################
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
