# SYMFONY

## **Composer**

## Mettre à jour le **composer**

```bash
composer self-update
```

## Mettre à jour les dépendances du projet

```bash
composer update
```

## Installer les dépendances d’un projet existant

```bash
composer install
```

## Voir toutes les dépendances

```bash
composer show
```

Flex
, c’est un
outil

**Symfony**
 qui permet d'ajouter des nouvelles briques

## Installer la recette

Logger
, qui permet d'écrire dans des fichiers log ce qu'il se passe dans votre application
=> indispensable pour débogguer une application en production

```bash
composer require logger
```

## Template

**Twig**
, sert d’afficher le contenu de votre page **HTML** de façon dynamique

```bash
composer require twig
```

## Recette

Annotations
, qui permet d'utiliser plusieurs types d'annotations
=> dont celle qui nous intéresse pour définir les routes

```bash
composer require annotations
```

## Barre de debug, la barre en bas de page

```bash
composer require debug
```

## ???

```bash
composer require orm
```

## ???

```bash
composer require maker
```

---

## Créer un projet

website-skeleton
, le squelette recommandé pour faire des projets web

```bash
composer create-project symfony/website-skeleton nom_projet
```

## Créer

microservice, console application or API

```bash
symfony new nom_projet
```

## Créer Traditional Web Application

```bash
symfony new --full nom_projet
```

## Infos

```bash
php bin/console
```

```bash
./app/console
```

## Avoir des infos sur le projet (symfony, php version, kernel et l’environnement)

```bash
php bin/console about
```

## Lancer le serveur

```bash
symfony server:start
```

## Créer une Entity=Class

```bash
php bin/console make:entity NomDeMaClass
```

## Créer un bundle (=> ne fonctionne pas ???)

$
php bin/console generate:bundle

## Test d’envoie d’un email (=> s’il y a swift mailer ???)

```bash
./app/console swiftmailer:email:send
```

## Générer les assets (CCS, JS …)

```bash
./app/console assetic:dump
```

## Ecouter si les modifs des assets, alors ils sont régénérés à la volée

```bash
./app/console assetic:watch
```

## Doctrine

## Voir les commandes existantes avec Doctrine

```bash
./app/console doctrine:
```

```bash
./app/console doctrine:migration
```

## Créer Database (il faut configurer avant les fichiers .env et doctrine.yaml)

```bash
php bin/console doctrine:database:create
```

## Faire la migration des données

```bash
php bin/console doctrine:migrations:migrate
```

```bash
./app/console doctrine:migrations:migrate
```

## Vérifier la mise à jour de la Database

```bash
php bin/console doctrine:schema:update --dump-sql
```

## Mettre à jour la Database

```bash
php bin/console doctrine:schema:update --force
```

## Si je modifie les « Entity », cela va créer un fichier faisant la différence entre mon schema et le schema attendu dans le code

```bash
./app/console doctrine:migration:diff
```

## Vider le cache

```bash
php bin/console cache:clear ( --env=prod )
```

```bash
php bin/console make:migration
```

---

@ORM
 : indique le nom de la table auquel l'entity fait référence (la table order_customer_order contient les données de l'entity CustomerOrder)

@ORM
 : défini la classe CustomerOrder comme une entity pour **Symfony** / Doctrine. Et l'option repositoryClass contient le chemin de la classe Repository.

La classe REPOSITORY est la classe où l'on regroupe généralement toutes les requêtes **SQL** liés à l'entity

---
