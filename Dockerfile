# FROM continuumio/anaconda3:4.4.0

# MAINTAINER Rupali Sinha

FROM python:3.7
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev \
    postgresql python-psycopg2 libpq-dev

COPY . /usr/local/python/

EXPOSE 5000

WORKDIR /usr/local/python/

RUN pip3 install -r requirements.txt

CMD python flask_predict.py