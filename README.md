# moscow

Moscow Academy by iFraganus

___

# pip

```
python3 -m venv venv
source ./venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
```

___

# postgres

```
CREATE DATABASE moscow WITH OWNER solijonov;
GRANT ALL ON DATABASE moscow TO solijonov;
```

___

# Systemd service [moscow.service]

```
[Unit]
Description=Systemd service daemon for moscow
Before=nginx.service
After=network.target
[Service]
User=major
Group=major
WorkingDirectory=/home/major/moscow
# ExecStart=/home/major/moscow/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/major/moscow/gunicorn.sock project.wsgi:application
ExecStart=/home/major/moscow/venv/bin/python manage.py runserver 0.0.0.0:8005
Restart=always
SyslogIdentifier=gunicorn
[Install]
WantedBy=multi-user.target
```

___

# Nginx [moscow_backend]

```
server {
    listen 80;
    server_name ? www.?;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static {
        alias /home/major/moscow/static;
    }
    
    location /media  {
        alias /home/major/moscow/media;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/major/moscow/gunicorn.sock;
    }
}
```

___

# Nginx [moscow_frontend]

```
server {
    listen 80;
    server_name bordo-jamoasi.uz www.bordo-jamoasi.uz;
    root /home/major/frontend/poyabzal-build/dist;
    index index.html index.htm index.nginx-debian.html;
    location / {
        try_files $uri $uri/ /index.html;
        # try_files $uri $uri/ =404;
    }
}
```