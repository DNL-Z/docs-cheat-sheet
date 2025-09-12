# **Python**

PEP8
 is the standard syntax in **Python**.
It is recommended to follow the
snake_case
 naming convention.

## Lancer python (système)

```bash
python
python -V
```

## Lancer python3 (homebrew)

```bash
python3
python3 -V
```

## Exporter la liste des paquets

```bash
pip freeze > requirements.txt
```

## Installer les librairies

$
python3 -m pip install -r requirements.txt

---

## Environnement virtuel avec Python3

## Créer un environnement

```bash
python3 -m venv <name-pyenv>
```

## Activer l'environnement

```bash
source <name-environement>/bin/activate
source ~/Dev/Python/environments/discovery-env/bin/activate
```

## Désactiver l'environnement

```bash
deactivate
```

## Environnement virtuel avec MiniConda (Anaconda)

## Créer un environnement

$
conda create --name <env_name> python=3.9

## Activer l'environnement

```bash
conda activate <env_name>
```

## Désactiver l'environnement

```bash
conda deactivate
```

## Lister les environnements

```bash
conda info --envs
```

---

## Installer Jupyter Notebook

```bash
pip install notebook
```

## Lancer Jupyter Notebook

```bash
jupyter notebook
```

## Installer Scrapy

```bash
pip install scrapy
```

## Utiliser Scrapy dans le web

```bash
scrapy runspider <name-file.py>
scrapy runspider ocr-scrapy.py -o characters.json
```

## Installer Pandas

```bash
pip install pandas
```

---

## Django

## Installer Django

```bash
pip install django
```

## Librairie pour la gestion d'image

```bash
pip install Pillow
```

## Création du projet

```bash
django-admin startproject insta
```

## Création app dans le projet

```bash
django-admin startapp photos
```

## Lancer le serveur

```bash
python manage.py runserver
```

## Creer une migration

```bash
python manage.py makemigration
```

## Executer la migration

```bash
python manage.py migrate
```

## Créer un nouveau user

```bash
python manage.py createsuperuser
```

Changer dans setting.py 
'DIRS': [], par 'DIRS': ["f\BASE_DIR\/templates"] 
pour gérer les templates.

```bash
python manage.py shell
```

## Exemple dans le shell python

from photos.models import Photo

## Affiche tout les données

Photo.objects.all()

## Trie les donnée dont le status es Published

Photo.objects.filter(status=Photo.PUBLISHED)
