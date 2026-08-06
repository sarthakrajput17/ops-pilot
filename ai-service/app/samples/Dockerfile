FROM python:latest

WORKDIR /app

COPY . .

RUN apt-get update

RUN apt-get install -y curl

CMD ["python","main.py"]