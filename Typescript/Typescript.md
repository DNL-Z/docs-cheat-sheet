# **TypeScript**

## Interface vs. Type

> Type aliases and interfaces are very similar, and in many cases you can choose between them freely. Almost all features of an interface are available in type, the **key** distinction is that a type cannot be re-opened to add new properties vs an interface which is always extendable.

## Partial<T>

> Constructs a type with all properties of Type set to optional. This utility will return a type that represents all subsets of a given type.

## Set<T>

> Represents a collection of unique elements of type T. Unlike tables, sets « Set » do not allow to store duplicate values.

## Record<K, T>

> Is used to create an object type whose keys are of type K and values are of type T. K is usually a union of string or number literals, and T represents the type of values associated with these keys.
