FROM python:3.13

# RUN apk update && apk add --no-cache \
#     mariadb-dev \
#     gcc \
#     musl-dev \
#     linux-headers
# WORKDIR /backend/app
RUN apt-get update && apt-get install -y netcat-openbsd
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install django-cors-headers
RUN pip install djangorestframework
RUN pip install pytest coverage coveralls

EXPOSE 8000

# CMD [ "python", "backend/app/manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["ls"]