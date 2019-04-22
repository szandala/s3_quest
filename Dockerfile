FROM python:3.7.3-alpine3.8

RUN pip install \
    sqlalchemy sqlalchemy-utils \
    mysql-connector-python \
    falcon gunicorn

WORKDIR /app

ENTRYPOINT ["python"]
