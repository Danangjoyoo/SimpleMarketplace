#!/bin/bash

supervisord
sleep 3s
tail -f /var/log/supervisor/uwsgi-stderr.log &
tail -f /var/log/supervisor/uwsgi-stdout.log