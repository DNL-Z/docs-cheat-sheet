# 🐍 Python

A comprehensive reference guide for Python development, covering package management, virtual environments, popular frameworks, and libraries.

## 📑 Table of Contents

- [📋 Code Standards](#-code-standards)
- [🚀 Running Python](#-running-python)
  - [System Python](#system-python)
  - [Homebrew Python3](#homebrew-python3)
- [📦 Package Management](#-package-management)
  - [Export Package List](#export-package-list)
  - [Install Libraries](#install-libraries)
- [🔧 Virtual Environments](#-virtual-environments)
  - [Python3 Virtual Environment](#python3-virtual-environment)
  - [MiniConda (Anaconda) Virtual Environment](#miniconda-anaconda-virtual-environment)
- [📓 Jupyter Notebook](#-jupyter-notebook)
- [🕷️ Web Scraping with Scrapy](#-web-scraping-with-scrapy)
- [📊 Data Analysis with Pandas](#-data-analysis-with-pandas)
- [🌐 Django Framework](#-django-framework)
  - [Installation](#installation)
  - [Project Setup](#project-setup)
  - [Database Migrations](#database-migrations)
  - [User Management](#user-management)
  - [Django Shell](#django-shell)

---

## 📋 Code Standards

**PEP8** is the standard syntax in Python. It is recommended to follow the **snake_case** naming convention.

---

## 🚀 Running Python

### System Python

```bash
  python
  python -V
```

### Homebrew Python3

```bash
  python3
  python3 -V
```

---

## 📦 Package Management

### Export Package List

Export all installed packages to a requirement file:

```bash
  pip freeze > requirements.txt
```

### Install Libraries

Install libraries from a requirement file:

```bash
  python3 -m pip install -r requirements.txt
```

---

## 🔧 Virtual Environments

### Python3 Virtual Environment

**Create an environment:**

```bash
  python3 -m venv <name-pyenv>
```

**Activate the environment:**

```bash
  source <name-environment>/bin/activate
```

**Deactivate the environment:**

```bash
  deactivate
```

### MiniConda (Anaconda) Virtual Environment

**Create an environment:**

```bash
  conda create --name <env_name> python=3.9
```

**Activate the environment:**

```bash
  conda activate <env_name>
```

**Deactivate the environment:**

```bash
  conda deactivate
```

**List environments:**

```bash
  conda info --envs
```

---

## 📓 Jupyter Notebook

**Install Jupyter Notebook:**

```bash
  pip install notebook
```

**Launch Jupyter Notebook:**

```bash
  jupyter notebook
```

---

## 🕷️ Web Scraping with Scrapy

**Install Scrapy:**

```bash
  pip install scrapy
```

**Run a Scrapy spider:**

```bash
  scrapy runspider <name-file.py>
  scrapy runspider ocr-scrapy.py -o characters.json
```

---

## 📊 Data Analysis with Pandas

**Install Pandas:**

```bash
  pip install pandas
```

---

## 🌐 Django Framework

### Installation

**Install Django:**

```bash
  pip install django
```

**Install Pillow (image management library):**

```bash
  pip install Pillow
```

### Project Setup

**Create a project:**

```bash
  django-admin startproject <project_name>
```

**Create an app within the project:**

```bash
  django-admin startapp <app_name>
```

**Run the development server:**

```bash
  python manage.py runserver
```

**Template configuration:**

In `settings.py`, change `'DIRS': []` to `'DIRS': [BASE_DIR / "templates"]` to manage templates.

### Database Migrations

**Create a migration:**

```bash
  python manage.py makemigrations
```

**Execute migrations:**

```bash
  python manage.py migrate
```

### User Management

**Create a new superuser:**

```bash
  python manage.py createsuperuser
```

### Django Shell

**Launch the Django shell:**

```bash
  python manage.py shell
```

**Example commands in the Django shell:**

```python
from photos.models import Photo

# Display all data
Photo.objects.all()

# Filter data where status is Published
Photo.objects.filter(status=Photo.PUBLISHED)
```
