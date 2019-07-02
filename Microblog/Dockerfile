FROM python:latest
MAINTAINER Vinícius Melo "vinicius.m.melo@me.com"
COPY . /var/web
WORKDIR /var/web
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["flask", "run"]
EXPOSE 5000 
