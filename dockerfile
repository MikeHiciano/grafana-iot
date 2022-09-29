FROM ubuntu:16.04

COPY ./server /usr/src/app/

WORKDIR /usr/src/app/

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get -y update && \
    apt-get install -y python3.9 && \
    apt-get install -y python3-pip

RUN pip3 install -r requirements.txt

CMD ["python3","usr/src/app/server.py"]