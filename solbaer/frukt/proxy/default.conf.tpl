
server {
    listen $(LISTEN_PORT);

    location /static {
        alias /vol/static;
    }

    location @s3{
        proxy_pass https://django-frukt-files.s3.eu-west-1.amazonaws.com/images/;
   }
}