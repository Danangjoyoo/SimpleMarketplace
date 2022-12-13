#!/bin/bash

cd /base/app
npm install -g npm@9.2.0
npm install
npm run build

cd /
/usr/bin/supervisord
sleep 5s
tail -f /var/log/supervisor/supervisord.log