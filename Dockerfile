FROM python:3
ENV DEBIAN_FRONTEND=noninteractive \
    CONTAINER_USER=python \
    DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
RUN apt-get update && \
    apt-get install -yqq --no-install-recommends ffmpeg
RUN mkdir /var/app
WORKDIR /var/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
