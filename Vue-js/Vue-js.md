# 🟢 Vue.js

A comprehensive reference guide for Vue.js, the progressive JavaScript framework for building user interfaces and single-page applications.

## 📑 Table of Contents

- [🚀 Getting Started](#-getting-started)
  - [Create a New Project](#create-a-new-project)
  - [GUI Tools](#gui-tools)
- [⚙️ Project Setup](#-project-setup)
  - [Using Vite (Recommended)](#using-vite-recommended)
  - [Using Vue CLI](#using-vue-cli)
  - [Installation](#installation)
- [🧪 Testing](#-testing)
  - [Jest Configuration](#jest-configuration)
  - [Vitest (Recommended for Vite)](#vitest-recommended-for-vite)
- [📦 Core Concepts](#-core-concepts)
  - [Vue 3 Composition API](#vue-3-composition-api)
  - [Vue 3 Options API](#vue-3-options-api)
  - [Component Basics](#component-basics)
  - [Props and Events](#props-and-events)
- [🔄 State Management](#-state-management)
  - [Pinia (Recommended)](#pinia-recommended)
  - [Vuex (Legacy)](#vuex-legacy)
- [🛣️ Routing](#-routing)
  - [Vue Router](#vue-router)
- [💡 Best Practices](#-best-practices)

---

## 🚀 Getting Started

### Create a New Project

**Using Vue CLI (legacy):**
```bash
  vue create my-project
```

Interactive prompts will guide you through selecting features.

### GUI Tools

Launch the Vue UI graphical interface:

```bash
  vue ui
```

This provides a visual interface for creating and managing Vue projects.

---

## ⚙️ Project Setup

### Using Vite (Recommended)

**Create a new Vue 3 project with Vite:**
```bash
  npm create vite@latest my-vue-app -- --template vue
```

**With TypeScript:**
```bash
  npm create vite@latest my-vue-app -- --template vue-ts
```

**After creating the project:**
```bash
  cd my-vue-app
  npm install
  npm run dev
```

### Using Vue CLI

**Create a new project:**
```bash
  vue create my-project
```

**Select preset:**
- Default (Vue 3)
- Default (Vue 2)
- Manually select features

**Start development server:**
```bash
  npm run serve
```

### Installation

**Install Vue 3 in an existing project:**
```bash
  npm install vue@next
```

**Install Vue 2:**
```bash
  npm install vue
```

---

## 🧪 Testing

### Jest Configuration

**For Vue CLI projects, configure Jest:**

Update `package.json` to include Jest configuration:

```json
{
  "jest": {
    "testEnvironment": "jsdom"
  }
}
```

**Install dependencies:**
```bash
  yarn add --save-dev vue-jest babel-jest @vue/test-utils
```

**Or with npm:**
```bash
  npm install --save-dev vue-jest babel-jest @vue/test-utils
```

### Vitest (Recommended for Vite)

**For Vite projects, use Vitest:**

```bash
  npm install --save-dev vitest @vue/test-utils jsdom
```

**Configure `vite.config.js`:**
```javascript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'jsdom'
  }
})
```

**Add test script to `package.json`:**
```json
{
  "scripts": {
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage"
  }
}
```

---

## 📦 Core Concepts

### Vue 3 Composition API

**Basic component structure:**

```vue
<script setup>
import { ref, computed, onMounted } from 'vue'

const count = ref(0)
const doubleCount = computed(() => count.value * 2)

function increment() {
  count.value++
}

onMounted(() => {
  console.log('Component mounted')
})
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>

<style scoped>
/* Component styles */
</style>
```

### Vue 3 Options API

**Basic component structure:**

```vue
<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  computed: {
    doubleCount() {
      return this.count * 2
    }
  },
  methods: {
    increment() {
      this.count++
    }
  },
  mounted() {
    console.log('Component mounted')
  }
}
</script>

<template>
  <div>
    <p>Count: {{ count }}</p>
    <p>Double: {{ doubleCount }}</p>
    <button @click="increment">Increment</button>
  </div>
</template>
```

### Component Basics

**Registering components:**

```javascript
// Global registration
import { createApp } from 'vue'
import MyComponent from './MyComponent.vue'

const app = createApp(App)
app.component('MyComponent', MyComponent)
```

```vue
<!-- Local registration -->
<script setup>
import MyComponent from './MyComponent.vue'
</script>

<template>
  <MyComponent />
</template>
```

### Props and Events

**Defining props:**

```vue
<script setup>
// Composition API
const props = defineProps({
  title: String,
  count: {
    type: Number,
    required: true,
    default: 0
  }
})
</script>
```

**Emitting events:**

```vue
<script setup>
const emit = defineEmits(['update', 'delete'])

function handleUpdate() {
  emit('update', { id: 1, value: 'new' })
}
</script>

<template>
  <button @click="handleUpdate">Update</button>
</template>
```

**Using in parent:**

```vue
<template>
  <ChildComponent
    :title="pageTitle"
    :count="counter"
    @update="handleUpdate"
  />
</template>
```

---

## 🔄 State Management

### Pinia (Recommended)

**Installation:**
```bash
  npm install pinia
```

**Setup in `main.js`:**
```javascript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const app = createApp(App)
app.use(createPinia())
app.mount('#app')
```

**Create a store:**
```javascript
// stores/counter.js
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)

  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
```

**Using the store:**
```vue
<script setup>
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
</script>

<template>
  <div>
    <p>{{ counter.count }}</p>
    <button @click="counter.increment">Increment</button>
  </div>
</template>
```

### Vuex (Legacy)

**Installation:**
```bash
  npm install vuex@next
```

**Basic store setup:**
```javascript
import { createStore } from 'vuex'

export default createStore({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++
    }
  },
  actions: {
    incrementAsync({ commit }) {
      setTimeout(() => {
        commit('increment')
      }, 1000)
    }
  },
  getters: {
    doubleCount: state => state.count * 2
  }
})
```

---

## 🛣️ Routing

### Vue Router

**Installation:**
```bash
  npm install vue-router@4
```

**Setup `router/index.js`:**
```javascript
import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/user/:id',
    name: 'User',
    component: () => import('@/views/User.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
```

**Register in `main.js`:**
```javascript
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
```

**Navigation:**
```vue
<template>
  <!-- Declarative -->
  <router-link to="/">Home</router-link>
  <router-link :to="{ name: 'User', params: { id: 123 }}">User</router-link>

  <!-- Router outlet -->
  <router-view />
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Programmatic navigation
function goToAbout() {
  router.push('/about')
}

// Access route params
console.log(route.params.id)
</script>
```

---

## 💡 Best Practices

**1. Use Composition API for Vue 3**
- Leverage `<script setup>` for cleaner, more concise code
- Use composables to extract and reuse stateful logic
- Prefer Composition API for better TypeScript support

**2. Component Organization**
- Keep components small and focused on a single responsibility
- Use proper naming conventions (PascalCase for components)
- Co-locate related files (component, tests, styles)

**3. State Management**
- Use Pinia instead of Vuex for new projects
- Keep stores focused and modular
- Avoid storing derived state; use computed properties

**4. Performance Optimization**
- Use `v-show` for frequently toggled elements
- Use `v-if` for conditional rendering that rarely changes
- Implement lazy loading for routes and components
- Use `v-memo` for expensive list rendering

**5. Props and Events**
- Always validate props with proper types
- Use descriptive event names
- Avoid mutating props directly; emit events instead
- Document complex prop structures

**6. Template Best Practices**
- Keep templates simple and readable
- Extract complex logic into computed properties or methods
- Use shorthand directives (`:` for `v-bind`, `@` for `v-on`)
- Avoid inline expressions with complex logic

**7. Testing**
- Write unit tests for components with business logic
- Use Vitest for Vite projects, Jest for Vue CLI
- Test user interactions, not implementation details
- Maintain good test coverage for critical paths

**8. TypeScript Integration**
- Use TypeScript for better type safety and IDE support
- Define proper types for props, emits, and composables
- Leverage Vue's built-in TypeScript support

**9. Development Workflow**
- Use Vue DevTools for debugging
- Enable hot module replacement for faster development
- Configure ESLint and Prettier for consistent code style
- Use Vite for faster build times and better DX

**10. Project Structure**
- Organize files by feature or domain
- Keep views, components, and composables separate
- Use absolute imports with path aliases
- Follow consistent naming conventions throughout the project
