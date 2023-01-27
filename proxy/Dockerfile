FROM nginxinc/nginx-unprivileged:1-alpine

COPY --chown=$USER ./default.conf /etc/nginx/conf.d/default.conf
RUN sed -i 's/.*server_names_hash_bucket_size.*/\t server_names_hash_bucket_size 64;/' /etc/nginx/nginx.conf