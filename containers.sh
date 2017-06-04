#!/usr/bin/env bash

docker run -d -p 80:80 -p 443:443 \
-v /srv/data/nginx/certs:/etc/nginx/certs:ro \
-v /srv/data/nginx/vhost.d:/etc/nginx/vhost.d \
-v /srv/share/www:/usr/share/nginx/html \
-v /var/run/docker.sock:/tmp/docker.sock:ro \
jwilder/nginx-proxy
sleep 2;
echo 'starting letsencrypt-nginx'
docker run -d \
-v /srv/data/nginx/certs:/etc/nginx/certs:rw \
--volumes-from nginx-proxy \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
jrcs/letsencrypt-nginx-proxy-companion
sleep 2;
echo 'starting example container Gollum Wiki'
docker run -d \
-e "VIRTUAL_HOST=wiki.jradd.com" \
-e "LETSENCRYPT_HOST=wiki.jradd.com" \
-e "LETSENCRYPT_EMAIL=jredd42@gmail.com" \
--volumes-from gollum-data \
-v /srv/data/wiki:/wiki \
-p 8212 \
--env-file /srv/data/wiki/.build/gollum-app.env \
--name gollum-wiki \
jradd/gollum-wiki

echo 'add more containers using letsencrypt envars and virtualhosts envars'
echo 'done!'
