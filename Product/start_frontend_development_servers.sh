#!/bin/bash

cd ../APIManager
cd APIManager
docker-compose up db &

cd Frontend
cd ../Frontend
npm install
npm start &


cd ../APIManager
docker-compose up web &
