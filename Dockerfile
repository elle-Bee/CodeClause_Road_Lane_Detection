FROM python:3.8

WORKDIR /app
COPY requirements.txt .

#update and install dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y libx11-6 libxext6 libxrender1 \
                       libxtst6 libxi6 libfontconfig1 \
                       dbus-x11 libxrender-dev\
                       libglib2.0-0 libsm6
RUN apt-get install -y mesa-common-dev libgl1-mesa-dev \
                       libglu1-mesa-dev freeglut3-dev

#install requirements.txt
RUN pip install -r requirements.txt

COPY main.py .
COPY test.mp4 .

ENTRYPOINT [ "python","main.py" ]
