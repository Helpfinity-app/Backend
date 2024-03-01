FROM python:3.10-slim-buster

WORKDIR /helpfinity_back

COPY /requirements/requirements.txt /helpfinity_back/requirements/

RUN pip install --upgrade pip

RUN apt-get update && apt-get upgrade -y

RUN pip install -r requirements/requirements.txt

COPY . /helpfinity_back


EXPOSE 8000 9000