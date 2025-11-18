# 🍺 HOMEBREW

**Homebrew** is a free and open-source package manager for macOS and Linux.

It simplifies the installation of software on Apple's operating system and Linux distributions, making it easy to install, update, and manage software packages from the command line.

**Formulae** are packages that contain source code to be compiled and installed.

**Casks** are pre-compiled applications that are installed with minimal transformation.

## 📑 Table of Contents
- [🔍 Information](#-information)
- [🔧 Maintenance](#-maintenance)
- [📦 Package Management](#-package-management)
- [🎯 Cask Management](#-cask-management)

---

## 🔍 Information

### Check Homebrew version

```bash
  brew --version
```

### Display help

```bash
  brew help
```

### Show package information

```bash
  brew info <package_name>
```

---

## 🔧 Maintenance

### Diagnose potential issues

```bash
  brew doctor
```

### Update Homebrew itself

```bash
  brew update
```

### Upgrade all installed packages

```bash
  brew upgrade
```

### Upgrade a specific package

```bash
  brew upgrade <package_name>
```

---

## 📦 Package Management

### List installed packages

```bash
  brew list
```

### Search for packages

```bash
  brew search <package_name>
```

### Install a package

```bash
  brew install <package_name>
```

### Uninstall a package

```bash
  brew uninstall <package_name>
```

---

## 🎯 Cask Management

Casks are used to install GUI applications on macOS.

### Install a cask

```bash
  brew install --cask <cask_name>
```

### Install a cask to a custom directory

```bash
  brew install --cask --appdir <custom_directory> <cask_name>
```

### Uninstall a cask

```bash
  brew uninstall --cask <cask_name>
```

### List installed casks

```bash
  brew list --cask
```

### Search for casks

```bash
  brew search --cask <cask_name>
```
