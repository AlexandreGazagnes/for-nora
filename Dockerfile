FROM python:3.9-bullseye 

# date
RUN rm -f /etc/localtime  && ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime 

# Workdir
WORKDIR /app

# Copy
COPY ./requirements.txt /app/requirements.txt
COPY ./make.sh /app/make.sh

# Make
RUN chmod +x ./make.sh && ./make.sh

# Copy the app 
COPY . /app

# Cmd
RUN echo "hello"
RUN /bin/bash