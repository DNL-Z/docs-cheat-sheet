# 🔴 Laravel

An elegant PHP framework for web artisans, providing expressive syntax and powerful tools for building modern web applications.

## 📑 Table of Contents

- [🚀 Getting Started](#-getting-started)
  - [Create New Project](#create-new-project)
  - [Start Development Server](#start-development-server)
  - [Project Information](#project-information)
- [⚙️ Configuration](#-configuration)
  - [Environment Configuration](#environment-configuration)
  - [Generate Application Key](#generate-application-key)
  - [Cache Configuration](#cache-configuration)
- [🗄️ Database & Migrations](#-database--migrations)
  - [Create Migration](#create-migration)
  - [Run Migrations](#run-migrations)
  - [Rollback Migrations](#rollback-migrations)
  - [Fresh Migration](#fresh-migration)
  - [Seed Database](#seed-database)
- [🎨 Models & Eloquent](#-models--eloquent)
  - [Create Model](#create-model)
  - [Mass Assignment](#mass-assignment)
  - [Eloquent Relationships](#eloquent-relationships)
- [🎯 Controllers](#-controllers)
  - [Create Controller](#create-controller)
  - [Resource Controller](#resource-controller)
- [🛣️ Routing](#-routing)
  - [View Routes](#view-routes)
  - [Route Caching](#route-caching)
- [🖼️ Views & Blade](#-views--blade)
  - [Blade Templating](#blade-templating)
  - [Clear View Cache](#clear-view-cache)
- [🔐 Authentication](#-authentication)
  - [Install Authentication](#install-authentication)
- [📦 Packages & Dependencies](#-packages--dependencies)
  - [Install Dependencies](#install-dependencies)
  - [Update Dependencies](#update-dependencies)
- [🧹 Maintenance & Optimization](#-maintenance--optimization)
  - [Clear All Caches](#clear-all-caches)
  - [Optimize Application](#optimize-application)
  - [Maintenance Mode](#maintenance-mode)
- [🧪 Testing](#-testing)
  - [Run Tests](#run-tests)
  - [Create Test](#create-test)
- [📝 Artisan Console](#-artisan-console)
  - [List All Commands](#list-all-commands)
  - [Create Custom Command](#create-custom-command)

---

## 🚀 Getting Started

### Create New Project

Create a new Laravel project using **Composer**.

```bash
  composer create-project laravel/laravel project-name
```

Or using the **Laravel installer**:

```bash
  composer global require laravel/installer
  laravel new project-name
```

### Start Development Server

Start the built-in PHP development server on `http://localhost:8000`.

```bash
  php artisan serve
```

Start on a specific **host and port**:

```bash
  php artisan serve --host=127.0.0.1 --port=8080
```

### Project Information

Display information about the Laravel installation and environment.

```bash
  php artisan about
```

---

## ⚙️ Configuration

### Environment Configuration

Laravel uses the **`.env`** file for environment-specific configuration. Copy the example file:

```bash
  cp .env.example .env
```

### Generate Application Key

Generate a new application key for encryption (required for new projects).

```bash
  php artisan key:generate
```

### Cache Configuration

Cache all configuration files for better performance in production.

```bash
  php artisan config:cache
```

Clear the configuration cache:

```bash
  php artisan config:clear
```

---

## 🗄️ Database & Migrations

### Create Migration

Create a new **migration** file to define database schema changes.

```bash
  php artisan make:migration create_users_table
```

Create a migration for an **existing table**:

```bash
  php artisan make:migration add_column_to_users_table --table=users
```

### Run Migrations

Execute all pending migrations to update the database schema.

```bash
  php artisan migrate
```

### Rollback Migrations

Rollback the **last batch** of migrations:

```bash
  php artisan migrate:rollback
```

Rollback a **specific number** of migrations:

```bash
  php artisan migrate:rollback --step=3
```

Rollback **all** migrations:

```bash
  php artisan migrate:reset
```

### Fresh Migration

Drop all tables and re-run all migrations (destructive operation).

```bash
  php artisan migrate:fresh
```

Drop all tables, re-run migrations, and **seed** the database:

```bash
  php artisan migrate:fresh --seed
```

### Seed Database

Populate the database with test data using **seeders**.

```bash
  php artisan db:seed
```

Run a **specific seeder**:

```bash
  php artisan db:seed --class=UserSeeder
```

Create a new **seeder**:

```bash
  php artisan make:seeder UserSeeder
```

---

## 🎨 Models & Eloquent

### Create Model

Create a new **Eloquent model** for database interaction.

```bash
  php artisan make:model User
```

Create a model with a **migration**:

```bash
  php artisan make:model User -m
```

Create a model with **migration, controller, and factory**:

```bash
  php artisan make:model User -mcf
```

Create a model with **all resources** (migration, factory, seeder, controller):

```bash
  php artisan make:model User --all
```

### Mass Assignment

Define which attributes can be mass-assigned in your model using `$fillable` or `$guarded`.

```php
// Specify fillable attributes
protected $fillable = ['name', 'email', 'password'];

// Or guard specific attributes
protected $guarded = ['id', 'admin'];
```

### Eloquent Relationships

Define relationships between models:

```php
// One to Many
public function posts() {
    return $this->hasMany(Post::class);
}

// Belongs To
public function user() {
    return $this->belongsTo(User::class);
}

// Many to Many
public function roles() {
    return $this->belongsToMany(Role::class);
}
```

---

## 🎯 Controllers

### Create Controller

Create a new **controller** class to handle application logic.

```bash
  php artisan make:controller UserController
```

### Resource Controller

Create a controller with **resourceful methods** (index, create, store, show, edit, update, destroy).

```bash
  php artisan make:controller UserController --resource
```

Create a resource controller with a **specific model**:

```bash
  php artisan make:controller UserController --resource --model=User
```

---

## 🛣️ Routing

### View Routes

List all registered routes in your application.

```bash
  php artisan route:list
```

Filter routes by **name**:

```bash
  php artisan route:list --name=user
```

Filter routes by **method**:

```bash
  php artisan route:list --method=GET
```

### Route Caching

Cache routes for faster route registration (production optimization).

```bash
  php artisan route:cache
```

Clear the route cache:

```bash
  php artisan route:clear
```

---

## 🖼️ Views & Blade

### Blade Templating

Laravel's **Blade** templating engine provides powerful features for building views.

```php
// Layout inheritance
@extends('layouts.app')

// Section definition
@section('content')
    <h1>Welcome</h1>
@endsection

// Include partials
@include('partials.header')

// Conditional rendering
@if($user)
    <p>Hello, {{ $user->name }}</p>
@endif

// Loops
@foreach($users as $user)
    <p>{{ $user->name }}</p>
@endforeach
```

### Clear View Cache

Clear compiled Blade view files.

```bash
  php artisan view:clear
```

Cache all Blade views for better performance:

```bash
  php artisan view:cache
```

---

## 🔐 Authentication

### Install Authentication

Install Laravel's authentication scaffolding using **Breeze** (recommended for new projects):

```bash
  composer require laravel/breeze --dev
  php artisan breeze:install
  npm install && npm run dev
  php artisan migrate
```

Or use **Laravel UI** for Bootstrap/Vue/React scaffolding:

```bash
  composer require laravel/ui
  php artisan ui bootstrap --auth
  npm install && npm run dev
  php artisan migrate
```

---

## 📦 Packages & Dependencies

### Install Dependencies

Install PHP dependencies from `composer.json`:

```bash
  composer install
```

Install JavaScript dependencies from `package.json`:

```bash
  npm install
```

### Update Dependencies

Update all Composer dependencies:

```bash
  composer update
```

Update specific package:

```bash
  composer update vendor/package
```

---

## 🧹 Maintenance & Optimization

### Clear All Caches

Clear all application caches (config, route, view, cache):

```bash
  php artisan optimize:clear
```

Or clear them individually:

```bash
  php artisan config:clear
  php artisan route:clear
  php artisan view:clear
  php artisan cache:clear
```

### Optimize Application

Cache configuration, routes, and views for production:

```bash
  php artisan optimize
```

### Maintenance Mode

Enable maintenance mode (displays a maintenance page to users):

```bash
  php artisan down
```

Enable maintenance mode with a **secret bypass token**:

```bash
  php artisan down --secret="my-secret-token"
```

Disable maintenance mode:

```bash
  php artisan up
```

---

## 🧪 Testing

### Run Tests

Run all tests using **PHPUnit**:

```bash
  php artisan test
```

Or use PHPUnit directly:

```bash
  ./vendor/bin/phpunit
```

Run tests with **coverage**:

```bash
  php artisan test --coverage
```

### Create Test

Create a new **feature test**:

```bash
  php artisan make:test UserTest
```

Create a **unit test**:

```bash
  php artisan make:test UserTest --unit
```

---

## 📝 Artisan Console

### List All Commands

Display all available Artisan commands.

```bash
  php artisan list
```

Get help for a **specific command**:

```bash
  php artisan help migrate
```

### Create Custom Command

Create a new custom Artisan command.

```bash
  php artisan make:command SendEmails
```

The command will be created in `app/Console/Commands/` and can be registered in `app/Console/Kernel.php`.
