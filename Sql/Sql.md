# MySQL

## Se connecter à une bdd avec MySQL

```bash
mysql -uroot -p
```

## Local mamp

$
/Applications/MAMP/Library/bin/mysql --host=localhost -uroot -proot

## Importer une bdd en .sql dans une bdd

```bash
mysql -u root -ppassword nom_base_de_donnees < nom_fichier.sql
```

## Exporter une bdd dans un fichier .sql

```bash
mysqldump -u root -ppassword nom_base_de_donnees > nom_fichier.sql
```
