# 🟨 JavaScript

Interpreted programming language, mainly used for client-side and server-side web development.

## 📑 Table of Contents

- [📦 Variables and Types](#-variables-and-types)
  - [Variable Declaration](#variable-declaration)
  - [NULL vs UNDEFINED](#null-vs-undefined)
  - [Primitive Types](#primitive-types)
  - [Void Operator](#void-operator)
- [🛠️ Compilation Tools](#-compilation-tools)
  - [Babel](#babel)
  - [Parcel](#parcel)
  - [Webpack](#webpack)
- [🧮 Basic Functions](#-basic-functions)
  - [Conditional Operators](#conditional-operators)
  - [Array Methods](#array-methods)
  - [String Methods](#string-methods)
  - [Iterations and Transformations](#iterations-and-transformations)
- [🎯 Modern Syntax](#-modern-syntax)
  - [Destructuring](#destructuring)
  - [Spread Operator](#spread-operator)
  - [Template Literals](#template-literals)
  - [Regular Expressions (RegExp)](#regular-expressions-regexp)
- [⚡ Asynchronous Programming](#-asynchronous-programming)
  - [Callback](#callback)
  - [Promise](#promise)
  - [Synchronous vs Asynchronous](#synchronous-vs-asynchronous)
  - [Async / Await](#async--await)
- [🌐 APIs and Storage](#-apis-and-storage)
  - [AJAX](#ajax)
  - [JSON](#json)
  - [Local Storage](#local-storage)
- [📚 Advanced Concepts](#-advanced-concepts)
  - [Iterable & Enumerable](#iterable--enumerable)

---

## 📦 Variables and Types

### Variable Declaration

- **let**: block scoped variable that can be reassigned
- **const**: block scoped and its reference cannot be reassigned
- **var**: can have local or global scope, can be reassigned and is **hoisted**

### NULL vs UNDEFINED

- **undefined** means a variable has been declared, but no value has been assigned to it yet (typeof = undefined)
- **null** is an assignment value. It can be assigned to a variable as a representation of no value (typeof = object)

### Primitive Types

A **primitive** (primitive value or primitive data structure) is data that is not an object and has no methods. In **JavaScript**, there are **7 primitive data types**: **String**, **Number**, **Boolean**, **Null**, **undefined**, **Symbol**, **Bigint** (new in ECMAScript 2020)

### Void Operator

The **void** operator evaluates the given expression and then returns **undefined**

---

## 🛠️ Compilation Tools

### Babel

It's a free and open source **JavaScript transcompiler** that is mainly used to convert **ECMAScript 2015+** code into a **backwards compatible** version of **JavaScript** that can be run by older **JavaScript** engines

🔗 [https://babeljs.io/](https://babeljs.io/)

### Parcel

**Parcel**'s **JavaScript** compiler is built on **SWC**, which handles transpilation of **JavaScript**, **JSX**, and **TypeScript**. On top of SWC, Parcel implements dependency collection, bundling, **scope hoisting**, **tree shaking**, **Node** emulation, **hot reloading**, and more

🔗 [https://parceljs.org/](https://parceljs.org/)

### Webpack
**Webpack** is a **module bundler** for modern JavaScript applications. It analyzes your application, builds a dependency graph and generates one or more bundles

🔗 [https://webpack.js.org/](https://webpack.js.org/)

---

## 🧮 Basic Functions

### Conditional Operators

```js
// On-the-fly condition with logical operator
true && expression || false && expression

// Conditional ternary operator
condition ? exprIfTrue : exprIfFalse
```

### Array Methods

**concat()**: used to merge one or more arrays by concatenating them

**includes()**: determines whether an array contains a value and returns **true** if it does, otherwise **false**

**find()**: returns the value of the **first element found** in the array that meets the condition given by the test function passed as an argument. Otherwise, the **undefined** value is returned

**some()**: tests whether **at least one element** in the array passes the test implemented by the provided function. It returns a **boolean** indicating the test result

**sort()**: sorts the elements of an array, in that same array, and returns the array. The sort is performed on the array elements converted to **character strings** and sorted according to the values of **UTF-16** code units

**slice()**: returns an array object, containing a **shallow copy** of a portion of the original array, the portion is defined by a start index and an end index (excluded). The **original array will not be modified**

**splice()**: **modifies the content** of an array by removing elements and/or adding new elements

### String Methods

**split()**: divides a character string into an ordered list of substrings, places these substrings in an array and returns the array

Example:
```js
const str = 'The quick brown fox jumps over the lazy dog.';
const words = str.split(' ');
console.log(words[3]);
// expected output: "fox"
```

### Iterations and Transformations

**forEach()**: allows executing a given function on each element of the array

**map()**: makes it easy to iterate over data and return a **new array** of elements

**filter()**: creates and returns a **new array** containing all the elements of the original array that meet a condition determined by the **callback** function

Example:
```js
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter(word => word.length > 6);
console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]
```

**reduce()**: applies a function (accumulator) that processes each value in a list (from left to right) in order to **reduce it to a single value**

---

## 🎯 Modern Syntax

### Destructuring

**Destructuring** allows you to directly declare variables and assign them the value of properties from an **object** or an **array**.

Example:
```js
const note = {
  id: 1,
  title: 'My first note',
  date: '01/01/1970',
};

const { id, title, date } = note;
```

### Spread Operator

The **Spread** syntax (`...`) allows you to **expand** an iterable (array, string, etc.)
- in **function calls** (multiple arguments),
- in **array literals** (multiple elements),
- in **object literals** (**key–value** pairs).

Example:
```js
const tools = ['hammer', 'screwdriver'];
const otherTools = ['wrench', 'saw'];

const allTools = [...tools, ...otherTools];
console.log(allTools);
// expected output: ["hammer", "screwdriver", "wrench", "saw"]
```

### Template Literals

**Template literals** (`` `...` ``) are string literals allowing **expression interpolation**. They also allow **multi-line** strings and **interpolation**.

Example:
```js
// Simple concatenation
let rep = 42;
console.log(`The answer is ${rep}`);
```

### Regular Expressions (RegExp)

A **regular expression** (regex) like `/^([a-zA-Z ]+)$/` allows, among other things, to **verify** the content of a character string.

Example:
```js
if (!pseudo.match(/^([a-zA-Z ]+)$/)) {
  alert('Invalid pseudo');
}
```

---

## ⚡ Asynchronous Programming

### Callback

A **callback** is simply a **function** that you define. The principle is to **pass it as a parameter** to an **asynchronous** function. Once the asynchronous function has finished its task, it **calls** our callback function by passing it a **result**. Thus, the code we put in our callback function will be **executed asynchronously**.

Example:
```js
function greeting(name) {
  alert('Hello ' + name);
}

function processUserInput(callback) {
  var name = prompt('Enter your name.');
  callback(name);
}

processUserInput(greeting);
```

### Promise

The **Promise** object is used to perform **asynchronous** processing. Any call to a function defined with the **async** keyword returns a **Promise** of the value returned with **return**.

A Promise exposes in particular:
- **.then()** to execute code as soon as the **promise is resolved**,
- **.catch()** to execute code as soon as an **error** has occurred

### Synchronous vs Asynchronous

- **Synchronous**: the code executes **line by line**, waiting for the end of the execution of the previous line.
- **Asynchronous**: the code executes line by line, but a **following line** can **wait** for an asynchronous operation (for example with **await**) to finish its execution.

### Async / Await

With **async** and **await**:
- an asynchronous function must have the **async** keyword before the function;
- in the code, we can **wait** for the result of other asynchronous functions thanks to the **await** keyword placed before the function call.

#### 📖 Recommended Article

Asynchronous **JavaScript**: The Event Loop, Callbacks, Promises, and Async / Await

🔗 https://blog.bitsrc.io/journey-from-callbacks-to-promises-to-async-await-6fcd7f7fa3c5

---

## 🌐 APIs and Storage

### AJAX

If multiple **JavaScript** files need to perform **HTTP requests**, then the `ajax.js` file must always be included in the web page **before** the other **JavaScript** files that use the functions it contains.

### JSON

**JavaScript** makes it easy to handle this data format:
- **JSON.parse()**: transforms a **string** conforming to the JSON format into a **JavaScript object**;
- **JSON.stringify()**: transforms a **JavaScript object** into a **string** conforming to the JSON format.

### Local Storage

The **localStorage** only knows one type of value: **character strings**.

---

## 📚 Advanced Concepts

### Iterable & Enumerable

The main difference between **iterable** and **enumerable** is that the former applies to **values** and the latter to **properties**.

🔗 https://dilshankelsen.com/difference-between-iterable-enumarable-in-javascript/
