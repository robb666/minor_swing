upstream django {
	server django_gunicorn:8080;
}

server {
    listen $(LISTEN_PORT);

    location /static {
        alias /vol/static;
    }

     location /images/ {
        proxy_pass django-frukt-files;
        default_type "image/gif";

   }
}





    location /s3/ {
      proxy_http_version     1.1;
      proxy_set_header       Connection "";
      proxy_set_header       Authorization '';
      proxy_set_header       Host yanpy.dev.s3.amazonaws.com;
      proxy_hide_header      x-amz-id-2;
      proxy_hide_header      x-amz-request-id;
      proxy_hide_header      x-amz-meta-server-side-encryption;
      proxy_hide_header      x-amz-server-side-encryption;
      proxy_hide_header      Set-Cookie;
      proxy_ignore_headers   Set-Cookie;
      proxy_intercept_errors on;
      add_header             Cache-Control max-age=31536000;
      proxy_pass             http://yanpy.dev.s3.amazonaws.com/;
    }