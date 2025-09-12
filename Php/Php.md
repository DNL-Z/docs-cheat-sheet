# **PHP**

count()
 — Compte tous les éléments d'un tableau ou quelque chose d'un objet

round()
 — Arrondit un nombre à virgule flottante -> round($resultat, 2), deux nombre après la virgule

rand()
 — Génère une valeur aléatoire -> rand(0, 100)

mt_rand()
 — Génère une valeur aléatoire, par exemple entre 1 et 10 -> mt_rand(1, 10)

ksort()
 — Trie un tableau suivant les clés

unset()
 — Détruit une variable (supprime la valeur assigner à une variable)

trim()
 — Supprime les espacés ou d'autres caractères, en début et fin de chaîne

iconv_strlen()
 — Retourne le nombre de caractères d'une chaîne

empty()
 — Détermine si une variable est vide (donc, à utiliser !empty())

isset()
 — Détermine si une variable est déclarée et est différente de NULL

strpos()
 — Cherche la position de la première occurrence dans une chaîne

strval()
 — Récupère la valeur d'une variable, au format chaîne

strlen()
 — Calcule la taille d'une chaîne

str_repeat()
 — Répète une chaîne

str_replace()
 — Remplace toutes les occurrences dans une chaîne

substr()
 — Retourne un segment de chaîne

strtoupper()
 — Renvoie une chaîne en majuscules

trim()
 — Supprime les espaces (ou d'autres caractères) en début et fin de chaîne

is_dir()
 — Indique si le fichier est un dossier

scandir()
 — Liste les fichiers et dossiers dans un dossier

unlink()
 — Supprime un fichier

htmlspecialchars()
 — Convertit les caractères spéciaux en entités **HTML**

nl2br()
 — Insère un retour à la ligne **HTML** à chaque nouvelle ligne

is_null()
 — Indique si une variable vaut NULL

method_exists()
 — Vérifie si la méthode existe pour une classe

L'opérateur ternaire
 peut être considéré comme une instruction en ligne if . 
Il se compose de trois parties.
L'operator
et
 deux résultats
 :

$value = <operator> ? <true value> : <false value>
$value = <operator> ?: <false value> (raccourci)
Si <operator> est true, alors on affiche la valeur de <true value>, sinon <false value>

## POO

Une
classe
 est une
entité
(
Entity
)
 regroupant des variables et des fonctions. 
Chacune de ces fonctions aura accès aux variables de cette entité.
Les variables et les fonctions stockées dans la classe : 
un
attribut
 désigne une
variable
 et une
méthode
 désigne une
fonction
.
Une
instance
, c'est tout simplement le résultat d'une instanciation. Une instanciation, c'est le fait d'instancier une classe. 
Instancier une classe, c'est se servir d'une classe, afin qu'elle nous crée un objet. En gros, une
instance
 est un
objet
.

Le constructeur __construct()
Sert à exécuté dès la création de l'objet et par conséquent, aucune valeur ne doit être retournée, même si ça ne génèrera aucune erreur.
Il sert à créer un objet pour lequel vous avez besoin d'initialiser les attributs dès sa création, sans connaitre leurs valeurs à l'avance.

Visibilité d'un attribut
ou
 d'une méthode

public
 : si un attribut ou une méthode est public, alors on pourra y avoir accès depuis n'importe où, depuis l'intérieur de l'objet (dans les méthodes qu'on a créées), comme depuis l'extérieur

private
 : impose quelques restrictions. On n'aura accès aux attributs et méthodes seulement depuis l'intérieur de la classe

protected
 : (voir avec la notion d’héritage)

Une
 constante de classe
 est une sorte d'attribut appartenant à la classe, dont la valeur ne change jamais.

Les attributs statiques
 et
les méthodes statiques

appartient à la classe
 et
non à un objet
.
Et
tous les objets auront accès à cet attribut et cet attribut aura la même valeur pour tous les objets.

Exemples :

	private static $_texteADire = 'Je vais tous vous tuer !';

	public static function parler() \ \

On n'accède pas à un attribut statique avec $this, mais avec
self::
.

L’opérateur de résolution de portée « :: »
Il permet d'accéder à un élément d’une classe.

self ::
, ce qui veut dire « moi-même » <=> à la classe.
Un
getter
 est une méthode chargée de
renvoyer la valeur d'un attribut
.
Un
setter
 est une méthode
chargée
 d'assigner une valeur à un attribut
 en vérifiant son intégrité.

Abstraction de classes

**PHP** 5 introduit
les concepts de classes
 et
de méthodes abstraites
. Les classes définies comme abstraites
ne peuvent pas être instanciées
.
Et toute classe contenant au moins une méthode abstraite, doit elle-aussi être abstraite.
Les méthodes définies comme abstraites déclarent simplement la signature de la méthode - elles ne peuvent définir son implémentation.

L’hydratation : public function hydrate() \

Quand on vous parle d'hydratation, c'est qu'on parle d'« objet à hydrater ». 

Hydrater un objet
, c'est tout simplement lui apporter ce dont il a besoin pour fonctionner. 
En d'autres termes plus précis, hydrater un objet revient à
lui fournir des données
 correspondant à ses attributs pour qu'il assigne les valeurs souhaitées à ces derniers. L'objet aura ainsi
des attributs valides
 et
sera en lui-même valide
.

## MySQL

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

L'extension PDO
C’est un outil complet qui permet d'accéder à n'importe quel type de base de données. 

On peut donc l'utiliser pour se connecter aussi bien à MySQL qu'à PostgreSQL ou Oracle.
«
Query
 » en anglais signifie une «
requête
 ».

fetch()
 — Va chercher

Connexion à MySQL
 :

$bdd = new PDO('mysql:host=localhost;dbname=cours_openclassrooms;charset=utf8', 'root', 'root');

Récupération du contenu de la table X
 :

$reponse = $bdd->query('SELECT * FROM X’);

Pour afficher chaque entrée une par une :

while($donnees = $reponse->fetch()) 
\
	echo $donnees['nom'];
\

Pour les requêtes normales :

exec()
 - Exécute une requête **SQL** et retourne le nombre de lignes affectées

Pour les requêtes préparées :

prepare()
 — Prépare une requête à l'exécution et retourne un objet (utiliser pour un formulaire)
execute()
 — Exécute une requête préparée

$reponse->closeCursor();

Fermeture du curseur d'analyse des résultats à chaque fois que vous avez fini de traiter le retour d'une requête.

Afin d'éviter d'avoir des problèmes à la requête suivante.
Cela veut dire qu'on a terminé le travail sur la requête.
