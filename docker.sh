#! /bin/sh

docker build -f ./Dockerfile -t for-nora:latest .  
# docker run -ti for-nora:latest python main.py
docker run -ti for-nora:latest /bin/bash        