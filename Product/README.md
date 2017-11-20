# How to run the development website

To start the development website use run the script 
`start_frontend_development_servers.sh`. 

What this actually does is starting the docker containers with the django 
development server from the APIManager folder and the Angular development server
from the Frontend folder. This can be done manually as well.

## Start Django development server
Run `docker-compose up &` from APIManager directory. This should start the django
development server in a docker container. However there are issues with the 
django server starting before the database server and crashing. If this happens 
run `docker-compose up web &`.

When there are significant changes to the containers one needs to run 
`docker-compose up --buld` to update the container image. This is rarely 
necessary, but if something you really expect should be working, isn't, then try
running this command.

## Start the Angular development server
Run `npm install` from Frontend directory to install all necessary dependencies.
After all dependencies are installed run `npm start`. This runs the start script
that is actually `ng serve --proxy-config proxy.conf.json`. This is used to 
allow communication with the django development server through the Angular 
development server.