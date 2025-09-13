# React

### Create a new project with Create React App
https://create-react-app.dev/docs/getting-started

```bash
  $ npx create-react-app « app_name »
```

### CDN
Content Delivery Network, permet notamment d'importer une bibliothèque directement dans le code HTML

### DOM
Document Object Model, document comme un ensemble de nœuds et d'objets possédant des propriétés et des méthodes

	•	React – c'est l'API qui permettra de gérer les composants
	•	React DOM – c’est l'API qui est responsable de générer les composants dans le DOM
	•	Babel – cet outil permet d'utiliser les dernières syntaxes de JS dans le navigateur (ES6+)

### Webpack
C’est un bundler, il nous permet d’importer notre composant aussi facilement, avec import. Cet outil particulièrement utile est essentiel pour lier les fichiers entre eux, afin qu’ils soient interprétés par le navigateur

### Files extensions
.jsx => this is the JavaScript extension created by React, which allows us to use our syntax as tags directly in the JavaScript code
.ts  => for pure TypeScript files
.tsx => for files which contain JSX « JavaScript XML »

For example, a React component would be .tsx, but a file containing helper functions would be .ts

—————————————————————————

# Functions

memo() vous permet d’éviter de recalculer le rendu d’un composant du moment que ses props n’ont pas changé

—————————————————————————

# Hooks
Un hook est une fonction qui permet de « se brancher, to hook up » sur des fonctionnalités React

useState() est un hook qui permet d’ajouter le State Local React à des composants fonctions
=> state local est présent à l’intérieur d’un composant

Example of useState() decomposed :
```
const cartState = useState(0)
const cart = cartState[0]
const updateCart = cartState[1]
```

useEffect() est un hook qui permet d’exécuter des actions après le rendre de nos composants en choisissant à quel moment et à quelle fréquence cette action doit être exécutée (une fonction qui permet de « se brancher » sur la fonctionnalité des effets de React)
Appelez toujours useEffect() à la racine de votre composant

	•	Un tableau de dépendances vide [ ] permet d'exécuter un effet uniquement au premier rendu de votre composant
	•	Un tableau de dépendances [total] précis, permet de préciser quelle modification de donnée déclenche les effets exécutés
	•	Sans préciser le tableau de dépendance, le useEffect() est appelé à chaque rendu du composant

useContext() est un hook qui permet de « se brancher » depuis un composant enfant qui a été wrappé par un Provider, et donc d’accéder simplement au state partagé. Le Contexte est conçu pour partager des données qui peuvent être considérées comme globales

useCallback() est un hook qui vous permet de mettre en cache une définition de fonction d’un rendu à l’autre (qui peut changer en fonction de leurs dépendances)

useMemo() est un hook qui renvoie une valeur calculée (une sorte de cache, qui peut changer en fonction de leurs dépendances)

useRef() est un Hook React qui vous permet de référencer une valeur qui n’est pas nécessaire au code du rendu lui-même

—————————————————————————

# React Router
C’est une des bibliothèques qui permettent de transformer une App React en SPA (Single Page Application)

```bash
$ npm install react-router-dom
```

<Switch /> nous permet d'afficher uniquement la première route dont le chemin correspond, et on ajoute une route à laquelle on ne passe pas de prop path à notre composant <Error />, où le visiteur sera rédiriger en cas de fausse route

<Route exact path=« / »>, exact permet de préciser la route par défaut

useRouter() est un hook de Next.JS, it allows to use if you want to access to the « router » object inside any function of component in tour app

useParams() it’s a hook returns an object of key / value pairs of the dynamic params from the current URL that were matched by the <Route path>. Child routes inherit all params from their parent routes

—————————————————————————

# Redux
Bibliothèque de gestion d'état pour applications web
https://redux.js.org/

# Axios
Axios is a promise-based HTTP Client for Node.js and the browser. It is isomorphic (= it can run in the browser and nodejs with the same codebase). On the server-side it uses the native node.js http module, while on the client (browser) it uses XMLHttpRequests

# ESLint
L’outil permettant de signaler les erreurs de code
file name => .eslintrc.json or else

# Install ESLint
```bash
$ npm install --save-dev eslint

$ npx eslint --fix .
```

# Prettier
L’outil de formatage de code de référence
file name => .prettierrc.json or else

```bash
$ npm install --save-dev --save-exact prettier
```

# Format all files with Prettier
```bash
$ npx prettier . --write
```

# Keyboard Shortcuts in WebStorm on MacBook
=> Shift + Option + Command + P

# Library of Forms
https://react-hook-form.com/

# PropTypes
Bibliothèque qui permet de déclarer le type des props qui est attendu lorsque vous les récupérez dans vos composants, et de déclencher un warning, si ça ne correspond pas
```bash
$ npm install prop-types
```

# Styled Components
```bash
$ npm install styled-components
```

# Emotion
```bash
$ npm install --save @emotion/react
```

# Simple Import Sort
```bash
$ npm i eslint-plugin-simple-import-sort
```
