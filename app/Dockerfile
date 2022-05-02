FROM python:3.9.7

WORKDIR /app
ENV FLASK_APP=app

COPY ./flaskapp/requirements.txt /app

RUN \
pip install --upgrade pip && \
pip install -r /app/requirements.txt
#pip install numpy &&\
#pip install
