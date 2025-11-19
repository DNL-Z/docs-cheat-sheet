# 💎 Ruby

Dynamic, object-oriented programming language focused on simplicity and productivity, with an elegant syntax that is natural to read and easy to write.

## 📑 Table of Contents

- [⚙️ Installation](#-installation)
- [🔤 Operators and Syntax](#-operators-and-syntax)
  - [Basic Operators](#basic-operators)
  - [Variable Interpolation](#variable-interpolation)
- [📦 Data Structures](#-data-structures)
  - [Symbols](#symbols)
  - [Hashes](#hashes)
- [🔧 Variables](#-variables)
  - [Variable Types](#variable-types)
- [🎯 Control Flow](#-control-flow)
  - [Unless Statement](#unless-statement)
- [🏗️ Classes and Objects](#-classes-and-objects)
  - [Defining Classes](#defining-classes)
  - [Inheritance](#inheritance)
  - [Overwriting Classes](#overwriting-classes)
- [📚 Modules](#-modules)
  - [Include (Instance Methods)](#include-instance-methods)
  - [Extend (Class Methods)](#extend-class-methods)
- [🔁 Iterators](#-iterators)
- [🛠️ Useful Methods](#-useful-methods)
- [⚡ Advanced Blocks](#-advanced-blocks)
- [🚂 Ruby on Rails](#-ruby-on-rails)
  - [Getting Started](#getting-started)
  - [Generators](#generators)
  - [Database Management](#database-management)
  - [Project Architecture](#project-architecture)
  - [Testing](#testing)

---

## ⚙️ Installation

Install Ruby using rbenv (Ruby version manager):

```bash
  brew install rbenv
```

---

## 🔤 Operators and Syntax

### Basic Operators

- **nil**: represents nothing/null
- **||**: logical OR
- **&&**: logical AND
- **<=>**: spaceship operator (comparison)
  - Returns `-1` if left is less than right
  - Returns `0` if left equals right
  - Returns `1` if left is greater than right

```ruby
puts 1 <=> 2  # returns -1
puts 1 <=> 1  # returns 0
puts 2 <=> 1  # returns 1
```

### Variable Interpolation

```ruby
# Using interpolation
"Hello #{name}"

# Using string formatting
"Hello %s" % name
```

---

## 📦 Data Structures

### Symbols

Symbols are immutable identifiers, prefixed with a colon:

```ruby
hash = { :toto => 'coucou' }
hash[:toto]  # returns 'coucou'
```

### Hashes

Hashes are key-value pairs (similar to dictionaries in other languages):

```ruby
# Modern syntax (symbol keys)
hash = { test: 'test' }

# Traditional syntax (symbol keys)
hash = { :test => 'test' }

# String keys
hash = { 'test' => 'test' }

# Accessing values
hash[:test]
```

---

## 🔧 Variables

### Variable Types

- **Local**: `foo` - accessible within current scope
- **Global**: `$foo` - accessible everywhere
- **Instance**: `@foo` - accessible within instance of a class
- **Class**: `@@foo` - shared across all instances of a class
- **Constants**: `FOO` - should not be changed

---

## 🎯 Control Flow

### Unless Statement

Inverse condition (use only for simple conditions):

```ruby
# Executes if condition is false
unless user.logged_in?
  redirect_to login_path
end
```

---

## 🏗️ Classes and Objects

### Defining Classes

```ruby
class Car
  def initialize(door)
    @door = door
  end

  def door
    @door
  end
end

car = Car.new(3)
puts car.door
```

### Inheritance

```ruby
class Bus < Car
  def driver
    true
  end
end

bus = Bus.new(4)
puts bus.door  # inherited from Car
puts bus.driver if bus.respond_to?(:driver)
```

### Overwriting Classes

You can add methods to existing classes (monkey patching):

```ruby
class String
  def bye
    p "good-bye #{self}"
  end
end

'John'.bye  # outputs: "good-bye John"
```

---

## 📚 Modules

### Include (Instance Methods)

Adds methods as instance methods:

```ruby
module Automatic
  def open
    'open'
  end

  def close
    'close'
  end
end

class Door
  include Automatic
end

door = Door.new
p door.open   # works
p door.close  # works
```

### Extend (Class Methods)

Adds methods as class methods:

```ruby
module Hello
  def say
    'hello'
  end
end

class Dog
  extend Hello
end

p Dog.say       # works
p Dog.new.say   # doesn't work
```

---

## 🔁 Iterators

```ruby
# Repeat action n times
10.times { puts 'Hello' }

# Iterate over array
['1', '2', '3'].each { |number| p number }

# Iterate with index
['1', '2', '3'].each_with_index { |number, index| p "#{number} #{index}" }
```

---

## 🛠️ Useful Methods

```ruby
.capitalize      # Capitalizes first letter
.nil?           # Checks if value is nil
.empty?         # Checks if collection is empty
.include?('o')  # Checks if element exists

# Array operations
var.push('toto')  # equivalent to var << 'toto'
```

---

## ⚡ Advanced Blocks

Using `yield` to create custom block methods:

```ruby
class String
  def do_some
    yield(self)
  end
end

"robert".do_some { |my_string| puts "hello #{my_string}" }
# outputs: "hello robert"
```

---

## 🚂 Ruby on Rails

### Getting Started

Create a new Rails application:

```bash
  rails new application_name
```

Start the development server:

```bash
  rails server
```

### Project Architecture

Standard Rails project structure:

- **app**: Application code (models, views, controllers)
- **bin**: Binary executables
- **config**: Configuration files
- **db**: Database files
- **lib**: Library modules
- **log**: Log files
- **public**: Static files
- **storage**: Active Storage files
- **test**: Test files
- **vendor**: Third-party code

### Generators

Create a controller with an action:

```bash
  rails generate controller Welcome index
```

Create a migration:

```bash
  rails generate migration AddWebsiteModel
```

Shorter syntax:

```bash
  rails g migration migration_name
```

### Database Management

Install dependencies from Gemfile:

```bash
  bundle install
```

Database configuration:

```
config/database.yml
```

Create databases:

```bash
  rake db:create
```

Run migrations:

```bash
  rake db:migrate
```

Rollback last migration:

```bash
  rake db:rollback
```

### Routes

View available routes:

```bash
  rake routes
```

### Partials

Partial files start with an underscore:

```
_field.html.erb
```

### Testing

Install RSpec for testing:

```bash
  rails generate rspec:install
```
