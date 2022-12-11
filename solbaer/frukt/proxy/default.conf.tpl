server {
    listen $(LISTEN_PORT);

    location /static {
        alias /vol/static;
    }

}