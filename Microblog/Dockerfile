FROM ubuntu:latest
MAINTAINER Vinícius Melo "vinicius.m.melo@me.com"
COPY . /var/web
WORKDIR /var/web
RUN  apt-get update && apt-get install -y python3-pip python3
RUN pip install -r requirements
ENTRYPOINT python microblog.py
EXPOSE 3000

