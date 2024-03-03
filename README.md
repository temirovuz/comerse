

Django Deploy Ubuntu Server




Server yangi olinganda unga bog'lanib yangilab yuborish kerak: sudo apt update

Serverga PostgreSQL ni o'rnating agar kerak bo'lsa , bo'lmasa sqlite3 ham bo'ladi!: sudo apt install postgresql postgresql-contrib

Va start: sudo systemctl start postgresql.service


Serverga muhitni o'rnating: sudo apt-get install python3-venv

Loyihani serverga clone qilib oling 

Loyiha papkasiga kiring 


Muhit yaratın: python3 -m venv venv

Muhtini activate qiling: . venv/bin/activate


Kerakli modullarni o'nating: pip3 install -r requirements.txt 


Agar baza sifatida PostgreSQL ni tanlagan bo'lsangiz Serveringizga uni o'rnating va baza create qiling!  loyihani ishga tushurmoqchi bo'lsangiz Agar baza yaratilmagan bolsa xatolik beradi!


PostgreSQL ni o'rnatib bo'lgach shu komanda bilan PostgreSQLga  bog'laning: sudo -i -u postgres

Endi baza yaratish uchun PostgreSQL ga kiring: psql


PostgreSQL da baza yaratish: create database database_nomi;
PostgreSQL da user yaratish: create user user_nomi with password 'password_yozasiz';
Chiqish uchun \q va keyin logout yozing


Loyihaga makemigraitons va migrate bering: python3 manage.py makemigrations, python3 manage.py migrate


Loyihani ishga tushiring test uchun: python3 manage.py runserver O'zingizni IP ni yozing:8000  masalan: python3 manage.py runserver 89.456.342.31:8000 


Muhitga gunicorn o'rnatilganligiga ishonch komil qiling: pip3 install gunicorn

Gunicorn yordamida loyihani test qilib ishga tushirib ko'ramiz:  gunicorn --bind 0.0.0.0:8000 loyihangiz_nomi.wsgi


Loyihani doimiy ishlab turishi uchun socket filelarni yaratishni boshlang: sudo nano /etc/systemd/system/gunicorn.socket 

[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target

Saqlash uchun: ctrl+s va ctrl+x ni Bosing!



Keyingi fayl: sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=root                                               # user nomi
Group=www-data
WorkingDirectory=/opt/telegrambotapi/myproject               # Loyihangiz joylashuvi va loyiha nomi!
ExecStart=/opt/telegrambotapi/venv/bin/gunicorn \            # Loyiha muhitini joylashuvi
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          loyihangiz_nomi.wsgi:application

[Install]
WantedBy=multi-user.target



Saqlash uchun: ctrl+s va ctrl+x ni Bosing!



Quydagi komandalarni bering:
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl status gunicorn.socket



Serverga NGINX ni o'rnating: sudo apt-get install nginx

Ningx fayl yarating: sudo nano /etc/nginx/sites-available/myproject

                          
server {
        listen 80;
        server_name domeningiz_nomi(httplarsiz);  # domen

        location = /favicon.ico { access_log off; log_not_found off; }
        location /static/ {
                autoindex on;
                alias /opt/uzairways/static/;  # static joylashuvi

        }
        location /media {
                autoindex on;
                alias /opt/uzairways/media/;   # media joylashuvi
        }
         
        location / {
                include proxy_params;
                proxy_pass http://unix:/run/gunicorn.sock;
        }
        
}

Saqlash uchun: ctrl+s va ctrl+x ni Bosing!



Faylni nusxalang: sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled


Nginxni tekshiring: sudo nginx -t


 systemctl daemon-reload
 sudo systemctl restart gunicorn
 sudo systemctl restart nginx


Loyola domen yoki IP ga kirib tekshirib ko'ring!




















