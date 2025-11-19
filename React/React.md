# ⚛️ React

A comprehensive reference guide for React development, covering project setup, core concepts, hooks, routing, state management, and essential tools.

## 📑 Table of Contents

- [🚀 Getting Started](#-getting-started)
  - [Create a New Project](#create-a-new-project)
  - [File Extensions](#file-extensions)
- [🔧 Core Concepts](#-core-concepts)
  - [CDN](#cdn)
  - [DOM](#dom)
  - [Webpack](#webpack)
- [🎣 Hooks](#-hooks)
  - [useState](#usestate)
  - [useEffect](#useeffect)
  - [useContext](#usecontext)
  - [useCallback](#usecallback)
  - [useMemo](#usememo)
  - [useRef](#useref)
- [⚡ Performance](#-performance)
  - [memo()](#memo)
- [🛣️ React Router](#-react-router)
  - [Installation](#installation)
  - [Router Hooks](#router-hooks)
- [📚 State Management & HTTP](#-state-management--http)
  - [Redux](#redux)
  - [Axios](#axios)
- [🎨 Styling](#-styling)
  - [Styled Components](#styled-components)
  - [Emotion](#emotion)
- [🛠️ Development Tools](#-development-tools)
  - [ESLint](#eslint)
  - [Prettier](#prettier)
  - [PropTypes](#proptypes)
  - [Simple Import Sort](#simple-import-sort)
- [📝 Forms](#-forms)
- [⌨️ Keyboard Shortcuts](#-keyboard-shortcuts)

---

## 🚀 Getting Started

### Create a New Project

Using Create React App:

**Documentation:** https://create-react-app.dev/docs/getting-started

```bash
  npx create-react-app <app_name>
```

### File Extensions

- **`.jsx`** - JavaScript extension created by React, allows using JSX syntax directly in JavaScript code
- **`.ts`** - For pure TypeScript files
- **`.tsx`** - For files containing JSX (JavaScript XML)

**Example:** A React component would use `.tsx`, while a file containing helper functions would use `.ts`.

---

## 🔧 Core Concepts

### CDN

**Content Delivery Network** allows importing libraries directly into HTML code.

### DOM

**Document Object Model** - represents the document as a set of nodes and objects with properties and methods.

**Key libraries:**
- **React** - API for managing components
- **React DOM** - API responsible for rendering components in the DOM
- **Babel** - Tool that enables using the latest JavaScript syntax (ES6+) in the browser

### Webpack

A **bundler** that allows importing components easily with `import`. This essential tool links files together so they can be interpreted by the browser.

---

## 🎣 Hooks

Hooks are functions that allow you to "hook into" React features.

### useState

A hook that adds React local state to functional components.

**Note:** Local state exists inside a component.

**Example decomposed:**

```javascript
const cartState = useState(0)
const cart = cartState[0]
const updateCart = cartState[1]
```

### useEffect

A hook that executes actions after rendering components, allowing you to choose when and how often the action should be executed.

**Important:** Always call `useEffect()` at the root of your component.

**Dependency array behavior:**
- **Empty array `[]`** - Executes the effect only on first render
- **Specific array `[total]`** - Executes when specified data changes
- **No array** - Executes on every component render

### useContext

A hook that allows a child component wrapped by a Provider to access the shared state. Context is designed to share data that can be considered global.

### useCallback

A hook that lets you cache a function definition between renders (can change based on dependencies).

### useMemo

A hook that returns a memoized calculated value (a sort of cache, can change based on dependencies).

### useRef

A React Hook that lets you reference a value that isn't needed for rendering itself.

---

## ⚡ Performance

### memo()

Allows you to skip re-rendering a component when its props haven't changed.

---

## 🛣️ React Router

One of the libraries that transform a React App into an SPA (Single Page Application).

### Installation

```bash
  npm install react-router-dom
```

**Key components:**

- **`<Switch />`** - Displays only the first route whose path matches, with a default route without a `path` prop redirecting to an `<Error />` component for invalid routes
- **`<Route exact path="/" />`** - The `exact` prop specifies the default route

### Router Hooks

**`useRouter()`** - A Next.js hook that allows accessing the router object inside any function component in your app.

**`useParams()`** - Returns an object of key/value pairs of dynamic params from the current URL matched by the `<Route path>`. Child routes inherit all params from parent routes.

---

## 📚 State Management & HTTP

### Redux

State management library for web applications.

**Documentation:** https://redux.js.org/

### Axios

A promise-based HTTP Client for Node.js and the browser. It is isomorphic (can run in both browser and Node.js with the same codebase). On the server-side it uses the native `node.js` http module, while on the client (browser) it uses XMLHttpRequests.

---

## 🎨 Styling

### Styled Components

```bash
  npm install styled-components
```

### Emotion

```bash
  npm install --save @emotion/react
```

---

## 🛠️ Development Tools

### ESLint

Tool for identifying code errors.

**Configuration file:** `eslint.config.js` or `eslint.config.mjs`

**Install ESLint:**

```bash
  npm install --save-dev eslint
```

**Fix errors automatically:**

```bash
  npx eslint --fix .
```

### Prettier

The reference code formatting tool.

**Configuration file:** `.prettierrc.json` or other formats

**Install Prettier:**

```bash
  npm install --save-dev --save-exact prettier
```

**Format all files:**

```bash
  # Check formatting
  npx prettier . --check

  # Write formatting changes
  npx prettier . --write
```

### PropTypes

A library that declares the expected type of props when receiving them in components, triggering a warning if types don't match.

```bash
  npm install prop-types
```

### Simple Import Sort

```bash
  npm install --save-dev eslint-plugin-simple-import-sort
```

⚠️ **Note:** Requires changes to the `eslint.config.js` or `eslint.config.mjs` file.

---

## 📝 Forms

**React Hook Form** - A library for managing forms in React.

**Documentation:** https://react-hook-form.com/

---

## ⌨️ Keyboard Shortcuts

### WebStorm on MacBook

**Format with Prettier:** `Shift + Option + Command + P`

---
