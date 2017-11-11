#!/bin/bash

res=6
while [ $res -ne 52 ]
do
	curl -s website_db:5432
	res=$?
done

cd APIManager &&
python manage.py makemigrations &&
python manage.py migrate &&
gunicorn project_config.wsgi --access-logfile '-' -b 0.0.0.0:8000
