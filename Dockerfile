RUN dos2unix /entrypoint.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*
FROM python:3.4.3
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="${PYTHONPATH}:/src/"
RUN mkdir -p /config/Product
ADD requirements.txt /config/
ADD Product/requirements.txt /config/Product/
RUN pip install --upgrade pip
RUN pip install --timeout 1000 -r /config/requirements.txt
RUN mkdir /src
RUN mkdir /src/Product
ADD Product /src/Product
WORKDIR /src
CMD ["ipython"]
