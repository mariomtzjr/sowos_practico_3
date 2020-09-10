FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

COPY ./etc/requirements.txt /code/

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev gettext-dev


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos el proyecto
COPY . /code/
