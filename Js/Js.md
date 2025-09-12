# **JavaScript**

## Variables

let
 variable is block scoped and can be re-assigned

const
 is block scoped and its reference can’t be re-assigned

var
 can be locally or globally scoped, re-assigned and hoisted

## Variable NULL vs UNDEFINED

undefined
 means a variable has been declared but has not yet been assigned a value (
typeof = undefined
)

null
 is an assignment value. It can be assigned to a variable as a representation of no value (
typeof = object
)

## Primitive

Une
primitive
 (valeur primitive ou structure de donnée primitive) est une donnée qui n'est pas un objet et n'a pas de méthode. En **JavaScript**, il y a 7 types de données primitives:
String
,
Number
,
Boolean
,
Null
,
undefined
,
Symbol
,
Bigint
 (nouveauté d'ECMAScript 2020)

## Operator void

The
void
 operator evaluates the given expression and then returns
undefined

## **Babel**

C’est un transcompilateur **JavaScript** gratuit et open source qui est principalement utilisé pour convertir le code ECMAScript 2015+ en une version rétrocompatible de **JavaScript** pouvant être exécutée par des moteurs **JavaScript** plus anciens

\*HYPERLINK "https://babeljs.io/"https://babeljs.io/

## Parcel

Parcel's **JavaScript** compiler is built on SWC, which handles transpiling **JavaScript**, JSX, and **TypeScript**. On top of SWC, Parcel implements dependency collection, bundling, scope hoisting, tree shaking, **Node** emulation, hot reloading, and more

\*HYPERLINK "https://parceljs.org/"
https://parceljs.org/

---

## Some basics **JavaScript** functions

La
condition à la volée
 avec
l’opérateur logique
 => true
&&
 expression || false
&&
 expression

L'opérateur
ternaire conditionnel
 => condition
?
 exprSiVrai
:
 exprSiFaux

La méthode
concat()
 est utilisée afin de
fusionner un
 ou
plusieurs tableaux
 en les concaténent

La méthode
includes()
 permet de déterminer si
un tableau contient une valeur
 et renvoie
true
 si c'est le cas, sinon
false
La méthode
find()
 renvoie la valeur du
premier élément trouvé
 dans le tableau qui respecte la condition donnée par la fonction de test passée en argument. Sinon, la valeur
undefined
 est renvoyée

La méthode
some()
 teste si au moins un élément du tableau passe le test implémenté par la fonction fournie. Elle renvoie un
booléen
 indiquant le résultat du test
La méthode
sort()

trie
 les éléments d'un tableau, dans ce même tableau, et renvoie le tableau. Le tri s'effectue sur les éléments du tableau convertis en chaînes de caractères et triées selon les valeurs des unités de code UTF-16 des caractères
La méthode
slice()
 renvoie un objet tableau, contenant une copie superficielle (shallow copy) d'une portion du tableau d'origine, la portion est définie par
un indice de début
 et
un indice de fin
 (exclus). Le tableau original ne sera pas modifié
La méthode
splice()

modifie le contenu d'un tableau
 en
retirant des éléments et/ou en ajoutant
 de nouveaux éléments

La méthode
split()

divise une chaîne de caractères
 en une
liste ordonnée de sous-chaînes
, place ces sous-chaînes
dans un tableau
 et retourne le tableau

const
str
 = 'The quick brown fox jumps over the lazy dog.';
const words =
str.split(
' '
)
;
console.log(words[3]);
// expected output: "fox"
La méthode
forEach()
 permet
d'exécuter une fonction donnée
 sur
chaque élément du tableau
La méthode
map()
 permet facilement
d'itérer sur des données
 et de retourner un tableau d'éléments
La méthode
filter()

crée et retourne un nouveau tableau
 contenant tous les éléments du tableau d'origine qui
remplissent une condition déterminée
par la fonction callback

const
words
 = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result =
words.filter(
word => word.length > 6
)
;
console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]
La méthode
reduce()
 applique une fonction qui est un
accumulateur
 et qui traite chaque valeur d'une liste (de la gauche vers la droite) afin de la réduire à
une seule valeur
La
déstructuration
 permet directement de
déclarer une variable
 et de
lui assigner la valeur d'une propriété d'un objet

const
note
 = \
  id: 1,
  title: 'My first note',
  date: '01/01/1970',
\
const \ id, title, date \ =
note
La
syntaxe de décomposition
 «
