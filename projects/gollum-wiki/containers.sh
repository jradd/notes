#!/bin/bash

#ENVARS
LOCAL_DIR="/srv/data/notes"
GITHUB_ID=""
GITHUB_SECRET=""

CONTAINER_NGINX_PROXY="docker run -d -p 80:80 -p 443:443 --name nginx-proxy \
  -v /srv/data/nginx/certs:/etc/nginx/certs:ro \
  -v /srv/data/nginx/vhost.d:/etc/nginx/vhost.d \
  -v /srv/data/nginx/html:/usr/share/nginx/html \
  -v /var/run/docker.sock:/tmp/docker.sock:ro \
  -v /srv/data/nginx/conf.d:/etc/nginx/conf.d \
  -v /srv/data/nginx/sites-enabled:/etc/nginx/sites-enabled \
  jwilder/nginx-proxy"

CONTAINER_LETS_ENCRYPT="docker run -d \
  -v /srv/data/nginx/certs:/etc/nginx/certs:rw \
  --volumes-from nginx-proxy \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  jrcs/letsencrypt-nginx-proxy-companion"

CONTAINER_VOLUME_DATA="docker create --name data-volume -v ${LOCAL_DIR}:/wiki busybox:latest
/bin/true"

CONTAINER_GOLLUM_WIKI="docker run -d \
-e "VIRTUAL_HOST=wiki.jradd.com" \
-e "LETSENCRYPT_HOST=wiki.jradd.com" \
-e "LETSENCRYPT_EMAIL=jredd42@gmail.com" \
--volumes-from data-volume \
-v "${NOTES_DIR}":/wiki \
-p 8212 \
jradd/gollum-wiki:testing"
