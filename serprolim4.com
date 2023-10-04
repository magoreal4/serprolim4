# /etc/nginx/sites-available/serprolim4

server {
    server_name limpiezapozossepticos.com www.limpiezapozossepticos.com;

    location = /favicon.ico { 
        access_log off; 
        log_not_found off; 
        }

    location /static/ {
        autoindex on;
        alias /root/serprolim4/staticfiles/;
        }
    
    location /media/ {
        autoindex on;
        alias /root/serprolim4/media/;
        }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/serprolim4.sock;
    }
}
