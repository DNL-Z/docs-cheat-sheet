# Mise en ligne d’un **WordPress**

1 - Récupérer la DB, en exportant le fichier sur
phpMyAdmin
, si la DB n’est pas trop lourde, sinon :
2 - Se connecte sur FTP

```bash
mysqldump -u root -p db_name > file_name.sql
```

3 - Récupérer le code

```bash
sudo tar cvzf file_name.tar.gz dns_site_name
```

4 - Se connecter sur le nouveau serveur
5 - Importer la bdd

```bash
mysql -u phpmyadmin -p db_name < file_name.sql
```

6 - Importer le code, là où il faut qu’il se trouve

```bash
sudo tar xvzf file_name.tar.gz
```

7 - Changer le MDP dans
/wp-config
 de l’ancien site
8 - Mettre le Search-Redirection (pour changer les liens) ou les changer dans
/wp_options
9 - Installer des plugins de sécurité
