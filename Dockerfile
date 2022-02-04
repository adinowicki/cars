FROM python:3.10-slim
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev
WORKDIR /app
COPY . .
RUN python3 -m pip install -r requirements.txt
