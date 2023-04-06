#!/usr/bin/env bash
# Bash script that sets up your web servers for deployment

sudo apt update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Welcome to nginx static files test page" | sudo tee -a /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu.ubuntu /data/

sudo sed -i 's+location / {+location /data/web_static/current/ {\n\t\talias https://mydomainname.tech/hbnb_static;\n\t}\n\n\tlocation / {+' /etc/nginx/sites-available/default
sudo nginx -s reload
