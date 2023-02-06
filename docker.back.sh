#! /bin/sh

docker build -f ./Dockerfile -t for-nora:latest . &&  \
docker run --env-file=./conf.env -p 8080:8080 -ti for-nora:latest /bin/bash