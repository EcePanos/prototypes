FROM ubuntu:20.04

RUN apt-get update -y --no-install-recommends &&\
apt-get install -y python3 python3-pip python3-setuptools --no-install-recommends

COPY . ./

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "test.py"]
