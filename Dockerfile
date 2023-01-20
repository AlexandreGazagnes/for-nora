FROM python:3.9-bullseye 

# date
RUN rm -f /etc/localtime  && ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime 
# RUN echo "date is $(date)"

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
COPY ./make.sh /app/make.sh
# RUN pwd
# RUN ls
# RUN chmod --help
RUN chmod +x ./make.sh
# RUN ls -lah
RUN ./make.sh

# copy the app && rm test
COPY . /app

# CMD 
RUN echo "hello"
RUN /bin/bash