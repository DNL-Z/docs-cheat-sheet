# 🎼 Symfony

PHP framework for building modern web applications with elegant architecture and reusable components.

## 📑 Table of Contents

- [📦 Composer](#-composer)
  - [Update Composer](#update-composer)
  - [Update Project Dependencies](#update-project-dependencies)
  - [Install Dependencies](#install-dependencies)
  - [View All Dependencies](#view-all-dependencies)
- [🧩 Symfony Flex & Recipes](#-symfony-flex--recipes)
  - [Logger Recipe](#logger-recipe)
  - [Twig Template Engine](#twig-template-engine)
  - [Annotations Recipe](#annotations-recipe)
  - [Debug Toolbar](#debug-toolbar)
  - [Doctrine ORM](#doctrine-orm)
  - [Maker Bundle](#maker-bundle)
- [🚀 Project Setup](#-project-setup)
  - [Create Web Project](#create-web-project)
  - [Create Microservice/API Project](#create-microserviceapi-project)
  - [Create Traditional Web Application](#create-traditional-web-application)
- [🛠️ Console Commands](#-console-commands)
  - [Console Information](#console-information)
  - [Project Information](#project-information)
  - [Start Development Server](#start-development-server)
  - [Clear Cache](#clear-cache)
- [📐 Entity Management](#-entity-management)
  - [Create Entity](#create-entity)
  - [Create Migration](#create-migration)
- [🎨 Asset Management](#-asset-management)
  - [Generate Assets](#generate-assets)
  - [Watch Assets](#watch-assets)
- [💾 Doctrine Commands](#-doctrine-commands)
  - [View Doctrine Commands](#view-doctrine-commands)
  - [Create Database](#create-database)
  - [Run Migrations](#run-migrations)
  - [Verify Schema Update](#verify-schema-update)
  - [Update Database Schema](#update-database-schema)
  - [Generate Migration Diff](#generate-migration-diff)
- [📚 Annotations Reference](#-annotations-reference)

---

## 📦 Composer

### Update Composer

Update the **Composer** tool itself to the latest version.

```bash
  composer self-update
```

### Update Project Dependencies

Update all project dependencies to their latest versions according to `composer.json` constraints.

```bash
  composer update
```

### Install Dependencies

Install dependencies from an existing project based on `composer.lock`.

```bash
  composer install
```

### View All Dependencies

Display all installed dependencies and their versions.

```bash
  composer show
```

---

## 🧩 Symfony Flex & Recipes

**Symfony Flex** is a Composer plugin that automates the most common tasks in Symfony applications. It allows you to add new components easily through recipes.

### Logger Recipe

Install the **Logger** component to write log files tracking application behavior - essential for debugging production applications.

```bash
  composer require logger
```

### Twig Template Engine

**Twig** is used to dynamically display HTML page content with a powerful templating syntax.

```bash
  composer require twig
```

### Annotations Recipe

Install **Annotations** support to use various types of annotations, including route definitions.

```bash
  composer require annotations
```

### Debug Toolbar

Install the **Debug Toolbar** that appears at the bottom of the page in development mode.

```bash
  composer require debug
```

### Doctrine ORM

Install **Doctrine ORM** for database management and object-relational mapping.

```bash
  composer require orm
```

### Maker Bundle

Install the **Maker Bundle** to generate boilerplate code for entities, controllers, forms, and more.

```bash
  composer require maker
```

---

## 🚀 Project Setup

### Create Web Project

Create a new project using **website-skeleton**, the recommended skeleton for web projects.

```bash
  composer create-project symfony/website-skeleton project_name
```

### Create Microservice/API Project

Create a minimal project for microservices, console applications, or APIs.

```bash
  symfony new project_name
```

### Create Traditional Web Application

Create a full-featured traditional web application with all common bundles.

```bash
  symfony new --full project_name
```

---

## 🛠️ Console Commands

### Console Information

Display all available console commands.

```bash
  php bin/console
```

Or for older Symfony versions:

```bash
  ./app/console
```

### Project Information

Get information about the project (Symfony version, PHP version, kernel, and environment).

```bash
  php bin/console about
```

### Start Development Server

Start the Symfony local development server.

```bash
  symfony server:start
```

### Clear Cache

Clear the application cache. Optionally, specify the environment (default is dev).

```bash
  php bin/console cache:clear
```

For production environment:

```bash
  php bin/console cache:clear --env=prod
```

---

## 📐 Entity Management

### Create Entity

Generate a new Entity class with interactive prompts for properties.

```bash
  php bin/console make:entity EntityName
```

### Create Migration

Generate a migration file based on entity changes.

```bash
  php bin/console make:migration
```

---

## 🎨 Asset Management

### Generate Assets

Generate assets (CSS, JS, images) for production.

```bash
  ./app/console assetic:dump
```

### Watch Assets

Watch for asset modifications and regenerate them automatically on change.

```bash
  ./app/console assetic:watch
```

---

## 💾 Doctrine Commands

### View Doctrine Commands

List all available Doctrine commands.

```bash
  ./app/console doctrine:
```

Or specifically for migrations:

```bash
  ./app/console doctrine:migration
```

### Create Database

Create the database (requires prior configuration in `.env` and `doctrine.yaml` files).

```bash
  php bin/console doctrine:database:create
```

### Run Migrations

Execute all pending migrations to update the database schema.

```bash
  php bin/console doctrine:migrations:migrate
```

Or for older versions:

```bash
  ./app/console doctrine:migrations:migrate
```

### Verify Schema Update

Check what SQL would be executed to update the database schema (dry-run).

```bash
  php bin/console doctrine:schema:update --dump-sql
```

### Update Database Schema

Force update the database schema to match entity definitions.

```bash
  php bin/console doctrine:schema:update --force
```

### Generate Migration Diff

Generate a migration file containing the differences between the current schema and expected schema from entities.

```bash
  ./app/console doctrine:migration:diff
```

---

## 📚 Annotations Reference

### @ORM Annotation

The **@ORM** annotation indicates the table name to which the entity refers. For example, the table `order_customer_order` contains data for the `CustomerOrder` entity.

It also defines the class as an entity for **Symfony** / **Doctrine**. The `repositoryClass` option contains the path to the Repository class.

### Repository Class

The **Repository** class is where you typically group all SQL queries related to an entity. It provides custom methods to retrieve data from the database in an object-oriented way.

---
