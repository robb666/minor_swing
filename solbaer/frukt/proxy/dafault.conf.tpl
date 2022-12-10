upstream django {
	server django_gunicorn:8080;
}

server {
    listen $(LISTEN_PORT);

    location /static {
        alias /vol/static;
    }

     location /images/ {
        proxy_pass https://django-frukt-files.s3.eu-west-1.amazonaws.com/images/;
        default_type "image/gif";
   }
}