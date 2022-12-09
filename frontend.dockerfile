FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y nano
RUN apt-get install -y net-tools
RUN apt-get install -y nginx
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y supervisor
RUN apt-get install -y openssh-server
RUN apt-get install -y git
RUN apt-get install -y sudo
RUN apt-get install -y npm
# RUN npm install -g ionic cordova