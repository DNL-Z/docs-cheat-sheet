# 🏔️ Bedrock

Modern WordPress development stack that helps you get started with the best development tools and project structure.

## 📑 Table of Contents

- [🚀 Project Setup](#-project-setup)
  - [Create a New Project](#create-a-new-project)
  - [Install WordPress with Bedrock](#install-wordpress-with-bedrock)
  - [Create a package.json File](#create-a-packagejson-file)
- [📦 Plugin Management](#-plugin-management)
  - [Install Plugin via Composer](#install-plugin-via-composer)
  - [Development Dependencies](#development-dependencies)
- [💡 Core Concepts](#-core-concepts)

---

## 🚀 Project Setup

### Create a New Project

Initialize a new Bedrock project using Composer:

```bash
  composer create-project roots/bedrock name_project
```

### Install WordPress with Bedrock

Install all dependencies including WordPress core:

```bash
  composer install
```

### Create a package.json File

Initialize npm for frontend dependencies:

```bash
  npm init
```

---

## 📦 Plugin Management

### Install Plugin via Composer

Install WordPress plugins using wpackagist:

```bash
  composer require wpackagist-plugin/plugin_name
```

### Development Dependencies

Install plugins as development dependencies (not needed in production):

```bash
  composer require --dev wpackagist-plugin/plugin_name
```

---

## 💡 Core Concepts

**Bedrock** is a WordPress boilerplate with an improved folder structure, easier configuration, and dependency management via Composer. Key features include:

- Better folder structure with separated web root
- Dependency management with Composer
- Easy WordPress configuration with environment files
- Environment variables with PHP dotenv
- Enhanced security (separated web root and secure passwords)
- Better deployment process with tools like Capistrano

**Directory Structure:**

```
.
├── composer.json          # Manage WordPress and plugins
├── config/               # Configuration files
│   ├── application.php   # Primary config file
│   └── environments/     # Environment-specific configs
├── vendor/              # Composer packages
├── web/                 # Web root (document root)
│   ├── app/            # WordPress content directory
│   │   ├── plugins/    # Plugins
│   │   ├── themes/     # Themes
│   │   └── uploads/    # Uploads
│   ├── wp/             # WordPress core (don't edit)
│   └── index.php       # WordPress entry point
└── .env                # Environment variables
```

**Environment Configuration:**

Create a `.env` file in the project root:

```dotenv
DB_NAME='database_name'
DB_USER='database_user'
DB_PASSWORD='database_password'
DB_HOST='localhost'

WP_ENV='development'
WP_HOME='http://example.test'
WP_SITEURL="${WP_HOME}/wp"
```

---
