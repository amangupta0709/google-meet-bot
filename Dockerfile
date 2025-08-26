FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive \
    CONTAINER_USER=python \
    DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'

RUN apt-get update && \
    apt-get install -yqq --no-install-recommends ffmpeg python3-distutils gcc

RUN mkdir /var/app
WORKDIR /var/app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
