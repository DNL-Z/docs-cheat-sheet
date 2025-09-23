# DOCKER

### Version

```bash
  docker --version
```

### Créer un container « ubuntu »

```bash
  docker container run -it ubuntu bash
```

### Lister les containers tous / allumés

```bash
  docker container ls -a
  docker container ps
```

### Lister les images

```bash
  docker image ls -a
```

### Renommer un container

```bash
  docker rename « name_my_container » « my_new_name_container »
```

### Supprimer un des container

```bash
  docker container rm « name / id »
```

### Supprimer des containers, les images, les réseaux non utilisés, (-a) pour tous (all)

```bash
  docker system prune -a
```

### Supprimer des images non utilisées, (-a) pour tout (all)

```bash
  docker images purge
```

### Commande à vérifier (???)

```bash
  docker-compose down --rmi all -v --remove-orphans
```

### Lancer mon docker-compose.yml

```bash
  docker-compose up -d
```

### Build mon docker-compose.yml

```bash
  docker-compose up --build
```

### Arrêter / supprimer le container ou docker-compose lancé

```bash
  docker container stop « id »
```

```bash
  docker-compose stop « id »
  docker-compose down « id »
```

### Installer « lsb-release »

```bash
  apt-get install -y lsb-release
```

### Voir lsb

```bash
  lsb_release -a
```

### Installer nginx

```bash
  apt-get install -y ngnix
```

### Voir nginx

```bash
  ngnix -v
```

### Lancer en local

```bash
  docker container run -d --rm -p 8080:80 --name web_1 nginx:1.14
```

OR

```bash
  docker start « name_my_container »
```

-d
 → pour détacher le conteneur du processus principal de la console
(cela permet de continuer à utiliser la console pendant que votre conteneur tourne sur un autre processus)

-t
 → permet de donner un nom à votre image **Docker**

### Lancer en local avec une page personnalisée avec le chemin indiqué

```bash
  docker container run -d --rm -p 8080:80 -v /Users/vtch_zvtn/Dev/Docker/docker-exercice-1/docker-volume/:/usr/share/nginx/html --name dnl_2 nginx:1.14
```

### Créer un network (qui permet de faire le lien entre 2 ou + de containers)

```bash
  docker network create « name_my_container »
```

### Pour trouver le chemin (???)

```bash
  docker container … $(pwd)/…
```

### Lancer Jenkins

(si l’image existe)

```bash
  docker run -it -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins
```

### Lancer un bash du container

```bash
  docker exec -ti « name_my_container » bash
```

OR

```bash
  docker container start -ia « name_my_container »
```

### Lancer le bash de mon container php-fpm

```bash
  docker-compose exec (--user=root) php-fpm bash
```

### Créer une image personnalisée à partie d’un Dockerfile (dans le répertoire courant)

```bash
  docker build -t « image_name » .
```

OR
(???)

```bash
  docker image build -t « image_name » .
```

---

### Dockerfile

**FROM**
 qui vous permet de définir l'image source

**RUN**
 qui vous permet d’exécuter des commandes dans votre conteneur

**ADD**
 qui vous permet d'ajouter des fichiers dans votre conteneur

**WORKDIR**
 qui vous permet de définir votre répertoire de travail

**EXPOSE**
 qui permet de définir les ports d'écoute par défaut

**VOLUME**
 qui permet de définir les volumes utilisables

**CMD**
 qui permet de définir la commande par défaut lors de l’exécution de vos conteneurs **Docker**

---

### docker-compose.yml

**image**
 qui permet de spécifier l'image source pour le conteneur

**build**
 qui permet de spécifier le Dockerfile source pour créer l'image du conteneur

**volume**
 qui permet de spécifier les points de montage entre le système hôte et les conteneurs

**restart**
 qui permet de définir le comportement du conteneur en cas d'arrêt du processus

**environment**
 qui permet de définir les variables d’environnement

**depends_on**
 qui permet de dire que le conteneur dépend d'un autre conteneur

**ports**
 qui permettent de définir les ports disponibles entre la machine host et le conteneur

---
