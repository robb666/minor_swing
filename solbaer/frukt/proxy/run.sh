#!/bin/sh

set -e

envsubst < /etc/nginx/deafoult.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
