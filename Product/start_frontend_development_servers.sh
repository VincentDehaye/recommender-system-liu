#!/bin/bash

docker-compose -f APIManager/docker-compose.yml up db &

cd UI
npm install

docker-compose -f ../APIManager/docker-compose.yml up web &

npm start
