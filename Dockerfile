FROM python:3.9

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

COPY src/ .
COPY drivingv/ .

ENTRYPOINT [ "python","main.py" ]