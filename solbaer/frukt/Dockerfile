FROM python:3.11.0-alpine3.17
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /requirements.txt
RUN mkdir minor_swing
ADD . /minor_swing/
WORKDIR /minor_swing/
RUN pip install --upgrade pip && pip install -r /requirements.txt
ENV PORT=8080
#EXPOSE 8888
#CMD python manage.py runserver
CMD gunicorn frukt.wsgi:application --bind 0.0.0.0:$PORT









## Base Image
#FROM ubuntu:22.04
#
## create and set working directory
#RUN mkdir /app
#WORKDIR /app
#
## Add current directory code to working directory
#ADD . /app/
#
## set default environment variables
#ENV PYTHONUNBUFFERED 1
#ENV LANG C.UTF-8
#ENV DEBIAN_FRONTEND=noninteractive
#
## set project environment variables
## grab these via Python's os.environ
## these are 100% optional here
#ENV PORT=8080
#
## Install system dependencies
#RUN apt-get update && apt-get install -y --no-install-recommends \
#        tzdata \
#        python3-setuptools \
#        python3-pip \
#        python3-dev \
#        python3-venv \
#        git \
#        && \
#    apt-get clean && \
#    rm -rf /var/lib/apt/lists/*
#
#
## install environment dependencies
#RUN pip3 install --upgrade pip
#RUN pip3 install pipenv
#
## Install project dependencies
#RUN pipenv install -r requirements.txt
##RUN pipenv install --skip-lock --system --dev
#
#EXPOSE 8888
#CMD gunicorn frukt.wsgi:application --bind 0.0.0.0:$PORT












#FROM python:3.11.0-alpine3.17
#ENV PYTHONUNBUFFERED=1
#COPY ./requirements.txt /requirements.txt
#RUN pip install -r /requirements.txt
#RUN mkdir /minor_swing
#WORKDIR /minor_swing
#COPY . /minor_swing
##RUN adduser -D user
##USER user
#CMD python manage.py runserver 0.0.0.0:8080





#FROM python:3.11.0-alpine3.17
#ENV PYTHONUNBUFFERED=1
#COPY ./requirements.txt /requirements.txt
#RUN mkdir minor_swing
#COPY . /minor_swing/
#RUN pip install -r /requirements.txt
#WORKDIR /minor_swing/
#CMD python manage.py runserver
