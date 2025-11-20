# ⚡ Vite

A comprehensive reference guide for Vite, the next-generation frontend build tool that provides a faster and leaner development experience for modern web projects.

## 📑 Table of Contents

- [🚀 Getting Started](#-getting-started)
  - [Create a New Vite Project](#create-a-new-vite-project)
  - [Project Templates](#project-templates)
- [⚙️ Configuration](#-configuration)
  - [vite.config.js](#viteconfigjs)
  - [Environment Variables](#environment-variables)
- [🔌 Plugins](#-plugins)
  - [Official Plugins](#official-plugins)
  - [Popular Community Plugins](#popular-community-plugins)
- [📦 Building for Production](#-building-for-production)
  - [Build Commands](#build-commands)
  - [Preview Production Build](#preview-production-build)
- [🎯 Core Features](#-core-features)
  - [Hot Module Replacement (HMR)](#hot-module-replacement-hmr)
  - [Static Asset Handling](#static-asset-handling)
  - [CSS Pre-processors](#css-pre-processors)
- [🔧 Development](#-development)
  - [Dev Server Options](#dev-server-options)
  - [Path Aliases](#path-aliases)
- [💡 Best Practices](#-best-practices)

---

## 🚀 Getting Started

### Create a New Vite Project

Interactive project creation (recommended):

```bash
  npm create vite@latest
```

This will prompt you to choose a project name and template.

### Project Templates

Create a project with a specific template directly:

**React with JavaScript:**
```bash
  npm create vite@latest my-project -- --template react
```

**React with TypeScript:**
```bash
  npm create vite@latest my-project -- --template react-ts
```

**Vue with JavaScript:**
```bash
  npm create vite@latest my-project -- --template vue
```

**Vue with TypeScript:**
```bash
  npm create vite@latest my-project -- --template vue-ts
```

**After creating a project:**
```bash
  cd my-project
  npm install
  npm run dev
```

---

## ⚙️ Configuration

### vite.config.js

Create a configuration file at the root of your project:

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true
  },
  build: {
    outDir: 'dist',
    sourcemap: true
  },
  resolve: {
    alias: {
      '@': '/src'
    }
  }
})
```

**Common configuration options:**

- `base` - Base public path when served in production
- `plugins` - Array of plugins to use
- `server` - Dev server options (port, host, proxy, etc.)
- `build` - Build options (outDir, minify, sourcemap, etc.)
- `resolve` - Resolution options (aliases, extensions, etc.)

### Environment Variables

Vite exposes environment variables on the special `import.meta.env` object.

**Create environment files:**

- `.env` - Loaded in all cases
- `.env.local` - Loaded in all cases, ignored by git
- `.env.[mode]` - Only loaded in specified mode (e.g., `.env.production`)
- `.env.[mode].local` - Only loaded in specified mode, ignored by git

**Example `.env` file:**

```dotenv
VITE_API_URL=https://api.example.com
VITE_APP_TITLE=My App
```

**Usage in code:**
```javascript
console.log(import.meta.env.VITE_API_URL)
console.log(import.meta.env.VITE_APP_TITLE)
```

**Built-in environment variables:**
- `import.meta.env.MODE` - The mode the app is running in
- `import.meta.env.PROD` - Whether the app is running in production
- `import.meta.env.DEV` - Whether the app is running in development
- `import.meta.env.BASE_URL` - The base URL the app is being served from

**Note:** Only variables prefixed with `VITE_` are exposed to your client-side code.

---

## 🔌 Plugins

### Official Plugins

**React:**
```bash
  npm install @vitejs/plugin-react -D
```

```javascript
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()]
})
```

**Vue:**
```bash
  npm install @vitejs/plugin-vue -D
```

```javascript
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()]
})
```

### Popular Community Plugins

**PWA Support:**
```bash
  npm install vite-plugin-pwa -D
```

**SVG as React Components:**
```bash
  npm install vite-plugin-svgr -D
```

**Environment Variables in HTML:**
```bash
  npm install vite-plugin-html -D
```

**Bundle Analyzer:**
```bash
  npm install rollup-plugin-visualizer -D
```

---

## 📦 Building for Production

### Build Commands

**Build for production:**
```bash
  npm run build
```

**Build with a custom output directory:**
```bash
  vite build --outDir custom-dist
```

**Build with custom mode:**
```bash
  vite build --mode staging
```

### Preview Production Build

Preview the production build locally:

```bash
npm run preview
```

Or specify a custom port:

```bash
  vite preview --port 8080
```

---

## 🎯 Core Features

### Hot Module Replacement (HMR)

Vite provides built-in HMR for instant updates during development without losing application state.

**HMR API for custom integrations:**
```javascript
if (import.meta.hot) {
  import.meta.hot.accept((newModule) => {
    // Handle hot update
  })
}
```

### Static Asset Handling

**Import assets as URLs:**
```javascript
import imgUrl from './img.png'
// imgUrl will be '/assets/img.2d8efhg.png' in production
```

**Import assets as strings:**
```javascript
import shaderString from './shader.glsl?raw'
```

**Import assets as Web Workers:**
```javascript
import Worker from './worker.js?worker'
const worker = new Worker()
```

### CSS Pre-processors

Vite provides built-in support for CSS pre-processors. Just install them:

**Sass/SCSS:**
```bash
  npm install sass -D
```

**Less:**
```bash
  npm install less -D
```

**Stylus:**
```bash
  npm install stylus -D
```

Then import them directly:
```javascript
import './styles.scss'
```

---

## 🔧 Development

### Dev Server Options

**Common server configurations:**

```javascript
export default defineConfig({
  server: {
    port: 3000,           // Port to run on
    open: true,           // Open browser on start
    cors: true,           // Enable CORS
    host: true,           // Listen on all addresses
    proxy: {              // Proxy API requests
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    },
    hmr: {                // HMR options
      overlay: true       // Show error overlay
    }
  }
})
```

### Path Aliases

Configure path aliases for cleaner imports:

```javascript
import { resolve } from 'path'

export default defineConfig({
  resolve: {
    alias: {
      '@': resolve(__dirname, './src'),
      '@components': resolve(__dirname, './src/components'),
      '@utils': resolve(__dirname, './src/utils'),
      '@assets': resolve(__dirname, './src/assets')
    }
  }
})
```

**Usage:**
```javascript
import Button from '@components/Button'
import { formatDate } from '@utils/date'
```

**For TypeScript projects, also update `tsconfig.json`:**
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"],
      "@assets/*": ["src/assets/*"]
    }
  }
}
```

---

## 💡 Best Practices

**1. Use Environment Variables Properly**
- Always prefix client-side variables with `VITE_`
- Never commit `.env.local` files
- Use different `.env` files for different environments

**2. Optimize Build Performance**
- Enable code splitting for large applications
- Use dynamic imports for lazy loading
- Minimize bundle size by analyzing with rollup-plugin-visualizer

**3. Development Server**
- Use proxy configuration for API calls to avoid CORS issues
- Enable HMR overlay for better error visibility
- Configure appropriate port to avoid conflicts

**4. Asset Management**
- Place static assets in the `public` directory for direct access
- Import assets as modules for cache busting and optimization
- Use appropriate asset loading strategies (URL, raw, worker)

**5. Configuration Organization**
- Keep configuration clean and well-commented
- Use environment-specific configs when needed
- Leverage TypeScript for type-safe configuration

**6. Plugin Usage**
- Only install plugins you actually need
- Keep plugins updated for better performance and security
- Check plugin compatibility with your Vite version

**7. Production Builds**
- Always test production builds locally with `vite preview`
- Enable source maps for easier debugging (when appropriate)
- Review bundle size and optimize if necessary
- Use appropriate build modes for different environments
