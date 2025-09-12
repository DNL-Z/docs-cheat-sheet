# RASPBERRY Pi 3B+ - OS RASPBIAN

IP-Freebox :

82.66.182.201

IP-Local-**Raspberry**-Pi :
 192.168.1.116

## Characteristics

	- Processor ARM Cortex-A53 64 bit quad-core 1,4 GHz
	- RAM 1 GB
	- Wi-Fi 5GHz
	- Bluetooth 4.2/BLE
	- 4 USB ports
	- Ethernet
	- HDMI
	- Micro-SD 32GB
	- GPIO connector with 40 I/O pins

## Applications

	=> **Raspberry** Pi Imager
	=> VNC Viewer

## Know version OS

```bash
cat /etc/os-release
```

## Update package lists

```bash
sudo apt update
```

## Download and install updated packages

```bash
sudo apt upgrade
```

## Clean old package

```bash
sudo apt clean
```

## Connection en local

```bash
ssh dnl@192.168.1.116
```

## Connection SSH external

```bash
ssh dnl@zhalkovskyy.tech -p 16422
```

## Restart SSH

```bash
sudo systemctl restart ssh
```

## Know Nginx version

```bash
nginx -v
```

## Know Apache version

```bash
/usr/sbin/apache2 -v
```

## Know **PHP** version

```bash
php --version
```

## Know MySQL version

```bash
mysql -V
```

## Connection MySQL

```bash
sudo mysql -u root -p password
```

## The **Raspberry** Pi configuration tool

```bash
sudo raspi-config
```

## Start Graphical User Interface (home desk)

```bash
sudo systemctl start lightdm
```

## Show a tree of directories

```bash
tree -d
```

## Restart **Raspberry** Pi

```bash
sudo reboot
```

## Show permission for user

```bash
groups username
```

## Address IP configuration

```bash
ifconfig
```

## Show accessible port

```bash
nmap « IP »
```

## Status of Nginx server

```bash
sudo systemctl status nginx
```

## Restart Nginx server

```bash
sudo systemctl restart nginx
```

## Status of Apache server

```bash
sudo systemctl status apache2
```

## Restart Apache server

```bash
sudo /etc/init.d/apache2 restart
```

OR

```bash
sudo systemctl restart apache2
```

## Start & stop Apache server

```bash
sudo /etc/init.d/apache2 start
```

$
sudo /etc/init.d/apache2 stop

## Do not start Apache at startup

```bash
sudo systemctl disable apache2
```

## Running Apache automatically at startup

```bash
sudo systemctl enable apache2
```

---

## Setup Nginx server

```bash
sudo nano /etc/ssh/sshd_config
sudo nano /etc/nginx/sites-available/zhalkovskyy.tech
```

```bash
sudo ln -s /etc/nginx/sites-available/zhalkovskyy.tech /etc/nginx/sites-enabled/
```

## DNS, CSR, SSL, TLS, DMZ

	=> Domain Name System
	=> Certificate Signing Request
	=> Secure Sockets Layer
	=> Transport Layer Security
	=> DeMilitarized Zone

## Activate SSL module

```bash
sudo a2enmod ssl
```

## Create CSR for SSL

```bash
openssl req -nodes -newkey rsa:2048 -sha256 -keyout myserver.key -out server.csr -utf8
```

## Create certificate with Let’s encrypt & Certbot (Nginx & Apache)

```bash
sudo apt install python-certbot-nginx
sudo certbot --nginx
sudo certbot --nginx -d zhalkovskyy.tech -d www.zhalkovskyy.tech
```

OR

```bash
sudo apt install python-certbot-apache
```

```bash
sudo certbot --apache
sudo certbot --apache -d zhalkovskyy.tech -d www.zhalkovskyy.tech
```

## Change the rules for Firewall with UFW

```bash
sudo ufw status
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

## Path of certificates SSL

```bash
cat Server-CSR-SSL/server.csr
cat /etc/ssl/certs/ssl-cert-snakeoil.pem
```

```bash
cat Server-CSR-SSL/myserver.key
cat /etc/ssl/private/ssl-cert-snakeoil.key
```

---

## Crate a new user

```bash
sudo adduser new_username
```

## Grant sudo privileges

```bash
sudo usermod -aG sudo new_username
```

## Transfer home directory files

```bash
sudo cp -r /home/pi/* /home/new_username/
```

## Change ownership

```bash
sudo chown -R new_username:new_username /home/new_username/
```

## Update autologin configuration

```bash
sudo nano /etc/lightdm/lightdm.conf
```

=> autologin-user=new_username

## Delete the old pi user

```bash
sudo deluser --remove-home pi
```

---

## Micro-SD at the end of the life

```bash
mount => see if it ReadOnly or ReadWrite
sudo umount /
sudo fsck -y /
sudo mount /
```

(it’s better to change Micro-SD card)

---
