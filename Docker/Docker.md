# 🐳 DOCKER

**Docker** helps developers build, share, run, and verify applications anywhere — without tedious environment configuration or management.

## 📑 Table of Contents

- [📋 General Information](#-general-information)
- [📦 Container Management](#-container-management)
- [🖼️ Image Management](#-image-management)
- [🗂️ Volume Management](#-volume-management)
- [🌐 Network Management](#-network-management)
- [🧹 Cleanup](#-cleanup)
- [🐳 Docker Compose](#-docker-compose)
- [🚀 Practical Examples](#-practical-examples)
- [📄 Dockerfile - Main Directives](#-dockerfile---main-directives)
- [📝 docker-compose.yml - Main Directives](#-docker-composeyml---main-directives)
- [🛠️ System Utilities](#-system-utilities-inside-a-container)

---

## 📋 General Information

### Version

```bash
  docker --version
```

---

## 📦 Container Management

### Create an "ubuntu" container

```bash
  docker container run -it ubuntu bash
```

### List containers

```bash
  # All containers
  docker container ls -a

  # Only active containers
  docker container ps
```

### Rename a container

```bash
  docker rename <name_my_container> <my_new_name_container>
```

### Start a container

```bash
  docker start <name_my_container>
```

### Stop a container

```bash
  docker container stop <container_id>
```

### Remove a container

```bash
  docker container rm <name_or_id>
```

### Launch bash in a container

```bash
  docker exec -ti <container_name> bash
```

OR

```bash
  docker container start -ia <container_name>
```

### View container logs

```bash
  docker logs <container_name>
  docker logs -f <container_name>  # follow logs in real-time
  docker logs --tail 100 <container_name>  # display last 100 lines
```

### View container stats in real-time

```bash
  docker stats
  docker stats <container_name>
```

### Inspect a container

```bash
  docker inspect <container_name>
```

### Retrieve IP address of a container

```bash
  docker inspect <container-name> | grep IPAddress
```

---

## 🖼️ Image Management

### List images

```bash
  docker image ls -a
```

### Create a custom image from a Dockerfile

```bash
  docker build -t <image_name> .
```

OR

```bash
  docker image build -t <image_name> .
```

### Remove unused images

```bash
  docker image prune -a
```

---

## 🗂️ Volume Management

```bash
  # List volumes
  docker volume ls

  # Create a volume
  docker volume create <volume_name>

  # Inspect a volume
  docker volume inspect <volume_name>

  # Remove a volume
  docker volume rm <volume_name>

  # Remove all unused volumes
  docker volume prune
```

---

## 🌐 Network Management

### Create a network

```bash
  docker network create <network_name>
```

### List and manage networks

```bash
  # List networks
  docker network ls

  # Inspect a network
  docker network inspect <network_name>

  # Remove a network
  docker network rm <network_name>

  # Remove all unused networks
  docker network prune
```

---

## 🧹 Cleanup

### Remove unused containers, images, networks

```bash
  docker system prune -a
```

---

## 🐳 Docker Compose

### Launch docker-compose.yml

```bash
  docker compose up -d
```

### Build docker-compose.yml

```bash
  docker compose up --build
```

### Stop / Remove services

```bash
  docker compose stop <service_name>
  docker compose down
```

### Completely remove (containers, images, volumes, orphan networks)

```bash
  docker compose down --rmi all -v --remove-orphans
```

### View docker compose logs

```bash
  docker compose logs
  docker compose logs -f <service_name>
```

### Restart services

```bash
  docker compose restart
  docker compose restart <service_name>
```

### Pull images

```bash
  docker compose pull
```

### Launch bash in a service

```bash
  docker compose exec (--user=root) php-fpm bash
```

---

## 🚀 Practical Examples

### Launch nginx locally

```bash
  docker container run -d --rm -p 8080:80 --name web_1 nginx:1.14
```

**Options:**
- `-d` : detach container from a main console process
- `-t` : allows naming your Docker image
- `--rm` : automatically remove container on stop
- `-p` : map ports (host:container)

### Launch nginx with a custom page

```bash
  docker container run -d --rm -p 8080:80 -v /path/to/your/html:/usr/share/nginx/html --name web_custom nginx:1.14
```

### Use the current directory in a command

```bash
  docker container run -v $(pwd):/app <image_name>
```

### Launch Jenkins

```bash
  docker run -it -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins
```

### Import SQL file into Postgres

```bash
  docker exec -i <container-name> psql -U <username> -d <database_name> < init.sql
```

---

## 📄 Dockerfile - Main Directives

**FROM**
 → define the source image

**RUN**
 → execute commands in your container

**ADD** / **COPY**
 → add files to your container

**WORKDIR**
 → define your working directory

**EXPOSE**
 → define default listening ports

**VOLUME**
 → define usable volumes

**CMD**
 → define default command when executing the container

**ENTRYPOINT**
 → define the main executable of the container

---

## 📝 docker-compose.yml - Main Directives

**image**
 → specify source image for the container

**build**
 → specify source Dockerfile to create the container image

**volumes**
 → specify mount points between a host system and containers

**restart**
 → define container behavior on process stop

**environment**
 → define environment variables

**depends_on**
 → indicate that the container depends on another container

**ports**
 → define available ports between host machine and container

**networks**
 → define networks to which the container belongs

---

## 🛠️ System Utilities (inside a container)

### Install lsb-release

```bash
  apt-get install -y lsb-release
```

### View lsb

```bash
  lsb_release -a
```

### Install nginx

```bash
  apt-get install -y nginx
```

### View nginx

```bash
  nginx -v
```

---
