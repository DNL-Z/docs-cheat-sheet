# 🌿 Twig

Flexible, fast, and secure template engine for PHP applications.

## 📑 Table of Contents

- [🔤 Expression Syntax](#-expression-syntax)
- [🔧 Operators](#-operators)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Comparison Operators](#comparison-operators)
  - [Logical Operators](#logical-operators)
  - [String Operators](#string-operators)

---

## 🔤 Expression Syntax

Expressions can be used in `{% blocks %}` and `{{ expressions }}`.

```twig
{# Variable output #}
{{ variable }}

{# Control structure #}
{% if condition %}
    Content
{% endif %}
```

---

## 🔧 Operators

### Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Converts both arguments to a number and adds them | `{{ 5 + 3 }}` → `8` |
| `-` | Converts both arguments to a number and subtracts them | `{{ 10 - 4 }}` → `6` |
| `*` | Converts both arguments to a number and multiplies them | `{{ 3 * 7 }}` → `21` |
| `/` | Converts both arguments to a number and divides them | `{{ 20 / 4 }}` → `5` |
| `%` | Converts both arguments to a number and returns the remainder | `{{ 10 % 3 }}` → `1` |

### Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Is the left expression equal to the right expression? | `{{ 5 == 5 }}` → `true` |
| `!=` | Is the left expression not equal to the right expression? | `{{ 5 != 3 }}` → `true` |
| `<` | Is the left expression less than the right expression? | `{{ 3 < 5 }}` → `true` |
| `>` | Is the left expression greater than the right expression? | `{{ 7 > 5 }}` → `true` |
| `<=` | Is the left expression less than or equal to the right? | `{{ 5 <= 5 }}` → `true` |
| `>=` | Is the left expression greater than or equal to the right? | `{{ 5 >= 3 }}` → `true` |

### Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `or` | True if the left or right expression is true | `{{ true or false }}` → `true` |
| `and` | True if both left and right expressions are true | `{{ true and false }}` → `false` |
| `not` | Negates the expression | `{{ not false }}` → `true` |

### String Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `~` | Converts both arguments to a string and concatenates them | `{{ "Hello" ~ " World" }}` → `"Hello World"` |
