FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project
ADD . .
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8080