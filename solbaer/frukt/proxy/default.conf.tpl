upstream django {
	server django_gunicorn:8080;
}

server {
    listen 80;

    location / {
        proxy_pass http://django;
    }

    location /static {
        alias /vol/static;
    }

    location @s3{
        proxy_pass https://django-frukt-files.s3.eu-west-1.amazonaws.com/images/;
   }
}