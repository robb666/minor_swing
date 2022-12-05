FROM python:3.11.0-alpine3.17
#ENV PATH="/scripts:${PATH}"
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /requirements.txt
RUN mkdir minor_swing
ADD . /minor_swing/
WORKDIR /minor_swing/
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    adduser -D robb
USER robb
ENV PORT=8080
#EXPOSE 8888
CMD ["entrypoint.sh"]
CMD gunicorn frukt.wsgi:application --bind 0.0.0.0:$PORT
