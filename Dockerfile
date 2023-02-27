
FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8000
