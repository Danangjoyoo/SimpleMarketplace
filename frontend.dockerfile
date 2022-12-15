FROM ubuntu:20.04

# base tools
RUN apt-get update
RUN apt-get install -y nano
RUN apt-get install -y nginx
RUN apt-get install -y supervisor
RUN apt-get install -y curl

# core tools
RUN apt-get install -y npm
RUN npm cache clean -f
RUN npm install -g n
RUN n latest

# building app
COPY ./frontend/app /base/app
WORKDIR /base/app
RUN npm install
RUN npm run build

# setting up nginx
COPY ./frontend/deployments/app-nginx.conf /etc/nginx/conf.d/

# setting up supervisord
COPY ./frontend/deployments/nginx-supervisord.conf /etc/supervisor/conf.d/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf