# NETWORK 🕸️

## VM’s :

USER /
Login : dnl
Password : J…99%

ROOT /
Login : 
Password : 

MySQL /
Login :
Password : 

## Update & Upgrade Packages

```bash
sudo apt update
sudo apt upgrade
```

## Install Net-Tools

```bash
sudo apt install net-tools
```

## Informations of VM

```bash
ifconfig
```

## Informations sur les adresse IP

```bash
ipcalc « l’adresse IP »
```

## Pour la connexion en SSH sur la VM

Il faut créer un fichier « authorized_keys » dans le dossier .ssh sur la VM, où on ajoute la clé-publique « id_rsa.pub » de notre machine.
=> Passer accès réseau de NAT en Bridge <=

## Première connexion en SSH via ma clé-publique sur la VM avec un user@ip_adress_local

```bash
ssh -i id_rsa.pub root@192.168.1.24
```

## Une fois connecté avec mon user, pour passer en

root

```bash
su -
```

## Modifier le fichier /etc/network/interfaces pour ajouter tous les « network » et ensuite maj avec

```bash
ifup enp0s8
ifup enp0s3
```

## Lister les routes existantes

```bash
route -n
```

## Ajouter une route de la VM (A) -> VM (C) en passant par VM (B)

```bash
route add -net 10.0.4.0/24 gw 10.0.3.5
```

## Ajouter une route de la VM (C) -> VM (A) (pour créer un « aller-retour »)

```bash
route add -net 10.0.3.0/24 gw 10.0.4.4
```

## Pour supprimer une route

```bash
route del -net 10.0.4.0/24 gw 10.0.3.5
```
