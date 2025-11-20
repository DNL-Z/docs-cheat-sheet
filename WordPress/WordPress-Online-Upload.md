# 🚀 WordPress Online Upload

Complete guide for migrating and deploying a WordPress site to a production server.

## 📑 Table of Contents

- [📥 Export Database from Source Server](#-export-database-from-source-server)
- [📦 Archive Website Files](#-archive-website-files)
- [🔄 Connect to Target Server](#-connect-to-target-server)
- [💾 Import Database](#-import-database)
- [📂 Deploy Website Files](#-deploy-website-files)
- [⚙️ Update Configuration](#-update-configuration)
- [🔗 Update URLs](#-update-urls)
- [🔒 Security Setup](#-security-setup)

---

## 📥 Export Database from Source Server

### Small Database (via phpMyAdmin)

If the database is not too large, export directly from phpMyAdmin:

1. Access phpMyAdmin
2. Select your database
3. Click on the "Export" tab
4. Choose an export method and download

### Large Database (via Command Line)

For larger databases, use `mysqldump` via FTP/SSH connection:

```bash
  mysqldump -u root -p db_name > file_name.sql
```

**Parameters:**
- `-u root`: Database username
- `-p`: Prompt for password
- `db_name`: Name of the database to export
- `file_name.sql`: Output SQL file name

---

## 📦 Archive Website Files

Create a compressed archive of your WordPress installation:

```bash
  sudo tar cvzf file_name.tar.gz site_directory_name
```

**Parameters:**
- `c`: Create new archive
- `v`: Verbose mode (display progress)
- `z`: Compress with gzip
- `f`: Specify file name
- `site_directory_name`: WordPress directory to archive

---

## 🔄 Connect to Target Server

Connect to your new production server via SSH or FTP using your hosting credentials.

```bash
  ssh username@server_address
```

---

## 💾 Import Database

Import the SQL database file to the new server:

```bash
  mysql -u username -p db_name < file_name.sql
```

**Parameters:**
- `-u username`: Database username on new server
- `-p`: Prompt for password
- `db_name`: Target database name
- `< file_name.sql`: Input SQL file to import

---

## 📂 Deploy Website Files

Extract the WordPress archive to the appropriate directory:

```bash
  sudo tar xvzf file_name.tar.gz
```

**Parameters:**
- `x`: Extract files
- `v`: Verbose mode
- `z`: Decompress gzip
- `f`: Specify archive file name

Move files to the correct web directory if needed (e.g., `/var/www/html/` or `/public_html/`).

---

## ⚙️ Update Configuration

### Update wp-config.php

Modify the `wp-config.php` file with new database credentials:

```php
define('DB_NAME', 'new_database_name');
define('DB_USER', 'new_username');
define('DB_PASSWORD', 'new_password');
define('DB_HOST', 'localhost');
```

**Important:** Update the database password from the old site configuration.

---

## 🔗 Update URLs

WordPress stores the site URL in the database. Update these references:

### Method 1: Search and Replace Plugin

Install and use a plugin like **Better Search Replace** or **Search Regex** to replace old URLs with new ones.

### Method 2: Direct Database Update

Update URLs in the `wp_options` table:

```sql
UPDATE wp_options
SET option_value = 'https://new-domain.com'
WHERE option_name = 'siteurl' OR option_name = 'home';
```

### Method 3: wp-config.php Override

Add these lines to `wp-config.php` (before "That's all, stop editing!"):

```php
define('WP_HOME', 'https://new-domain.com');
define('WP_SITEURL', 'https://new-domain.com');
```

---

## 🔒 Security Setup

Install and configure security plugins to protect your production site:

### Recommended Security Plugins

- **Wordfence Security**: Firewall and malware scanner
- **iThemes Security**: Comprehensive security hardening
- **Sucuri Security**: Security monitoring and auditing
- **All-in-one WP Security**: User-friendly security suite

### Essential Security Measures

1. Change default admin username
2. Use strong passwords
3. Enable two-factor authentication
4. Limit login attempts
5. Keep WordPress and plugins updated
6. Configure SSL certificate (HTTPS)
7. Set proper file permissions
8. Disable file editing in wp-config.php:

```php
define('DISALLOW_FILE_EDIT', true);
```

---

## ✅ Post-Migration Checklist

- [ ] Test all pages and links
- [ ] Verify media files load correctly
- [ ] Check contact forms functionality
- [ ] Test payment gateways (if applicable)
- [ ] Configure backups
- [ ] Set up monitoring
- [ ] Update DNS records if needed
- [ ] Configure caching
- [ ] Test mobile responsiveness
