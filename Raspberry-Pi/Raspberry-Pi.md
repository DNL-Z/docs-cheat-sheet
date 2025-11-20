# 🍓 Raspberry Pi

A comprehensive reference guide for Raspberry Pi administration, covering system management, web servers, SSL certificates, and user management.

## 📑 Table of Contents

- [⚙️ Hardware Specifications](#-hardware-specifications)
- [📱 Essential Applications](#-essential-applications)
- [🔄 System Management](#-system-management)
  - [Check OS Version](#check-os-version)
  - [Update System](#update-system)
  - [Configuration Tool](#configuration-tool)
  - [Restart System](#restart-system)
  - [Start GUI](#start-gui)
- [🌐 Network Configuration](#-network-configuration)
  - [IP Configuration](#ip-configuration)
  - [SSH Connection](#ssh-connection)
  - [Port Scanning](#port-scanning)
- [👥 User Management](#-user-management)
  - [Create New User](#create-new-user)
  - [Grant Sudo Privileges](#grant-sudo-privileges)
  - [Transfer Files](#transfer-files)
  - [Change Ownership](#change-ownership)
  - [Update Autologin](#update-autologin)
  - [Delete User](#delete-user)
  - [Show User Permissions](#show-user-permissions)
- [🌍 Web Servers](#-web-servers)
  - [Nginx](#nginx)
  - [Apache](#apache)
- [🔒 SSL/TLS Certificates](#-ssltls-certificates)
  - [SSL Terminology](#ssl-terminology)
  - [Certificate Management](#certificate-management)
  - [Firewall Configuration](#firewall-configuration)
- [🗄️ Database Management](#-database-management)
  - [MySQL](#mysql)
- [📁 File System](#-file-system)
  - [Directory Navigation](#directory-navigation)
  - [SD Card Troubleshooting](#sd-card-troubleshooting)

---

## ⚙️ Hardware Specifications

**Raspberry Pi 3B+ Specifications:**

- **Processor:** ARM Cortex-A53 64-bit quad-core 1.4 GHz
- **RAM:** 1 GB
- **Wireless:** Wi-Fi 5GHz, Bluetooth 4.2/BLE
- **Ports:** 4× USB, Ethernet, HDMI
- **Storage:** Micro-SD 32GB
- **GPIO:** 40 I/O pins connector

---

## 📱 Essential Applications

- **Raspberry Pi Imager** - OS installation tool
- **VNC Viewer** - Remote desktop access

---

## 🔄 System Management

### Check OS Version

```bash
  cat /etc/os-release
```

### Update System

**Update package lists:**

```bash
  sudo apt update
```

**Download and install updated packages:**

```bash
  sudo apt upgrade
```

**Clean old packages:**

```bash
  sudo apt clean
```

### Configuration Tool

Access the Raspberry Pi configuration tool:

```bash
  sudo raspi-config
```

### Restart System

```bash
  sudo reboot
```

### Start GUI

Start the graphical user interface (desktop environment):

```bash
  sudo systemctl start lightdm
```

---

## 🌐 Network Configuration

### IP Configuration

View network configuration:

```bash
  ifconfig
```

### SSH Connection

**Local connection:**

```bash
  ssh username@192.168.1.xxx
```

**External connection:**

```bash
  ssh username@domain.com -p port_number
```

**Restart SSH service:**

```bash
  sudo systemctl restart ssh
```

### Port Scanning

Show accessible ports:

```bash
  nmap <IP_ADDRESS>
```

---

## 👥 User Management

### Create New User

```bash
  sudo adduser new_username
```

### Grant Sudo Privileges

```bash
  sudo usermod -aG sudo new_username
```

### Transfer Files

Transfer home directory files to a new user:

```bash
  sudo cp -r /home/old_user/* /home/new_username/
```

### Change Ownership

```bash
  sudo chown -R new_username:new_username /home/new_username/
```

### Update Autologin

```bash
  sudo nano /etc/lightdm/lightdm.conf
```

Update the configuration:

```
autologin-user=new_username
```

### Delete User

Delete user and remove the home directory:

```bash
  sudo deluser --remove-home username
```

### Show User Permissions

```bash
  groups username
```

---

## 🌍 Web Servers

### Nginx

**Check version:**

```bash
  nginx -v
```

**Check service status:**

```bash
  sudo systemctl status nginx
```

**Restart service:**

```bash
  sudo systemctl restart nginx
```

**Setup Nginx server:**

Edit SSH configuration:

```bash
  sudo nano /etc/ssh/sshd_config
```

Edit site configuration:

```bash
  sudo nano /etc/nginx/sites-available/your-site
```

Create a symbolic link to enable the site:

```bash
  sudo ln -s /etc/nginx/sites-available/your-site /etc/nginx/sites-enabled/
```

### Apache

**Check version:**

```bash
  /usr/sbin/apache2 -v
```

**Check service status:**

```bash
  sudo systemctl status apache2
```

**Restart service:**

Option 1:

```bash
  sudo /etc/init.d/apache2 restart
```

Option 2:

```bash
  sudo systemctl restart apache2
```

**Start service:**

```bash
  sudo /etc/init.d/apache2 start
```

**Stop service:**

```bash
  sudo /etc/init.d/apache2 stop
```

**Disable automatic startup:**

```bash
  sudo systemctl disable apache2
```

**Enable automatic startup:**

```bash
  sudo systemctl enable apache2
```

---

## 🔒 SSL/TLS Certificates

### SSL Terminology

- **DNS** - Domain Name System
- **CSR** - Certificate Signing Request
- **SSL** - Secure Sockets Layer
- **TLS** - Transport Layer Security
- **DMZ** - DeMilitarized Zone

### Certificate Management

**Activate SSL module (Apache):**

```bash
  sudo a2enmod ssl
```

**Create CSR for SSL:**

```bash
  openssl req -nodes -newkey rsa:2048 -sha256 -keyout myserver.key -out server.csr -utf8
```

**Create a certificate with Let's Encrypt & Certbot:**

For Nginx:

```bash
  sudo apt install python-certbot-nginx
  sudo certbot --nginx
  sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

For Apache:

```bash
  sudo apt install python-certbot-apache
  sudo certbot --apache
  sudo certbot --apache -d your-domain.com -d www.your-domain.com
```

**Certificate paths:**

View CSR:

```bash
  cat Server-CSR-SSL/server.csr
  cat /etc/ssl/certs/ssl-cert-snakeoil.pem
```

View private key:

```bash
  cat Server-CSR-SSL/myserver.key
  cat /etc/ssl/private/ssl-cert-snakeoil.key
```

### Firewall Configuration

**Manage UFW (Uncomplicated Firewall):**

Check status:

```bash
  sudo ufw status
```

Allow ports:

```bash
  sudo ufw allow 22/tcp    # SSH
  sudo ufw allow 80/tcp    # HTTP
  sudo ufw allow 443/tcp   # HTTPS
```

---

## 🗄️ Database Management

### MySQL

**Check version:**

```bash
  mysql -V
```

**Connect to MySQL:**

```bash
  sudo mysql -u root -p
```

---

## 📁 File System

### Directory Navigation

**Show the directory tree:**

```bash
  tree -d
```

### SD Card Troubleshooting

**When a Micro-SD card is at the end of its life:**

Check if mounted as ReadOnly or ReadWrite:

```bash
  mount
```

Unmount and check the file system:

```bash
  sudo umount /
  sudo fsck -y /
  sudo mount /
```

> **Note:** If the SD card shows signs of failure, it's recommended to replace it with a new one.

---

## 🔍 Additional Commands

### Software Versions

**Check PHP version:**

```bash
  php --version
```

---

## 💡 Tips

- Always keep your system updated with `sudo apt update && sudo apt upgrade`
- Regularly backup your SD card to prevent data loss
- Use strong passwords for all user accounts
- Enable firewall rules to secure your Raspberry Pi
- Monitor disk space and clean old packages regularly
