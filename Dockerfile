FROM python:3.11.0-alpine3.17

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./frukt /app
#COPY ./frukt/static /static
WORKDIR /app

COPY ./entrypoint.sh /

RUN ["apk", "update"]
RUN ["apk", "add", "nano"]

ENTRYPOINT ["sh", "/entrypoint.sh"]
