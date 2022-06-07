FROM python:3

RUN apt-get update && apt-get install -y vim

RUN pip3 install pycurl
