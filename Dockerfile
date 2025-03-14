FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libmariadb-dev \
    netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-db.sh .
RUN chmod +x wait-for-db.sh

COPY . .

CMD ["sh", "-c", "./wait-for-db.sh db 3306 python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]