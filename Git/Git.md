# GIT

### Configuration file 

**.gitconfig**

> [user]
>
>> name = DNL <br>
>> email = danylo.zhalkovskyy@icloud.com <br>
>
> [core]
>
>> autocrlf = input <br>
>
> [pull]
>
>> ff = only <br>
>> rebase = true

---

### Générer les clés « id_rsa » et « id_rsa.pub » dans le dossier ~/.ssh

```bash
  ssh-keygen -t rsa
```

### Cloner un repository en local

```bash
  git clone « address SSH ou HTTPS »
```

### Afficher l'état des fichiers : modifiés, ajoutés, supprimés

```bash
  git status
```

### Lister toutes les branch

```bash
  git branch -a
```

### Supprimer une branch

```bash
  git branch -d « branch_name »
```

### Voir les modifications faites d’un fichier

```bash
  git diff « file_name »
```

### Ajouter le fichier en vue d'un commit

```bash
  git add « file_name »
```

### Annuler le fichier add

```bash
  git reset « file_name »
```

### La commande magique, qui est le fonctionnement de git add en interactif
Il est possible de sélectionner les lignes exactes que tu veux commiter, et pas forcément la totalité du fichier.

```bash
  git add -i
```

### Annuler les modifications d’un fichier

```bash
  git checkout « file_name »
```

### Supprimer le fichier en vue d'un commit
Si je supprime un fichier manuellement, mais qu’il est déjà sur repository git, ça ne va pas forcément le supprimer.

```bash
  git rm « file_name »
```

### Mettre en ligne les modifications

```bash
  git add « file_name » OR « . »
  git commit -m « initial commit »
  git push
```

### Modifier un commit local

```bash
  git commit —amend
```

### Annuler le dernier commit (?)

```bash
  git reset HEAD « file_name »
  git reset HEAD^1
```

### Push un projet local vers un repository

La clé publique **~/.ssh/id_rsa.pub**, doit être enregistrer sur le compte **Git**.

```bash
  git init --initial-branch=master OR main
```

```bash
  git remote add origin « url_ssh_repository_project »
  git add .
  git commit -m « Initial commit »
  git push -u origin master OR main
```

### Set up GitHub Token

```bash
  git remote set-url origin https://<githubtoken>@github.com/<username>/<repositoryname>.git
```

### Connaître la branch sur laquelle j’y suis

```bash
  git branch
```

### Créer une branch (autre que master/main)

```bash
  git branch « branch_name »
```

### Se connecter sur une autre branch

```bash
  git checkout « branch_name »
```
```bash
  git checkout -b « branch_name » (?)
```

### Stocker les fichiers modifier en local, pour effectuer d’autres tâches

```bash
  git stash
```

### Supprimer les fichiers stashed

```bash
  git stash clear
```

### Lister les fichiers stashed

```bash
  git stash list
```

### Montrer les fichiers stashed

```bash
  git stash show
```

### Récupérer ensuite les modifications stashed

```bash
  git stash pop
```

### Récupérer les derniers commits sur la branche courante

```bash
  git pull
```

 git pull = git fetch + git merge

### Récupérer les modifs de la branch master, si je suis sur une autre branche

```bash
  git pull origin master
```

### Afficher les derniers commits

```bash
  git log
```

### Afficher un commit spécifique

```bash
  git show
```

### Récupérer les branches et leurs commits distants (avant de merge)

```bash
  git fetch
```

### Merge les branches

```bash
  git checkout master OR main
 ```

```bash
  git pull origin master
  git merge « branch_name »
  git push origin master
```

### Merge les branches avec des conflits

```bash
  git checkout « branch_name_to_merge »
```

```bash
  git pull origin master
```

=> à ce moment il y a des conflits, donc il faut les régler + check si ça fonctionne (!!!)

```bash
  git add .
  git commit -m « merge master »
  git push
```

=> à ce moment là « branch_name_to_merge » devient à jour avec master
=> valider la PR + merge

### Rebase les commits locaux au-dessus de origin/dev, conservant les commits locaux

```bash
  git rebase origin/dev
```

### Réinitialise complètement la branche locale pour qu'elle corresponde exactement à origin/dev, supprimant les commits locaux

```bash
  git reset --hard origin/dev
```
