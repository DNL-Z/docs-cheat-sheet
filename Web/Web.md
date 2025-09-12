# WEB

## ACRONYMS - ACRONYMES

## CTO (Chief Technical Officer - Directeur des Nouvelles Technologies)

C’est le rôle d’une personne au sein d’une organisation qui a pour fonction d’orienter la stratégie de l'utilisation d'outils technologiques dans une organisation afin de permettre à celle-ci de réaliser ses objectifs. Il est donc en charge de l’innovation, du déploiement technique et technologique adaptés au développement d’une entreprise.
C'est un métier qui représente vraiment l'essence de la curiosité des développeur·se·s, dans le sens où cette personne doit en permanence connaître les nouvelles évolutions tech.

## Address IP (Internet Protocol Address)

L'adresse IP (Internet Protocol) désigne un numéro unique attribué de manière provisoire ou durable à un ordinateur connecté à un réseau informatique qui utilise l'internet protocole.

## NAT (**Network** Address Translation)

En réseau informatique, on dit qu'un routeur fait du network address translation (NAT) (« traduction d'adresse réseau » ou « translation d'adresse réseau ») lorsqu'il fait correspondre des adresses IP à d'autres adresses IP. En particulier, un cas courant est de permettre à des machines disposant d'adresses privées qui font partie d'un intranet et ne sont ni uniques ni routables à l'échelle d'Internet, de communiquer avec le reste d'Internet en utilisant vers l'extérieur des adresses externes publiques, uniques et routables.

## LAN (Local Area **Network**)

Réseau local, désigne les appareils connectés, par Wi-Fi ou connexion filaire, dans votre domicile ou bureau.

## DOM (Document Object Model)

Le « Document Object Model » ou DOM (pour modèle objet de document) est une interface de programmation pour les documents **HTML**, XML et SVG. Il fournit
une représentation structurée du document sous forme d'un arbre et définit la façon dont la structure peut être manipulée par les programmes,
 en termes de style et de contenu. Le DOM représente le document comme un ensemble de nœuds et d'objets possédant des propriétés et des méthodes. Les nœuds peuvent également avoir des gestionnaires d'événements qui se déclenchent lorsqu'un événement se produit. Cela permet de manipuler des pages web grâce à des scripts et/ou des langages de programmation. Les nœuds peuvent être associés à des gestionnaires d'événements. Une fois qu'un événement est déclenché, les gestionnaires d'événements sont exécutés.

## HOMEBREW

Le gestionnaire de paquets pour macOS, gratuit et open-source écrit en **Ruby**. Son but est de simplifier l'installation de programme. Il a été créé par Max Howell, le logiciel a connu un gain de popularité au sein de la communauté de **Ruby** on Rails et a reçu des éloges pour sa scalabilité.

```bash
brew --version
```

## **NPM** & YARN

**NPM** est le gestionnaire de paquets officiel de **Node.js**. Depuis la version 0.6.3 de **Node.js**, **npm** fait partie de l'environnement et est donc automatiquement installé par défaut. **NPM** fonctionne avec un terminal et gère les dépendances pour une application.

```bash
npm -v
```

## COMPOSER

**Composer** est un logiciel gestionnaire de dépendances libre écrit en **PHP**. Il permet à ses utilisateurs de déclarer et d'installer les bibliothèques dont le projet principal a besoin. Le développement a débuté en avril 2011 et a donné lieu à une première version sortie le 1er mars 2012.

```bash
composer --version
```

```bash
composer self-update
```

## LINT

Linting is the process of running a program that will analyse code for potential errors.

## XML

« Extensible Markup Language », signifie que ce format de fichier est conçu pour transmettre des informations. À ce titre, il ne faut pas se limiter aux échanges d'informations entre humains, ou entre une application et un humain : XML est tout aussi bien conçu, si ce n'est mieux, pour
des échanges entre applications informatiques
.

## API

Application Programming Interface (Interface de Programmation d’Application).

## Types of API

SOAP -
Simple Object Access Protocol.

REST -
Representational State Transfer.

## Differences of API

SOAP -
repose exclusivement sur XML pour envoyer des messages.

REST -
s’appuie souvent sur une URL simple et peut utiliser quatre méthodes de requête HTTP 1.1 différents :
(GET, POST, PUT et DELETE) pour effectuer des tâches.

POO
 =>
Programmation Orienté Objet
, c’est une méthode de programmation informatique qui consiste à définir un objet selon plusieurs caractéristiques, lesquelles vont hériter dans les enfant de l’objet. 

