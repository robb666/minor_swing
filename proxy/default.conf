upstream django {
	server django_gunicorn:8080;
}

server {
	listen 80 default_server;
    listen [::]:80 default_server;

    location /favicon.ico {
        access_log off;
        log_not_found off;
    }

	location / {
		proxy_pass http://django;
	}

    location /static/ {
        autoindex on;
		alias /static/;
	}
}