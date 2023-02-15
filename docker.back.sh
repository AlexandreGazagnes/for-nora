#! /bin/sh

docker build -f ./Dockerfile.back -t for-nora.back:latest . &&  \
docker run  -p 8080:8080 -ti for-nora.back:latest python3 run_back.py