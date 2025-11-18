# 🚫 GITIGNORE

**.gitignore** is a text file that tells Git which files or folders to ignore in a project. It helps keep your repository clean by excluding files that shouldn't be version controlled, such as dependencies, build outputs, environment files, and system-specific files.

## 📑 Table of Contents
- [📋 React/Next.js Template](#reactnextjs-template)
- [📦 Dependencies](#dependencies)
- [🧪 Testing](#testing)
- [🏗️ Production](#production)
- [📁 Miscellaneous](#miscellaneous)
- [🐛 Debug Files](#debug-files)
- [🔐 Environment Files](#environment-files)
- [☁️ Vercel](#vercel)
- [📘 TypeScript](#typescript)
- [💡 JetBrains IDEs](#jetbrains-ides)

---

## 📋 React/Next.js Template

Example of a complete **.gitignore** file for React or Next.js projects:

```gitignore
# Dependencies
/node_modules
/.pnp
.pnp.js

# Testing
/coverage

# Production
/build

# Miscellaneous
.DS_Store
*.pem

# Debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Environment files
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Vercel
.vercel

# TypeScript
*.tsbuildinfo
next-env.d.ts

# JetBrains IDEs
.idea
```

---

## 📦 Dependencies

Ignore package manager dependencies and cache files:

```gitignore
/node_modules
/.pnp
.pnp.js
```

---

## 🧪 Testing

Ignore test coverage reports:

```gitignore
/coverage
```

---

## 🏗️ Production

Ignore build output directories:

```gitignore
/build
```

---

## 📁 Miscellaneous

Ignore system files and sensitive files:

```gitignore
.DS_Store
*.pem
```

- **.DS_Store**: macOS system file
- **\*.pem**: Private key files

---

## 🐛 Debug Files

Ignore package manager debug logs:

```gitignore
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

---

## 🔐 Environment Files

Ignore environment configuration files containing sensitive data:

```gitignore
.env
.env.local
.env.development.local
.env.test.local
.env.production.local
```

⚠️ **Warning**: Never commit environment files containing API keys, passwords, or other sensitive information.

---

## ☁️ Vercel

Ignore Vercel deployment configuration:

```gitignore
.vercel
```

---

## 📘 TypeScript

Ignore TypeScript build information and generated files:

```gitignore
*.tsbuildinfo
next-env.d.ts
```

---

## 💡 JetBrains IDEs

Ignore JetBrains IDE configuration files (IntelliJ IDEA, WebStorm, etc.):

```gitignore
.idea
```
