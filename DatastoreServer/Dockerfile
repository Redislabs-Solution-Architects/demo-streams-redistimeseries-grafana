FROM ubuntu:19.04
RUN apt update
RUN apt install -y python git python-pip
ADD . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python GrafanaDatastoreServer.py --redis-server redis
