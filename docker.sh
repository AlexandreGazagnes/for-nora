#! /bin/sh

docker build -f ./Dockerfile -t for-nora:latest .  && docker run -p 8080:8080 -ti for-nora:latest python api.py 
# docker run -ti for-nora:latest python main.py
# docker run -p 8080:8080 -ti for-nora:latest python back.py 