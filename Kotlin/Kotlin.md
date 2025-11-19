# 🟣 Kotlin

Statically typed, cross-platform programming language developed by JetBrains for modern multiplatform applications, Android development, and JVM-based systems.

## 📑 Table of Contents

- [📦 Variables and Types](#-variables-and-types)
  - [Variable Declaration](#variable-declaration)
  - [Type Inference](#type-inference)
  - [Nullable Types](#nullable-types)
- [🔤 String Manipulation](#-string-manipulation)
  - [String Templates](#string-templates)
  - [String Methods](#string-methods)
- [🧮 Collections](#-collections)
  - [Lists](#lists)
  - [Maps](#maps)
  - [Sets](#sets)
- [🎯 Functions](#-functions)
  - [Function Declaration](#function-declaration)
  - [Lambda Expressions](#lambda-expressions)
  - [Extension Functions](#extension-functions)
- [💡 Basic Concepts](#-basic-concepts)
  - [Control Flow](#control-flow)
  - [When Expression](#when-expression)
  - [Null Safety](#null-safety)
- [🔧 Object-Oriented Programming](#-object-oriented-programming)
  - [Classes](#classes)
  - [Data Classes](#data-classes)
  - [Object Declaration](#object-declaration)

---

## 📦 Variables and Types

### Variable Declaration

```kotlin
// Mutable variable
var counter: Int = 0

// Immutable variable (constant)
val maxValue: Int = 100

// Type inference
var text = "Hello"  // String inferred
val number = 42     // Int inferred
```

### Type Inference

Kotlin automatically infers types when they can be determined from context:

```kotlin
val name = "Alice"        // String
val age = 30              // Int
val price = 19.99         // Double
val isActive = true       // Boolean
```

### Nullable Types

Types are **non-nullable** by default. Use `?` to allow null values:

```kotlin
var nonNullable: String = "Hello"
// nonNullable = null  // Compilation error

var nullable: String? = "Hello"
nullable = null  // OK
```

---

## 🔤 String Manipulation

### String Templates

Use `$` for variable interpolation and `${}` for expressions:

```kotlin
val name = "Alice"
val age = 30

println("Hello, $name!")
// Output: "Hello, Alice!"

println("Next year, you'll be ${age + 1}")
// Output: "Next year, you'll be 31"
```

### String Methods

```kotlin
val text = "Hello World"

text.uppercase()         // "HELLO WORLD"
text.lowercase()         // "hello world"
text.length              // 11
text.substring(0, 5)     // "Hello"
text.contains("World")   // true
text.split(" ")          // ["Hello", "World"]
```

---

## 🧮 Collections

### Lists

```kotlin
// Immutable list
val numbers = listOf(1, 2, 3, 4, 5)

// Mutable list
val mutableNumbers = mutableListOf(1, 2, 3)
mutableNumbers.add(4)

// Access elements
println(numbers[0])       // 1
println(numbers.first())  // 1
println(numbers.last())   // 5
```

### Maps

```kotlin
// Immutable map
val ages = mapOf("Alice" to 30, "Bob" to 25)

// Mutable map
val mutableAges = mutableMapOf("Alice" to 30)
mutableAges["Bob"] = 25

// Access elements
println(ages["Alice"])  // 30
```

### Sets

```kotlin
// Immutable set
val uniqueNumbers = setOf(1, 2, 3, 2, 1)  // [1, 2, 3]

// Mutable set
val mutableSet = mutableSetOf(1, 2, 3)
mutableSet.add(4)
```

---

## 🎯 Functions

### Function Declaration

```kotlin
// Basic function
fun greet(name: String): String {
    return "Hello, $name"
}

// Single-expression function
fun add(a: Int, b: Int): Int = a + b

// Function with default parameters
fun greet(name: String = "Guest"): String {
    return "Hello, $name"
}

// Unit return type (like void)
fun printMessage(message: String): Unit {
    println(message)
}
```

### Lambda Expressions

```kotlin
// Lambda syntax
val sum = { a: Int, b: Int -> a + b }
println(sum(2, 3))  // 5

// Lambda with collections
val numbers = listOf(1, 2, 3, 4, 5)
val doubled = numbers.map { it * 2 }
// [2, 4, 6, 8, 10]

val evens = numbers.filter { it % 2 == 0 }
// [2, 4]
```

### Extension Functions

Add functionality to existing classes without inheritance:

```kotlin
fun String.addExclamation(): String {
    return this + "!"
}

val result = "Hello".addExclamation()
// Output: "Hello!"
```

---

## 💡 Basic Concepts

### Control Flow

```kotlin
// If expression
val max = if (a > b) a else b

// For loop
for (i in 1..5) {
    println(i)
}

// For loop with step
for (i in 0..10 step 2) {
    println(i)  // 0, 2, 4, 6, 8, 10
}

// Iterate over collection
val items = listOf("apple", "banana", "cherry")
for (item in items) {
    println(item)
}

// While loop
var x = 5
while (x > 0) {
    println(x)
    x--
}
```

### When Expression

A powerful replacement for switch statements:

```kotlin
val x = 2
when (x) {
    1 -> println("One")
    2 -> println("Two")
    in 3..10 -> println("Between 3 and 10")
    else -> println("Other")
}

// When as expression
val result = when (x) {
    1 -> "One"
    2 -> "Two"
    else -> "Other"
}
```

### Null Safety

Kotlin provides built-in null safety features:

```kotlin
// Safe call operator
val length = text?.length

// Elvis operator (default value if null)
val length = text?.length ?: 0

// Not-null assertion
val length = text!!.length  // Throws exception if text is null

// Safe cast
val number = value as? Int  // Returns null if cast fails
```

---

## 🔧 Object-Oriented Programming

### Classes

```kotlin
// Basic class
class Person(val name: String, var age: Int) {
    fun introduce() {
        println("Hi, I'm $name and I'm $age years old")
    }
}

val person = Person("Alice", 30)
person.introduce()
```

### Data Classes

Automatically generates `equals()`, `hashCode()`, `toString()`, and `copy()`:

```kotlin
data class User(val name: String, val age: Int)

val user1 = User("Alice", 30)
val user2 = user1.copy(age = 31)

println(user1)  // User(name=Alice, age=30)
```

### Object Declaration

Create singleton objects:

```kotlin
object Database {
    val url = "jdbc://localhost"

    fun connect() {
        println("Connecting to $url")
    }
}

Database.connect()
```
