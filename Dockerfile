FROM python:3.8

COPY data /data
COPY src /src
COPY src/main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt



