# 🐦‍⬛ Swift

General-purpose compiled programming language developed by Apple for iOS, macOS, watchOS, and tvOS development.

## 📑 Table of Contents

- [📦 Variables and Types](#-variables-and-types)
  - [Variable Declaration](#variable-declaration)
  - [Type Annotation](#type-annotation)
  - [String Interpolation](#string-interpolation)
- [🔤 String Manipulation](#-string-manipulation)
  - [Converting Types to String](#converting-types-to-string)
- [💡 Basic Concepts](#-basic-concepts)
  - [Optionals](#optionals)
  - [Control Flow](#control-flow)

---

## 📦 Variables and Types

### Variable Declaration

```swift
// Variable (mutable)
var counter: Int

// Constant (immutable)
let maxValue: Int = 100
```

### Type Annotation

Swift uses **type inference**, but you can explicitly declare types:

```swift
var counter: Int
var text: String = "11"
var price: Double = 9.99
var isActive: Bool = true
```

### String Interpolation

Use `\()` to insert variables or expressions into strings:

```swift
var counter = 42
label.text = "\(counter)"
// Output: "42"

let name = "John"
print("Hello, \(name)!")
// Output: "Hello, John!"
```

---

## 🔤 String Manipulation

### Converting Types to String

Swift automatically converts values to strings within string interpolation:

```swift
let number: Int = 100
let text: String = "\(number)"
// text is now "100"

let price: Double = 19.99
let message = "Price: $\(price)"
// message is "Price: $19.99"
```

---

## 💡 Basic Concepts

### Optionals

**Optionals** represent a value that can be either present or `nil`:

```swift
var optionalString: String?
var optionalInt: Int? = nil

// Unwrapping optionals
if let unwrapped = optionalString {
    print(unwrapped)
} else {
    print("Value is nil")
}
```

### Control Flow

```swift
// If statement
if condition {
    // code
} else if otherCondition {
    // code
} else {
    // code
}

// For loop
for i in 0..<5 {
    print(i)
}

// While loop
while condition {
    // code
}

// Switch statement
switch value {
case 1:
    print("One")
case 2:
    print("Two")
default:
    print("Other")
}
```
