# 📦 Package.json

Configuration file for Node.js projects, defining dependencies, scripts, and project metadata with semantic versioning support.

## 📑 Table of Contents

- [🔢 Version Notation](#-version-notation)
  - [Tilde (~) - Patch Updates](#tilde--patch-updates)
  - [Caret (^) - Minor Updates](#caret--minor-updates)
  - [Exact Version](#exact-version)
  - [Wildcards (*, x, X)](#wildcards--x-x)
  - [Comparison Operators](#comparison-operators)
  - [Hyphen Ranges](#hyphen-ranges)
  - [Logical OR (||)](#logical-or-)
  - [Latest](#latest)

---

## 🔢 Version Notation

### Tilde (~) Patch Updates

**Approximately equivalent to version**

```json
{
  "dependencies": {
    "package-name": "~1.2.3"
  }
}
```

Will update you to all future **patch versions**, without incrementing the **minor** version.

- `~1.2.3` will use releases from `1.2.3` to `<1.3.0`
- `~1.2` is equivalent to `>=1.2.0 <1.3.0`
- `~1` is equivalent to `>=1.0.0 <2.0.0`

### Caret (^) Minor Updates

**Compatible with version**

```json
{
  "dependencies": {
    "package-name": "^1.2.3"
  }
}
```

Will update you to all future **minor/patch versions**, without incrementing the **major** version.

- `^1.2.3` will use releases from `1.2.3` to `<2.0.0`
- `^0.2.3` will use releases from `0.2.3` to `<0.3.0` (for 0.x versions)
- `^0.0.3` will use releases from `0.0.3` to `<0.0.4` (strict for 0.0.x)

### Exact Version

**Install a specific version**

```json
{
  "dependencies": {
    "package-name": "1.2.3"
  }
}
```

Will install **exactly** version `1.2.3`.

### Wildcards (*, x, X)

**Accept any version for the wildcard position**

```json
{
  "dependencies": {
    "package-name": "*",
    "another-package": "1.x",
    "third-package": "1.2.x"
  }
}
```

- `*` accepts any version
- `1.x` or `1.X` is equivalent to `>=1.0.0 <2.0.0`
- `1.2.x` or `1.2.*` is equivalent to `>=1.2.0 <1.3.0`

### Comparison Operators

**Use comparison operators for version ranges**

```json
{
  "dependencies": {
    "package-name": ">1.2.3",
    "another-package": ">=1.0.0",
    "third-package": "<2.0.0",
    "fourth-package": "<=1.5.0"
  }
}
```

- `>1.2.3` : Greater than version 1.2.3
- `>=1.2.3` : Greater than or equal to version 1.2.3
- `<2.0.0` : Less than version 2.0.0
- `<=1.5.0` : Less than or equal to version 1.5.0

**Combined ranges:**

```json
{
  "dependencies": {
    "package-name": ">=1.2.3 <2.0.0"
  }
}
```

### Hyphen Ranges

**Inclusive range between two versions**

```json
{
  "dependencies": {
    "package-name": "1.2.3 - 2.3.4"
  }
}
```

- `1.2.3 - 2.3.4` is equivalent to `>=1.2.3 <=2.3.4`
- `1.2 - 2.3` is equivalent to `>=1.2.0 <=2.3.x`

### Logical OR (||)

**Accept either version range**

```json
{
  "dependencies": {
    "package-name": "1.x || 2.x",
    "another-package": "<1.0.0 || >=2.0.0"
  }
}
```

Allows installation of versions that match **either** range.

### Latest

**Install the latest version**

```json
{
  "dependencies": {
    "package-name": "latest"
  }
}
```

Will always install the most recent version available.
