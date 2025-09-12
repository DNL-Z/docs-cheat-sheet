# **JavaScript**

## Variables

- **let** : variable à portée de bloc (**block scoped**) et peut-être réassignée
- **const** : à portée de bloc (**block scoped**) et sa référence ne peut pas être réassignée
- **var** : peut avoir une portée locale ou globale, peut être réassignée et est **hissée** (**hoisted**)

## Variable NULL vs UNDEFINED

- **undefined** signifie qu'une variable a été déclarée, mais qu'aucune valeur ne lui a encore été assignée (typeof = undefined)
- **null** est une valeur d'assignation. Elle peut être assignée à une variable comme représentation d'aucune valeur (typeof = object)

## Primitive

Une **primitive** (valeur primitive ou structure de donnée primitive) est une donnée qui n'est pas un objet et n'a pas de méthode. En **JavaScript**, il y a **7 types de données primitives** : **String**, **Number**, **Boolean**, **Null**, **undefined**, **Symbol**, **Bigint** (nouveauté d'ECMAScript 2020)

## Operator void

L'opérateur **void** évalue l'expression donnée puis retourne **undefined**

## **Babel**

C'est un **transcompilateur JavaScript** gratuit et open source qui est principalement utilisé pour convertir le code **ECMAScript 2015+** en une version **rétrocompatible** de **JavaScript** pouvant être exécutée par des moteurs **JavaScript** plus anciens

🔗 [https://babeljs.io/](https://babeljs.io/)

## Parcel

Le compilateur **JavaScript** de **Parcel** est construit sur **SWC**, qui gère la transpilation de **JavaScript**, **JSX**, et **TypeScript**. Par-dessus SWC, Parcel implémente la collecte de dépendances, le bundling, le **scope hoisting**, le **tree shaking**, l'émulation **Node**, le **hot reloading**, et plus encore

🔗 [https://parceljs.org/](https://parceljs.org/)

---

## Fonctions **JavaScript** de base

## Opérateurs conditionnels

- **Condition à la volée** avec l'opérateur logique : `true && expression || false && expression`
- **Opérateur ternaire conditionnel** : `condition ? exprSiVrai : exprSiFaux`

## Méthodes de tableaux

**concat()** : utilisée afin de fusionner un ou plusieurs tableaux en les concaténant

**includes()** : permet de déterminer si un tableau contient une valeur et renvoie **true** si c'est le cas, sinon **false**

**find()** : renvoie la valeur du **premier élément trouvé** dans le tableau qui respecte la condition donnée par la fonction de test passée en argument. Sinon, la valeur **undefined** est renvoyée

**some()** : teste si **au moins un élément** du tableau passe le test implémenté par la fonction fournie. Elle renvoie un **booléen** indiquant le résultat du test

**sort()** : trie les éléments d'un tableau, dans ce même tableau, et renvoie le tableau. Le tri s'effectue sur les éléments du tableau convertis en **chaînes de caractères** et triées selon les valeurs des unités de code **UTF-16**

**slice()** : renvoie un objet tableau, contenant une **copie superficielle** (**shallow copy**) d'une portion du tableau d'origine, la portion est définie par un indice de début et un indice de fin (exclus). Le **tableau original ne sera pas modifié**

**splice()** : **modifie le contenu** d'un tableau en retirant des éléments et/ou en ajoutant de nouveaux éléments

## Méthodes de chaînes de caractères

**split()** : divise une chaîne de caractères en une liste ordonnée de sous-chaînes, place ces sous-chaînes dans un tableau et retourne le tableau

Exemple :
```js
const str = 'The quick brown fox jumps over the lazy dog.';
const words = str.split(' ');
console.log(words[3]);
// expected output: "fox"
```

## Itérations et transformations de tableaux

**forEach()** : permet d'exécuter une fonction donnée sur chaque élément du tableau

**map()** : permet facilement d'itérer sur des données et de retourner un **nouveau tableau** d'éléments

**filter()** : crée et retourne un **nouveau tableau** contenant tous les éléments du tableau d'origine qui remplissent une condition déterminée par la fonction **callback**

Exemple :
```js
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter(word => word.length > 6);
console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]
```

**reduce()** : applique une fonction (accumulateur) qui traite chaque valeur d'une liste (de la gauche vers la droite) afin de la **réduire à une seule valeur**

## Déstructuration

La **déstructuration** permet de déclarer directement des variables et de leur assigner la valeur des propriétés d'un **objet** ou d'un **tableau**.

Exemple :
```js
const note = {
  id: 1,
  title: 'My first note',
  date: '01/01/1970',
};

const { id, title, date } = note;
```

## Opérateur de décomposition (Spread)

La syntaxe de **décomposition** « Spread » (`...`) permet d'**étendre** un itérable (tableau, chaîne, etc.)
- dans les **appels de fonctions** (plusieurs arguments),
- dans les **littéraux de tableaux** (plusieurs éléments),
- dans les **littéraux d'objets** (paires **clé–valeur**).

Exemple :
```js
const tools = ['hammer', 'screwdriver'];
const otherTools = ['wrench', 'saw'];

const allTools = [...tools, ...otherTools];
console.log(allTools);
// expected output:["hammer", "screwdriver", "wrench", "saw"]
```

## Gabarits de chaînes (Template literals)

Les **littéraux de gabarits** (`` `...` ``) sont des littéraux de chaînes de caractères permettant d'**intégrer des expressions**. Ils permettent aussi des chaînes **multi‑lignes** et l'**interpolation**.

Exemple :
```js
// Simple concatenation
let rep = 42;
console.log(`La réponse est ${rep}`);
```

## Expressions régulières (RegExp)

Une **expression régulière** (regex) comme `/^([a-zA-Z ]+)$/` permet, entre autres, de **vérifier** le contenu d'une chaîne de caractères.

Exemple :
```js
if (!pseudo.match(/^([a-zA-Z ]+)$/)) {
  alert('Pseudo invalide');
}
```

---

## Callback

Un **callback** est simplement une **fonction** que vous définissez. Le principe est de la **passer en paramètre** d’une fonction **asynchrone**. Une fois que la fonction asynchrone a fini sa tâche, elle **appelle** notre fonction callback en lui passant un **résultat**. Ainsi, le code que nous mettons dans notre fonction callback sera **exécuté de manière asynchrone**.

Exemple :
```js
function salutation(name) {
  alert('Bonjour ' + name);
}

function processUserInput(callback) {
  var name = prompt('Entrez votre nom.');
  callback(name);
}

processUserInput(salutation);
```

## Promise

L'objet **Promise** est utilisé pour réaliser des traitements **asynchrones**. Tout appel à une fonction définie avec le mot clé **async** retourne une **Promise** de la valeur retournée avec **return**.

Une Promise expose notamment :
- **.then()** pour exécuter du code dès que la **promesse est résolue**,
- **.catch()** pour exécuter du code dès qu'une **erreur** est survenue.

---

## Synchrone vs Asynchrone

- **Synchrone** : le code s'exécute **ligne après ligne**, en attendant la fin de l'exécution de la ligne précédente.
- **Asynchrone** : le code s'exécute ligne après ligne, mais une **ligne suivante** peut **attendre** qu'une opération asynchrone (par exemple avec **await**) ait fini son exécution.

## Async / Await

Avec **async** et **await** :
- une fonction asynchrone doit avoir le mot clé **async** avant la fonction ;
- dans le code, on peut **attendre** le résultat d'autres fonctions asynchrones grâce au mot clé **await** placé devant l'appel de la fonction.

## Article recommandé

Asynchronous **JavaScript**: The Event Loop, Callbacks, Promises, and Async / Await
🔗 https://blog.bitsrc.io/journey-from-callbacks-to-promises-to-async-await-6fcd7f7fa3c5

---

## AJAX

Si plusieurs fichiers **JavaScript** ont besoin d'effectuer des **requêtes HTTP**, alors le fichier `ajax.js` doit toujours être inclus dans la page web **avant** les autres fichiers **JavaScript** qui utilisent les fonctions qu'il contient.

## JSON

**JavaScript** permet de gérer facilement ce format de données :
- **JSON.parse()** : transforme une **chaîne** conforme au format JSON en un **objet JavaScript** ;
- **JSON.stringify()** : transforme un **objet JavaScript** en **chaîne** conforme au format JSON.

## Iterable & Enumerable

The main difference between **iterable** and **enumerable** is that the former applies to **values** and the latter to **properties**.
🔗 https://dilshankelsen.com/difference-between-iterable-enumarable-in-javascript/

## Local Storage

Le **localStorage** ne connait qu'un seul type de valeur : les **chaînes de caractères**.
