FROM python:3.13.0a2-slim

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY . /app
RUN pip install -e .
