FROM python:3.4.3
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD APIManager/requirements.txt /config/
RUN pip install -r /config/requirements.txt
RUN mkdir /src;
WORKDIR /src
