##### Ghost Container w/ nginx  
DATA_GHOST="docker create --name ghost-data -v /srv/data/ghost:/var/lib/ghost busybox:latest /bin/true"
APP_GHOST="docker run --name ghost-app --volumes-from ghost-data -p 8080:2368 ghost"

APP_NGINX="docker run -d -p 80:80 --link ghost-app:ghost-app --name nginx -v /srv/data/nginx/logs:/var/log/nginx -v /srv/data/nginx/nginx.conf:/etc/nginx/nginx.conf nginx"
