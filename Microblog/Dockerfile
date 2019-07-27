FROM python:latest
MAINTAINER Vinícius Melo "vinicius.m.melo@me.com"
COPY . /var/web
WORKDIR /var/web
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV FLASK_APP=microblog.py
CMD ["flask", "run"]
EXPOSE 5000 
