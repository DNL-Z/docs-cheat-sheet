# RUBY

## Install

```bash
brew install rbenv
```

## Operators

nil : rien
|| : ou
&& : et
<=> : différence (puts 1 <=> 2 return -1, puts 1 <=> 1 return 0)

## Appel a une variable

#\name\ ou "hello %s" % name

## Symbols

\:toto => 'coucou'\[:toto]

## Hashes

hash = \test: 'test'\
hash = \:test => 'test'\
hash = \'test' => 'test'\
hash[:test]

## Variables

* Local foo
* Globale $foo
* Instance @foo
* Classe @@foo
* Constants FOO

## Condition

unless = condition inverse /!\\ a utiliser pour de condition simple

## Les Class

class Car
  def initialize(door)
    @door = door
  end
  def door
    @door
  end
end
class Bus < Car // Héritage
  def driver
    true
  end
end
car = Car.new(3)
puts car.door
puts car.driver if car.respond_to?(:driver)

## Overwrite a Class

class String
  def bye
    p "good-bye #\self\"
  end
end
'John'.bye

## Modules

(* includes : ajoute en tant que méthode d'instance)
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
p door.open
p door.close
(* extends : ajoute en tant que méthode de class)
module Hello
  def say
    'hello'
  end
end
class Dog
  extends Hello
end
p Dog.say # Marche
p Dog.new.say # Marche pas  

## Iterators

10.times \ puts 'Hello' \
['1','2','3'].each \ |number| p number \
['1','2','3'].each_with_index \ |number, index| p "#\number\ #\index\" \

## Quelques méthodes utiles

.capitalize
.nil?
.empty?
.include? 'o'
var.push('toto') == var << ('toto')

## Tricky block

class String
  def do_some
    yield(self)
  end
end
"rober".do_some \ |ma_string| puts "coucou #\ma_string\"\

## **Ruby** on Rails

## Créer une nouvelle application

```bash
rails new « application_name »
```

## Lancer le serveur de l’application

```bash
rails server
```

Architecture d’un projet :
* app
* bin
* config
* db
* lib
* log
* public
* storage
* test
* vendor

## Pour créer un Controller avec l’action « index »

$
rails generate controller Welcome index

## (5 - rails.doc)

## Pour installer le Gemfile

```bash
bundle install
```

## Config de la db

=> config/database.yml

## Pour créer une migration

```bash
rails generate migration AddWebsiteModel
```

## Connaitre les routes dispo

```bash
rake routes
```

Exemple de Partial :
=> _field.html.erb

## Pour créer les db

```bash
rake db:create
```

## Créer un fichier de bdd

```bash
rails g migration « name »
```

## Faire la migration du fichier de bdd crée

```bash
rake db:migrate
```

## Pour revenir a la migration précédente

```bash
rake db:rollback
```

## Pour installer rspec

```bash
rails generate rspec:install
```
