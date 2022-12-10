FROM ubuntu:20.04

# basic tools
RUN apt-get update
RUN apt-get install -y nano
RUN apt-get install -y net-tools

# deployments
RUN apt-get install -y nginx
RUN apt-get install -y supervisor

# application
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip

# setting up venv
COPY ./storage/app/requirements.txt .
RUN cd / && pip3 install virtualenv && python3 -m virtualenv venv
ENV PATH="/venv/bin:$PATH"
RUN /venv/bin/pip install --upgrade pip
RUN /venv/bin/pip install -r requirements.txt

# setting up nginx
COPY ./storage/deployments/app-nginx.conf /etc/nginx/conf.d/

# setting up supervisord
COPY ./storage/deployments/supervisord.conf /etc/supervisor/conf.d/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# prepare storage dir
RUN mkdir /storage.d