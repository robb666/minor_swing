FROM python:3.11.0-alpine3.17
#ENV PATH="/scripts:${PATH}"
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /requirements.txt
#RUN mkdir minor_swing
ADD . /app/
COPY ./scripts /scripts
WORKDIR /app/
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /vol
ENV PATH="/scripts:/py/bin:${PATH}"
ENV PORT=8080
USER app
#EXPOSE 8888
CMD ["run.sh"]
CMD gunicorn frukt.wsgi:application --bind 0.0.0.0:$PORT

