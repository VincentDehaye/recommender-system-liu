FROM python:3.4.3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /config/
ADD requirements.txt /config/
RUN pip install --upgrade pip
RUN pip install --timeout 1000 -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src
