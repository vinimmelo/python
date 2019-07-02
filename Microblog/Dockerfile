FROM python:latest
MAINTAINER Vinícius Melo "vinicius.m.melo@me.com"
COPY . /var/web
WORKDIR /var/web
RUN pip install -r requirements
ENTRYPOINT python microblog.py
EXPOSE 5000 
