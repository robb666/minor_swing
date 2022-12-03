FROM python:3.11.0-alpine3.17
ENV PYTHONUNBUFFERED=1

RUN mkdir minor_swing
WORKDIR /minor_swing
COPY ./requirements.txt /requirements.txt

COPY . /minor_swing/
#COPY . .

RUN pip install -r /requirements.txt

CMD python manage.py runserver 0.0.0.0:8080








#FROM python:3.11.0-alpine3.17
#ENV PYTHONUNBUFFERED=1
#COPY ./requirements.txt /requirements.txt
#RUN mkdir minor_swing
#COPY . /minor_swing/
#RUN pip install -r /requirements.txt
#WORKDIR /minor_swing/
#CMD python manage.py runserver
