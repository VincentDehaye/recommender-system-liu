#!/bin/bash

# Trap sigint (CTRL-C) and cleanup the development environment.
trap "cleanup" INT

cleanup() {
	trap "" INT TERM
	echo "**** Shutting down... ****"
    docker-compose down
	kill -TERM 0
	wait
	echo "Done with cleanup"
}

# Try to make sure that we're in the correct folder for running the script, then start the
# development environment.
cd Product
cd ..
cd Product
docker-compose up &

cd Frontend
npm install
npm start &

# Wait for sigint
cat