Paradigme
 => Une manière d’approcher selon les règles et de pouvoir définir quel langage utiliser pour programmer.

Design-Patterns
 => une manière de pensée et d’organiser son code.

---

HTTP
 =
Hyper Text Transfer Protocol
C’est un échange d’informations sur le web, son équivalents sécurise HTTPS. 

Protocole :
Client
 <=>
Serveur
Mécanisme :
requête
 /
réponse

CORS
 = le «
Cross-Origin Resource Sharing
 » ou « partage des ressources entre origines multiples » (en français, moins usité) est un mécanisme qui consiste à ajouter des en-têtes HTTP afin de permettre à un agent utilisateur d'accéder à des ressources d'un serveur situé sur une autre origine que le site courant. Un agent utilisateur réalise une requête HTTP multi-origine (cross-origin) lorsqu'il demande une ressource provenant d'un domaine, d'un protocole ou d'un port différent de ceux utilisés pour la page courante.

CDN
 = le «
Content Delivery **Network**
 » permet d'importer une bibliothèque directement dans le code **HTML**.

AJAX
 =
Asynchronous **JavaScript** And XML
C’est équivalent à une requête HTTP asynchrone vers un serveur web pour récupérer ou envoyer des données sous différentes formats.
Echange
SYNCHRONE
 => le demandeur attend que l’information voulue lui soit fournie.
Exemple : conversation téléphonique, chacun à son tour.
Echange
ASYNCHRONE
 => le demandeur peut faire autre chose en attendant la réponse.
Exemple : j’ai répondu à un email et en attendant la réponse je fais autre chose. 
Les requêtes
AJAX
 sont limités par leur Cross Domain = « same origin policy ».
C’est à dire qu’on ne peut pas interroger 2 différents domaines (pour la sécurité).
Il est possible d’activer sur un serveur web ->
Cross Origin Resource Sharing
.
Pour autoriser les requêtes d’autres domaine que le sien.

JSON
 =
**JavaScript** Object Notation
(key => value)

## Les méthodes HTTP

OPTIONS
 : en
CORS
, une requête de pré-vérification est envoyée avec la méthode OPTIONS afin que le serveur indique si la requête est acceptable avec les paramètres spécifiés.

GET
 : permet de
récupérer des ressources
, comme par exemple le temps actuel sur un service de météo.

POST
 : permet de
créer ou modifier une ressource
, comme la création d'un nouvel utilisateur sur votre application.

PUT
 : permet de
modifier une ressource
, comme le nom de l'utilisateur que vous venez de créer avec POST.

DELETE
 : Permet de
supprimer une ressource
, comme un commentaire dans un fil de discussion.

## Codes HTTP

200
 - indique que tout s'est bien passé

201
 - indique que tout s'est bien passé et qu'une nouvelle ressource a bien été créée

204
 - indique que tout s'est bien passé, mais qu'aucun résultat n'est renvoyé

301
 &
302
 - redirection

400
 - indique qu'une requête est erronée

401
 - indique que l'utilisateur n'est pas authentifié, alors que c'est nécessaire

403
 - indique que l'utilisateur n'a pas le droit d'accéder à cette ressource (accès refuser
)

404
 - indique que la ressource demandée n'existe pas (page non trouvée
)

500
 - indique que le serveur a subi une erreur interne (erreur serveur
)

504
 - le serveur ne réponds pas

502
 -
indique que le serveur, agissant comme une passerelle ou un proxy, a reçu une réponse invalide depuis le serveur en amont
522
 - problème d’interface

## Récupération de résultat de la requête

UNSENT
(code 0) : l'objet est prêt mais la méthode open() n'a pas encore été appelée.

OPENED
 (code 1) : open() a été appelé.

HEADERS_RECEIVED
 (code 2) :  send() a été appelé, les headers et  status  sont disponibles au sein de l'objet.

LOADING
 (code 3) : réception en cours, les données reçues sont partielles.

DONE
 (code 4) : requête terminée.

---

ReadyState
  : qui contient l'état de la requête.

Status
  : qui contient le code de statut de la requête
	- 2xx quand ça s'est bien passé
	- 3xx pour les redirection
	- 4xx pour les erreurs

ResponseText
  : qui contient la réponse du service web au format texte. Ainsi, si le texte que l'on attend est au format JSON, il va falloir le transformer en objet **JavaScript** avec la fonction
JSON.parse(texteJSON)
 <=>
JSON.stringify(jsonBody)
.

Socket
 -> point de connexion.
