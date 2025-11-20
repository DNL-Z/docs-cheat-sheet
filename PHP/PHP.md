# 🐘 PHP

A comprehensive reference guide for PHP functions, object-oriented programming concepts, and MySQL database operations.

## 📑 Table of Contents

- [🔧 Built-in Functions](#-built-in-functions)
  - [Array Functions](#array-functions)
  - [String Functions](#string-functions)
  - [Numeric Functions](#numeric-functions)
  - [File System Functions](#file-system-functions)
  - [HTML Functions](#html-functions)
  - [Type Checking Functions](#type-checking-functions)
  - [Class/Object Functions](#classobject-functions)
- [⚙️ Operators](#-operators)
  - [Ternary Operator](#ternary-operator)
- [🎯 Object-Oriented Programming (OOP)](#-object-oriented-programming-oop)
  - [Classes and Objects](#classes-and-objects)
  - [Constructor](#constructor)
  - [Visibility (Access Modifiers)](#visibility-access-modifiers)
  - [Constants](#constants)
  - [Static Members](#static-members)
  - [Scope Resolution Operator](#scope-resolution-operator)
  - [Getters and Setters](#getters-and-setters)
  - [Abstract Classes](#abstract-classes)
  - [Object Hydration](#object-hydration)
- [🗄️ MySQL Database](#-mysql-database)
  - [Connection Commands](#connection-commands)
  - [Import/Export Operations](#importexport-operations)
  - [PDO Extension](#pdo-extension)
  - [Query Execution](#query-execution)

---

## 🔧 Built-in Functions

### Array Functions

**`count()`** — Counts all elements in an array or something in an object

```php
$array = [1, 2, 3, 4, 5];
echo count($array); // Output: 5
```

**`ksort()`** — Sorts an array by keys

```php
$array = ['b' => 2, 'a' => 1];
ksort($array);
```

### String Functions

**`trim()`** — Removes whitespace or other characters from the beginning and end of a string

```php
$text = "  Hello World  ";
echo trim($text); // Output: "Hello World"
```

**`iconv_strlen()`** — Returns the number of characters in a string

```php
$text = "Hello";
echo iconv_strlen($text); // Output: 5
```

**`strlen()`** — Calculates the length of a string

```php
echo strlen("Hello"); // Output: 5
```

**`strpos()`** — Finds the position of the first occurrence in a string

```php
$text = "Hello World";
echo strpos($text, "World"); // Output: 6
```

**`strval()`** — Gets the string value of a variable

```php
$number = 123;
echo strval($number); // Output: "123"
```

**`str_repeat()`** — Repeats a string

```php
echo str_repeat("Ha", 3); // Output: "HaHaHa"
```

**`str_replace()`** — Replaces all occurrences in a string

```php
$text = "Hello World";
echo str_replace("World", "PHP", $text); // Output: "Hello PHP"
```

**`substr()`** — Returns a substring

```php
$text = "Hello World";
echo substr($text, 0, 5); // Output: "Hello"
```

**`strtoupper()`** — Returns a string in uppercase

```php
echo strtoupper("hello"); // Output: "HELLO"
```

### Numeric Functions

**`round()`** — Rounds a floating-point number

```php
$number = 3.14159;
echo round($number, 2); // Output: 3.14 (two decimal places)
```

**`rand()`** — Generates a random value

```php
$random = rand(0, 100); // Random number between 0 and 100
```

**`mt_rand()`** — Generates a random value using the Mersenne Twister algorithm

```php
$random = mt_rand(1, 10); // Random number between 1 and 10
```

### File System Functions

**`is_dir()`** — Checks if the file is a directory

```php
if (is_dir('/path/to/folder')) {
    echo "It's a directory";
}
```

**`scandir()`** — Lists files and directories in a folder

```php
$files = scandir('/path/to/folder');
```

**`unlink()`** — Deletes a file

```php
unlink('/path/to/file.txt');
```

### HTML Functions

**`htmlspecialchars()`** — Converts special characters to HTML entities

```php
$text = "<script>alert('XSS')</script>";
echo htmlspecialchars($text);
```

**`nl2br()`** — Inserts HTML line breaks before all newlines

```php
$text = "Line 1\nLine 2";
echo nl2br($text);
```

### Type Checking Functions

**`empty()`** — Determines if a variable is empty (use `!empty()` to check if not empty)

```php
$var = "";
if (empty($var)) {
    echo "Variable is empty";
}
```

**`isset()`** — Determines if a variable is declared and is different from NULL

```php
$var = "value";
if (isset($var)) {
    echo "Variable is set";
}
```

**`is_null()`** — Checks if a variable is NULL

```php
$var = null;
if (is_null($var)) {
    echo "Variable is NULL";
}
```

### Class/Object Functions

**`method_exists()`** — Checks if a method exists for a class

```php
if (method_exists($object, 'methodName')) {
    echo "Method exists";
}
```

### Variable Functions

**`unset()`** — Destroys a variable (removes the value assigned to a variable)

```php
$var = "value";
unset($var); // Variable no longer exists
```

---

## ⚙️ Operators

### Ternary Operator

The ternary operator can be considered as an inline `if` statement. It consists of three parts: an operator and two results.

**Syntax:**

```php
$value = <condition> ? <true value> : <false value>
```

**Shorthand syntax:**

```php
$value = <condition> ?: <false value>
```

If `<condition>` is true, the value of `<true value>` is returned, otherwise `<false value>`.

**Example:**

```php
$age = 18;
$status = ($age >= 18) ? "Adult" : "Minor";
echo $status; // Output: "Adult"
```

---

## 🎯 Object-Oriented Programming (OOP)

### Classes and Objects

A **class** is an entity that groups variables and functions together. Each of these functions has access to the variables of this entity.

- An **attribute** refers to a **variable** stored in the class
- A **method** refers to a **function** stored in the class

An **instance** is simply the result of instantiation. Instantiation is the act of instantiating a class. To instantiate a class means to use a class so that it creates an object for us. In short, an **instance** is an **object**.

```php
class Person {
    public $name;
    public $age;

    public function greet() {
        echo "Hello, my name is " . $this->name;
    }
}

$person = new Person(); // Creating an instance
$person->name = "John";
$person->greet();
```

### Constructor

**`__construct()`** — Executed as soon as the object is created

The constructor serves to initialize object attributes upon creation without knowing their values in advance. No value should be returned, even though it won't generate an error.

```php
class Person {
    private $name;
    private $age;

    public function __construct($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }
}

$person = new Person("John", 30);
```

### Visibility (Access Modifiers)

**`public`** — If an attribute or method is public, it can be accessed from anywhere, both from inside the object (in the methods we created) and from outside

**`private`** — Imposes restrictions. Attributes and methods can only be accessed from inside the class

**`protected`** — Can be accessed within the class and by inheriting classes (see inheritance concept)

```php
class Example {
    public $publicVar = "Public";
    private $privateVar = "Private";
    protected $protectedVar = "Protected";
}
```

### Constants

A **class constant** is a type of attribute belonging to the class whose value never changes.

```php
class Math {
    const PI = 3.14159;

    public function getCircleArea($radius) {
        return self::PI * $radius * $radius;
    }
}

echo Math::PI;
```

### Static Members

**Static attributes** and **static methods** belong to the class and not to an object. All objects have access to this attribute, and it has the same value for all objects.

```php
class Counter {
    private static $count = 0;

    public static function increment() {
        self::$count++;
    }

    public static function getCount() {
        return self::$count;
    }
}

Counter::increment();
echo Counter::getCount(); // Output: 1
```

Static attributes are not accessed with `$this`, but with `self::`.

### Scope Resolution Operator

**The scope resolution operator `::`** allows access to an element of a class.

**`self::`** means "myself" and refers to the class.

```php
class Example {
    private static $staticVar = "Static value";

    public static function getStaticVar() {
        return self::$staticVar;
    }
}
```

### Getters and Setters

A **getter** is a method responsible for returning the value of an attribute.

A **setter** is a method responsible for assigning a value to an attribute while verifying its integrity.

```php
class Person {
    private $age;

    // Getter
    public function getAge() {
        return $this->age;
    }

    // Setter
    public function setAge($age) {
        if ($age > 0 && $age < 150) {
            $this->age = $age;
        }
    }
}
```

### Abstract Classes

PHP 5 introduced the concepts of abstract classes and abstract methods. Classes defined as abstract cannot be instantiated. Any class containing at least one abstract method must also be abstract.

Abstract methods simply declare the method signature - they cannot define its implementation.

```php
abstract class Animal {
    abstract public function makeSound();

    public function sleep() {
        echo "Sleeping...";
    }
}

class Dog extends Animal {
    public function makeSound() {
        echo "Woof!";
    }
}
```

### Object Hydration

**Hydrating an object** means simply providing it with what it needs to function. More precisely, hydrating an object involves providing it with data corresponding to its attributes so that it assigns the desired values to them. The object will thus have valid attributes and be valid itself.

```php
class Person {
    private $name;
    private $age;

    public function hydrate(array $data) {
        foreach ($data as $key => $value) {
            $method = 'set' . ucfirst($key);
            if (method_exists($this, $method)) {
                $this->$method($value);
            }
        }
    }

    public function setName($name) {
        $this->name = $name;
    }

    public function setAge($age) {
        $this->age = $age;
    }
}

$person = new Person();
$person->hydrate(['name' => 'John', 'age' => 30]);
```

---

## 🗄️ MySQL Database

### Connection Commands

**Connect to a MySQL database**

```bash
  mysql -uroot -p
```

**Local MAMP connection**

```bash
  /Applications/MAMP/Library/bin/mysql --host=localhost -uroot -proot
```

### Import/Export Operations

**Import a .sql file into a database**

```bash
  mysql -u root -ppassword database_name < filename.sql
```

**Export a database to a .sql file**

```bash
  mysqldump -u root -ppassword database_name > filename.sql
```

### PDO Extension

PDO (PHP Data Objects) is a complete tool that allows access to any type of database. It can be used to connect to MySQL, PostgreSQL, Oracle, and more.

### Query Execution

**PDO connection to MySQL:**

```php
$bdd = new PDO('mysql:host=localhost;dbname=database_name;charset=utf8', 'username', 'password');
```

**Retrieving content from table X:**

```php
$reponse = $bdd->query('SELECT * FROM X');
```

**Displaying each entry one by one:**

```php
while($data = $reponse->fetch()) {
    echo $data['name'];
}
```

**For normal queries:**

**`exec()`** — Executes an SQL query and returns the number of affected rows

**For prepared queries:**

**`prepare()`** — Prepares a query for execution and returns an object (use for forms)

**`execute()`** — Executes a prepared query

```php
$stmt = $bdd->prepare('SELECT * FROM users WHERE email = :email');
$stmt->execute(['email' => $email]);
$user = $stmt->fetch();
```

**`fetch()`** — Fetches the next row from a result set

**Closing the cursor:**

```php
$reponse->closeCursor();
```

Close the cursor after you have finished processing the return of a query to avoid problems with the next query. This indicates that the work on the query is complete.
