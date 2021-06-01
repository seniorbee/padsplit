# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies for Pillow
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add --no-cache jpeg-dev zlib-dev

# copy requirements
COPY moveoutlist/requirements.txt .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apk del .tmp

# copy project
COPY moveoutlist/ .