Spread
 » permet
d'étendre un itérable
 (par exemple une expression de tableau ou une chaîne de caractères) en lieu et place de plusieurs arguments (pour les appels de fonctions) ou de plusieurs éléments (pour les littéraux de tableaux) ou de paires clés-valeurs (pour les littéraux d'objets)

const
tools
 = ['hammer', 'screwdriver']
const
otherTools
 = ['wrench', 'saw']
const allTools = [...
tools
, ...
otherTools
]
console.log(allTools)
// expected output:["hammer", "screwdriver", "wrench", "saw"]
Les
 littéraux de gabarits « `` »
 sont des littéraux de chaînes de caractères permettant
d'intégrer des expressions
. Avec eux, on peut utiliser des chaînes de caractères multi-lignes et des fonctionnalités d'interpolation
// Simple concatenation
let rep = 42;
console.log(
`
La réponse est
$
rep
\`
);

Le
 regex ou expression régulière
 est ce petit bout de code
/^([a-zA-Z ]+)$/
 qui permet, entre autre, de
vérifier le contenu d'une chaîne de caractères

if(! pseudo.match(
/^([a-zA-Z ]+)$/
))
    alert('Pseudo invalide');

---

## Callback

Un
callback
 est simplement une fonction que vous définissez.

Le principe de callback est de la
passer en paramètre
 d’une fonction asynchrone. Une fois que la fonction asynchrone a fini sa tâche, elle va appeler notre fonction
callback
 en lui passant un
résultat
.
Ainsi, le code que nous mettons dans notre fonction
callback
 sera exécuté de manière asynchrone

function salutation(name) \
  alert('Bonjour ' + name);
\
function processUserInput(callback) \
  var name = prompt('Entrez votre nom.');
  callback(name);
\
processUserInput(salutation);

## Promise

L'objet
Promise
, pour « promesse » est utilisé pour réaliser des traitements de façon asynchrone
Tout appel à une fonction définie avec le mot clé
async
 retourne une
Promise
 de la valeur retournée avec
return

Une
Promise
, on peut utiliser sa fonction
.then()
 pour exécuter du code dès que la promesse est résolue, et sa fonction
.catch()
 pour exécuter du code dès qu'une erreur est survenue

---

## Synchrone vs Asynchrone

Si du code
synchrone
 est du code qui s'exécute ligne après ligne en attendant
la fin de l'exécution
 de la ligne précédente, alors on peut facilement en déduire que du code
asynchrone
 va s'exécuter ligne après ligne, mais la ligne suivante
attendra
 que la ligne asynchrone (avec
await
) ait fini son exécution

## Async / Await

Quand on utilise
async
 et
await
, une fonction asynchrone doit avoir le mot clé
async
 avant la fonction. Ensuite, dans le code, nous pouvons faire appel à des fonctions asynchrones et attendre leur résultat grâce au mot clé
await
 que l'on met devant l'appel de la fonction

## Asynchronous **JavaScript**: The Event Loop, Callbacks, Promises, and Async / Await

\*HYPERLINK "https://blog.bitsrc.io/journey-from-callbacks-to-promises-to-async-await-6fcd7f7fa3c5"https://blog.bitsrc.io/journey-from-callbacks-to-promises-to-async-await-6fcd7f7fa3c5

---

## AJAX

Si plusieurs fichiers **JavaScript** ont besoin d'effectuer des requêtes HTTP, alors le fichier « ajax.js » doit toujours être inclus dans la page web
avant
 les autres fichiers **JavaScript** qui utilisent les fonctions qu'il contient

## JSON

Le langage **JavaScript** permet de gérer facilement ce format de données
La fonction
JSON.parse()
 permet de transformer une chaîne de caractères conforme au format JSON en un objet **JavaScript**
La fonction
JSON.stringify()
 joue le rôle inverse : elle transforme un objet **JavaScript** en chaîne de caractères conforme au format JSON

## Iterable & Enumerable

The main difference between
iterable
 and
enumerable
 is that the former applies to
values
 and the latter to
properties

\*HYPERLINK "https://dilshankelsen.com/difference-between-iterable-enumarable-in-javascript/"https://dilshankelsen.com/difference-between-iterable-enumarable-in-javascript/

## Local Storage

Le
localStorage
 ne connait qu'un seul type de valeur :
les chaînes de caractères
