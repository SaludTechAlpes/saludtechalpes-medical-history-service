# Usa una versión específica de Python (3.9-alpine3.16)
FROM python:3.9-alpine3.16

WORKDIR /app

ENV PYTHONPATH=/app/src

RUN apk add --no-cache \
    build-base \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    python3-dev \
    libstdc++ \
    gcompat


COPY requirements.txt ./
RUN pip install --upgrade "pip<24.1"
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 3002

COPY ./docker/start.sh /start.sh
RUN chmod +x /start.sh

CMD ["make", "run-docker"]