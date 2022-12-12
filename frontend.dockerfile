FROM ubuntu:20.04

# base tools
RUN apt-get update
RUN apt-get install -y nano
RUN apt-get install -y nginx
RUN apt-get install -y supervisor
RUN apt-get install -y curl

# core tools
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
RUN export NVM_DIR="$HOME/.nvm" && \
    echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> ~/.bashrc && \
    echo '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"' >> ~/.bashrc && \
    . ~/.bashrc && \
    nvm install node
RUN apt-get install -y nodejs npm
# RUN /root/.nvm/versions/node/v19.2.0/bin/npm install -g npm@9.2.0
# RUN /root/.nvm/versions/node/v19.2.0/bin/npm install react
# RUN /root/.nvm/versions/node/v19.2.0/bin/npm install antd

# setting up nginx
COPY ./frontend/deployments/app-nginx.conf /etc/nginx/conf.d/

# setting up supervisord
COPY ./frontend/deployments/nginx-supervisord.conf /etc/supervisor/conf.d/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# npm install -g npm@9.2.0 && npm install antd && npm install react-router-dom && npm install && npm start