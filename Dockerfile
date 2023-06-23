FROM python:3.12.0b3-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY . /app
RUN pip install -e .
