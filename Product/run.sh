#!/bin/bash/
cd Frontend/
npm run build
cd ..
docker-compose up
echo "done"
