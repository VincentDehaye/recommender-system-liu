#!/bin/bash
res=6
while [ $res -ne 52 ]
do
	sleep 1
	curl -s $WEBSITE_DATABASE_HOST:5432
	res=$?
done

cd Product/APIManager &&
python manage.py makemigrations &&
python manage.py migrate &&

if [ ${PRODUCTION:-0} -eq 1 ]; then
	gunicorn project_config.wsgi --access-logfile '-' -b 0.0.0.0:8000
else
	gunicorn project_config.wsgi --reload --access-logfile '-' -b 0.0.0.0:8000
fi
