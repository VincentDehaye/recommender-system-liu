FROM python:3.4.3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /config/APIManager
ADD requirements.txt /config/
ADD APIManager/requirements.txt /config/APIManager
RUN pip install -r /config/requirements.txt
RUN mkdir /src;
WORKDIR /src
