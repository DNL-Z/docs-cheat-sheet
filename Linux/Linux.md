# LINUX - SHELL

## Basics

## Retourner au répertoire de l’utilisateur / à la racine

```bash
cd ~
cd /
```

## Lister tous les « process status »

```bash
ps
```

## Lister les fichiers & les fichiers cachés / tri

```bash
ls -la
tree -d
```

$
tree -I 'node_modules'

## Créer un fichier vide

```bash
touch <name_file>
```

## Ecrire / créer dans le fichier

```bash
nano <name_file>
```

## Créer un dossier vide

```bash
mkdir <name_directory>
```

## Créer un dossier d’arborescence

```bash
mkdir -p 1/3/6/2/6/8
```

## Copier des fichiers ou des répertoires

```bash
cp <source> <directory>
```

## Renommer ou déplacer un fichier ou un dossier

```bash
mv <source> <directory>
```

## Créer des liens durs et liens symboliques

```bash
ln <source> <directory>
```

## Supprimer un fichier

```bash
rm <file_or_directory>
```

## Effacer un chemin/dossier

```bash
rmdir /tmp/<name_directory>
```

## Effacer un dossier et tout le contenu récursivement

(remove directories and their contents recursively : -r, -R, --recursive)

```bash
rm -r /tmp/<folder_name>
```

## Trouver un fichier

```bash
find / -name <nom_fichier> (-print)
```

## Lister les répertoires /etc et /bin

```bash
ls /etc /bin
```

## Lister le contenu

```bash
ls /etc > tmp/configurations.log
```

## Lister avec une majuscule dans /etc

```bash
ls /etc/[A-Z]*
ls /etc |grep [A-Z]*
```

## Créer un dossier dans le répertoire de l’utilisateur

```bash
mkdir ~root/temporary_directory
```

## Savoir le chemin actuel

```bash
pwd
```

sort
 => sort lines of text files

grep
 =>
print lines matching a pattern

cut
 =>
remove sections from each line of files

## SSH

GCP
 = Google Cloud Platform

## Se connecter à SSH de GCP

```bash
ssh danylo_zhalkovskyy@(#IP)->change à chaque démarrage
```

## Se connecter à un serveur avec user@ip

```bash
ssh id@62.39.143.50
ssh -i ~.ssh/id_rsa_prod admin_web@198.168.10.4
```

## Secure Copy Protocol

## Transférer / Récupérer un répertoire distant en local (-r pour récursive, c’est à dire tout le dossier)

$
scp -r utilisateur@monserveur.com:/chemin/du/repertoire/distant(source) /chemin/du/repertoire/local(destination)

## Transférer / Récupérer un répertoire local en distant

```bash
scp -r nom/du/dossier/sur/mon/mac user@ip:/nom/du/dossier/sur/mon/instance
```

## Compressions / Décompression

## Décompresser un fichier en BZ

```bash
bzcat access.log.bz2
```

## Décompresser un fichier en GZIP

```bash
gzip access.log.gz
```

## Décompresser un fichier en TGZ

$
tar xzvf <nom_archive>.tar.gz

## Compresser un fichier en TAR.GZ

$
tar czvf <nom_archive>.tar.gz <nom_rep>

## Droits d’accès

		r
 : droit de lecture (read) =
4

		w
 : droit d'écriture (write) =
2

		x
 : droit d'exécution (execute) =
1

## Changer les droits d’un fichier

```bash
chmod 117 oss.txt
```

## Rendre un script exécutable

```bash
chmod +x <script.sh>
```

## Scripts

## Exécuter un script

```bash
./<script.sh>
```

## Déboggage du script

```bash
bash -x <script.sh>
```

## Donner le droit d’exécution pour l’utilisateur au fichier script.sh

```bash
chmod u+x script.sh
```

## Changer les droits du script

```bash
chmod u+x, g+x, o-x script.sh
```

## Changer le groupe en « Ubuntu », pour tous les fichiers du répertoire /src dans le répertoire de l’utilisateur

```bash
chown :ubuntu ~/src
```

## Pour changer les droits d’accès :

```bash
sudo chmod -R 775 /folder_name
```

## Pour changer le proprietaire/groupe :

```bash
sudo chown -R proprietaire:groupe /folder_name
```

## Signes mathématiques pour les script

-lt => <
-le => =<
-gt => >
-ge => =>
-eq => =

## Afficher les 100 premières lignes du fichier <listing.csv.bz2>

```bash
bzcat listing.csv.bz2 | head -100
bzcat listing.csv.bz2 | head -n 100
```

## Top 100 croissant du nombre d’occurrences uniques du 6ème champ du fichier nasa.tsv

```bash
cut -f 6 nasa.tsv | sort | uniq -c | sort | tail 5
```

## Compter le nombre d’occurrence de chaque date et heure de création uniques du répertoire /dev

```bash
ls -l /dev | cut -c 36-47 | sort | unic cachés
```

## Générer une clé SSH RSA de 1024

```bash
ssh-keygen -t rsa -b 1024 -f ~./ssh/id_rsa_eval -N protected
```

## Pour les top 5 articles du log

```bash
cat 01-Oct.log | cut -d " " -f 7 | grep article | sort | uniq -c | sort -n | tail -n 5
```

## Trier les fichiers

```bash
ls -l a* b* c* = ls -l [abc]*
ls -l fi??[^l]* = fi[cl][he][^l]*
```

## Lister les fichiers contenant un chiffre

```bash
ls /var/log | grep [O-9]
ls /var/log/*[O-9]*
```
