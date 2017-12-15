FROM python:3.6

RUN apt-get update

RUN apt-get install -y build-essential python python-pip python-pillow

ADD . /code

WORKDIR /code

RUN python -m pip install -r ./requirements.txt