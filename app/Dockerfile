FROM python:3.9.7

WORKDIR /app
ENV FLASK_APP=app

COPY ./requirements.txt ./

RUN \
pip install --upgrade pip && \
pip install -r ./requirements.txt
