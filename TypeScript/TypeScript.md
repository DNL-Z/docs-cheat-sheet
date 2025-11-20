# 🔷 TypeScript

Statically typed superset of JavaScript that compiles to plain JavaScript, providing type safety and enhanced developer tooling for modern web development.

## 📑 Table of Contents

- [📦 Variables and Types](#-variables-and-types)
  - [Variable Declaration](#variable-declaration)
  - [Type Annotation](#type-annotation)
  - [Type Inference](#type-inference)
- [🔤 Type System](#-type-system)
  - [Interface vs Type](#interface-vs-type)
  - [Union and Intersection Types](#union-and-intersection-types)
  - [Type Guards](#type-guards)
- [🧮 Utility Types](#-utility-types)
  - [Partial&lt;T&gt;](#partialt)
  - [Required&lt;T&gt;](#requiredt)
  - [Readonly&lt;T&gt;](#readonlyt)
  - [Record&lt;K, T&gt;](#recordk-t)
  - [Pick&lt;T, K&gt;](#pickt-k)
  - [Omit&lt;T, K&gt;](#omitt-k)
- [📚 Collections](#-collections)
  - [Arrays](#arrays)
  - [Set&lt;T&gt;](#sett)
  - [Map&lt;K, V&gt;](#mapk-v)
- [🎯 Functions](#-functions)
  - [Function Types](#function-types)
  - [Arrow Functions](#arrow-functions)
  - [Generic Functions](#generic-functions)
- [🔧 Object-Oriented Programming](#-object-oriented-programming)
  - [Classes](#classes)
  - [Interfaces](#interfaces)
  - [Abstract Classes](#abstract-classes)
- [💡 Advanced Concepts](#-advanced-concepts)
  - [Generics](#generics)
  - [Decorators](#decorators)
  - [Type Assertions](#type-assertions)

---

## 📦 Variables and Types

### Variable Declaration

```typescript
// Variable (mutable)
let counter: number = 0;

// Constant (immutable)
const maxValue: number = 100;

// Variable without initialization
let username: string;
```

### Type Annotation

Explicitly declare types for variables:

```typescript
let age: number = 25;
let name: string = "Alice";
let isActive: boolean = true;
let data: any = "flexible";  // Avoid using 'any' when possible
```

### Type Inference

TypeScript automatically infers types when not explicitly declared:

```typescript
let count = 42;           // Inferred as number
let message = "Hello";    // Inferred as string
let enabled = true;       // Inferred as boolean
```

---

## 🔤 Type System

### Interface vs Type

**Type aliases** and **interfaces** are very similar, and in many cases you can choose between them freely. Almost all features of an interface are available in type, the **key distinction** is that a type cannot be re-opened to add new properties, whereas an interface is always extendable.

```typescript
// Interface (extendable)
interface User {
  name: string;
  age: number;
}

interface User {
  email: string;  // ✅ Extends the existing User interface
}

// Type alias (not extendable)
type Person = {
  name: string;
  age: number;
};

// type Person = {
//   email: string;  // ❌ Error: Duplicate identifier
// }

// Type alias for union types
type Status = "pending" | "approved" | "rejected";

// Type alias for complex types
type Callback = (result: string) => void;
```

**When to use:**
- Use **interface** for object shapes that may be extended
- Use **type** for unions, intersections, and complex type compositions

### Union and Intersection Types

```typescript
// Union type (one of several types)
type StringOrNumber = string | number;

let value: StringOrNumber;
value = "hello";   // ✅ OK
value = 42;        // ✅ OK

// Intersection type (combines multiple types)
type Person = { name: string };
type Employee = { employeeId: number };

type Staff = Person & Employee;

const worker: Staff = {
  name: "Alice",
  employeeId: 123
};
```

### Type Guards

Narrow down types within conditional blocks:

```typescript
function processValue(value: string | number) {
  if (typeof value === "string") {
    // TypeScript knows value is string here
    console.log(value.toUpperCase());
  } else {
    // TypeScript knows value is number here
    console.log(value.toFixed(2));
  }
}

// Custom type guard
interface Cat {
  meow(): void;
}

interface Dog {
  bark(): void;
}

function isCat(animal: Cat | Dog): animal is Cat {
  return (animal as Cat).meow !== undefined;
}
```

---

## 🧮 Utility Types

### Partial&lt;T&gt;

Constructs a type with all properties of `T` set to **optional**. This utility represents all subsets of a given type.

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// All properties become optional
type PartialUser = Partial<User>;

function updateUser(id: number, updates: Partial<User>) {
  // Can update any subset of properties
}

updateUser(1, { name: "Alice" });  // ✅ OK
updateUser(2, { email: "bob@example.com", age: 30 });  // ✅ OK
```

### Required&lt;T&gt;

Constructs a type with all properties of `T` set to **required** (opposite of Partial):

```typescript
interface User {
  id?: number;
  name?: string;
  email?: string;
}

type RequiredUser = Required<User>;

const user: RequiredUser = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"  // All properties must be provided
};
```

### Readonly&lt;T&gt;

Constructs a type with all properties of `T` set to **readonly**:

```typescript
interface User {
  id: number;
  name: string;
}

const user: Readonly<User> = {
  id: 1,
  name: "Alice"
};

// user.name = "Bob";  // ❌ Error: Cannot assign to 'name' because it is read-only
```

### Record&lt;K, T&gt;

Constructs an object type whose keys are of type `K` and values are of type `T`. `K` is usually a union of string or number literals, and `T` represents the type of values associated with these keys.

```typescript
type Role = "admin" | "user" | "guest";

const permissions: Record<Role, string[]> = {
  admin: ["read", "write", "delete"],
  user: ["read", "write"],
  guest: ["read"]
};

// Using with string keys
type UserDatabase = Record<string, { name: string; age: number }>;

const users: UserDatabase = {
  "user1": { name: "Alice", age: 30 },
  "user2": { name: "Bob", age: 25 }
};
```

### Pick&lt;T, K&gt;

Constructs a type by picking specific properties `K` from `T`:

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

type UserPreview = Pick<User, "id" | "name">;

const preview: UserPreview = {
  id: 1,
  name: "Alice"
  // email and password are not included
};
```

### Omit&lt;T, K&gt;

Constructs a type by omitting specific properties `K` from `T`:

```typescript
interface User {
  id: number;
  name: string;
  email: string;
  password: string;
}

type PublicUser = Omit<User, "password">;

const publicUser: PublicUser = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
  // password is excluded
};
```

---

## 📚 Collections

### Arrays

```typescript
// Typed arrays
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["Alice", "Bob", "Charlie"];

// Array methods
numbers.push(6);
numbers.pop();
numbers.map(n => n * 2);
numbers.filter(n => n > 3);

// Readonly arrays
const readonlyNumbers: readonly number[] = [1, 2, 3];
// readonlyNumbers.push(4);  // ❌ Error
```

### Set&lt;T&gt;

Represents a collection of **unique elements** of type `T`. Unlike arrays, sets do not allow duplicate values.

```typescript
// Create a set
const uniqueNumbers = new Set<number>();

uniqueNumbers.add(1);
uniqueNumbers.add(2);
uniqueNumbers.add(2);  // Duplicate, will be ignored

console.log(uniqueNumbers.size);  // 2
console.log(uniqueNumbers.has(1));  // true

// Iterate over set
uniqueNumbers.forEach(num => console.log(num));

// Convert to array
const numbersArray = Array.from(uniqueNumbers);

// Remove duplicates from array
const duplicates = [1, 2, 2, 3, 3, 3, 4];
const unique = [...new Set(duplicates)];  // [1, 2, 3, 4]
```

### Map&lt;K, V&gt;

Collection of key-value pairs with keys of type `K` and values of type `V`:

```typescript
// Create a map
const userRoles = new Map<number, string>();

userRoles.set(1, "admin");
userRoles.set(2, "user");

console.log(userRoles.get(1));  // "admin"
console.log(userRoles.has(2));  // true
console.log(userRoles.size);    // 2

// Iterate over map
userRoles.forEach((role, id) => {
  console.log(`User ${id}: ${role}`);
});

// Object-like map
const config = new Map<string, any>([
  ["timeout", 3000],
  ["retries", 3],
  ["debug", true]
]);
```

---

## 🎯 Functions

### Function Types

```typescript
// Function declaration with types
function add(a: number, b: number): number {
  return a + b;
}

// Function with optional parameters
function greet(name: string, greeting?: string): string {
  return `${greeting || "Hello"}, ${name}!`;
}

// Function with default parameters
function multiply(a: number, b: number = 1): number {
  return a * b;
}

// Function with rest parameters
function sum(...numbers: number[]): number {
  return numbers.reduce((acc, curr) => acc + curr, 0);
}
```

### Arrow Functions

```typescript
// Arrow function syntax
const add = (a: number, b: number): number => a + b;

// With function type
const subtract: (a: number, b: number) => number = (a, b) => a - b;

// Callback example
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((n: number) => n * 2);
```

### Generic Functions

```typescript
// Generic function
function identity<T>(value: T): T {
  return value;
}

console.log(identity<string>("hello"));  // "hello"
console.log(identity<number>(42));       // 42

// Generic function with constraints
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const person = { name: "Alice", age: 30 };
const name = getProperty(person, "name");  // "Alice"
```

---

## 🔧 Object-Oriented Programming

### Classes

```typescript
// Basic class
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet(): string {
    return `Hello, I'm ${this.name}`;
  }
}

const person = new Person("Alice", 30);
console.log(person.greet());

// Class with access modifiers
class BankAccount {
  private balance: number;
  public accountNumber: string;
  protected owner: string;

  constructor(accountNumber: string, owner: string, initialBalance: number = 0) {
    this.accountNumber = accountNumber;
    this.owner = owner;
    this.balance = initialBalance;
  }

  public deposit(amount: number): void {
    this.balance += amount;
  }

  public getBalance(): number {
    return this.balance;
  }
}
```

### Interfaces

```typescript
// Interface for object shape
interface User {
  id: number;
  name: string;
  email: string;
  isActive?: boolean;  // Optional property
}

const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
};

// Interface for function
interface SearchFunction {
  (query: string, limit: number): string[];
}

const search: SearchFunction = (query, limit) => {
  return [`Result for ${query}`];
};

// Interface extending another interface
interface Admin extends User {
  permissions: string[];
}
```

### Abstract Classes

```typescript
// Abstract class (cannot be instantiated)
abstract class Shape {
  abstract getArea(): number;

  describe(): string {
    return `Area: ${this.getArea()}`;
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }

  getArea(): number {
    return Math.PI * this.radius ** 2;
  }
}

const circle = new Circle(5);
console.log(circle.describe());  // "Area: 78.53981633974483"
```

---

## 💡 Advanced Concepts

### Generics

```typescript
// Generic class
class Box<T> {
  private content: T;

  constructor(content: T) {
    this.content = content;
  }

  getContent(): T {
    return this.content;
  }

  setContent(content: T): void {
    this.content = content;
  }
}

const numberBox = new Box<number>(42);
const stringBox = new Box<string>("Hello");

// Generic interface
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

const userResponse: ApiResponse<User> = {
  data: { id: 1, name: "Alice", email: "alice@example.com" },
  status: 200,
  message: "Success"
};
```

### Decorators

Decorators provide a way to add annotations and meta-programming syntax:

```typescript
// Class decorator
function sealed(constructor: Function) {
  Object.seal(constructor);
  Object.seal(constructor.prototype);
}

@sealed
class BugReport {
  type = "report";
  title: string;

  constructor(title: string) {
    this.title = title;
  }
}

// Method decorator
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;

  descriptor.value = function(...args: any[]) {
    console.log(`Calling ${propertyKey} with`, args);
    return originalMethod.apply(this, args);
  };

  return descriptor;
}

class Calculator {
  @log
  add(a: number, b: number): number {
    return a + b;
  }
}
```

### Type Assertions

Tell the compiler to treat a value as a specific type:

```typescript
// Using 'as' syntax (recommended)
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;

// Using angle-bracket syntax (not recommended in JSX)
let strLength2: number = (<string>someValue).length;

// Non-null assertion
function processValue(value: string | null) {
  // Tell TypeScript that value is definitely not null
  console.log(value!.toUpperCase());
}

// Const assertion
const config = {
  endpoint: "https://api.example.com",
  timeout: 3000
} as const;

// config.timeout = 5000;  // ❌ Error: Cannot assign to 'timeout' because it is read-only
```
