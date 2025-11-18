# 📦 Package Managers

Comparison of Node.js package managers: npm, yarn, and pnpm. These tools manage project dependencies, install packages, and maintain lock files for consistent installations.

## 📑 Table of Contents

- [📥 Installing Dependencies](#-installing-dependencies)
- [➕ Adding Packages](#-adding-packages)
- [🔄 Updating Packages](#-updating-packages)
- [🌍 Global Installation](#-global-installation)
- [🗑️ Removing Packages](#-removing-packages)
- [🏃 Running Scripts](#-running-scripts)
- [📊 Package Information](#-package-information)
- [🧹 Cleanup Commands](#-cleanup-commands)
- [⚡ Performance Tips](#-performance-tips)

---

## 📥 Installing Dependencies

**Install all dependencies from package.json**

| npm | yarn | pnpm |
|-----|--------------------------|------|
| `npm install` | `yarn` or `yarn install` | `pnpm install` |

This command installs all dependencies listed in package.json and generates a lock file (package-lock.json, yarn.lock, or pnpm-lock.yaml).

---

## ➕ Adding Packages

**Add a package and save it to dependencies in package.json**

| npm | yarn | pnpm |
|-----|------|------|
| `npm install <package>` | `yarn add <package>` | `pnpm add <package>` |

**Add a package as a dev dependency**

| npm | yarn | pnpm |
|-----|------|------|
| `npm install <package> --save-dev` | `yarn add <package> --dev` | `pnpm add <package> --save-dev` |

**Add a specific version**

| npm | yarn | pnpm |
|-----|------|------|
| `npm install <package>@<version>` | `yarn add <package>@<version>` | `pnpm add <package>@<version>` |

---

## 🔄 Updating Packages

**Update dependencies according to version ranges in package.json**

| npm | yarn | pnpm |
|-----|------|------|
| `npm update` | `yarn upgrade` | `pnpm update` |

A new lock file will be generated after the update.

**Update a specific package**

| npm | yarn | pnpm |
|-----|------|------|
| `npm update <package>` | `yarn upgrade <package>` | `pnpm update <package>` |

**Update to the latest version (ignoring semver)**

| npm | yarn | pnpm |
|-----|------|------|
| `npm install <package>@latest` | `yarn upgrade <package> --latest` | `pnpm update <package> --latest` |

---

## 🌍 Global Installation

**Install a package globally on the operating system**

| npm | yarn | pnpm |
|-----|------|------|
| `npm install <package> -g` | `yarn global add <package>` | `pnpm add <package> -g` |

**List global packages**

| npm | yarn | pnpm |
|-----|------|------|
| `npm list -g --depth=0` | `yarn global list` | `pnpm list -g` |

---

## 🗑️ Removing Packages

**Remove a dependency and its reference from package.json**

| npm | yarn | pnpm |
|-----|------|------|
| `npm uninstall <package>` | `yarn remove <package>` | `pnpm remove <package>` |

**Remove a global package**

| npm | yarn | pnpm |
|-----|------|------|
| `npm uninstall <package> -g` | `yarn global remove <package>` | `pnpm remove <package> -g` |

---

## 🏃 Running Scripts

**Execute a script defined in package.json**

| npm | yarn | pnpm |
|-----|------|------|
| `npm run <script>` | `yarn run <script>` or `yarn <script>` | `pnpm run <script>` or `pnpm <script>` |

**Execute a package binary (without installing globally)**

NPX is a tool for executing Node packages without installing them globally.

| npx | yarn | pnpm |
|-----|------|------|
| `npx <package>` | `yarn dlx <package>` | `pnpm dlx <package>` |

Example: `npx create-react-app my-app`

---

## 📊 Package Information

**View package information**

| npm | yarn | pnpm |
|-----|------|------|
| `npm info <package>` | `yarn info <package>` | `pnpm view <package>` |

**List installed packages**

| npm | yarn | pnpm |
|-----|------|------|
| `npm list` | `yarn list` | `pnpm list` |

**Check for outdated packages**

| npm | yarn | pnpm |
|-----|------|------|
| `npm outdated` | `yarn outdated` | `pnpm outdated` |

---

## 🧹 Cleanup Commands

**Clear cache**

| npm | yarn | pnpm |
|-----|------|------|
| `npm cache clean --force` | `yarn cache clean` | `pnpm store prune` |

**Remove node_modules and reinstall**

```bash
  rm -rf node_modules package-lock.json
  npm install

  rm -rf node_modules yarn.lock
  yarn install

  rm -rf node_modules pnpm-lock.yaml
  pnpm install
```

---

## ⚡ Performance Tips

**Speed comparison (generally):**
- **pnpm** 🥇 Fastest (uses hard links, shared store)
- **yarn** 🥈 Fast (parallel installation, offline cache)
- **npm** 🥉 Standard (improved significantly in recent versions)

**Disk space:**
- **pnpm** 💾 Most efficient (single shared store)
- **yarn** 💾 Moderate (offline cache)
- **npm** 💾 Each project has its own node_modules

**Key features:**

| Feature | npm | yarn | pnpm |
|---------|-----|------|------|
| Lock file | ✅ package-lock.json | ✅ yarn.lock | ✅ pnpm-lock.yaml |
| Workspaces | ✅ | ✅ | ✅ |
| Plug'n'Play | ❌ | ✅ | ❌ |
| Content addressable | ❌ | ❌ | ✅ |
| Strict mode | ❌ | ❌ | ✅ (default) |
