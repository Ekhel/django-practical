FROM python:3.7-alpine
MAINTAINER django-practical

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /practical
WORKDIR practical
COPY ./practical /practical

RUN adduser -D user
USER user
