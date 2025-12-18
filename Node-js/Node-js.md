# ⚙️ Node.js

**Node.js** is a JavaScript runtime built on Chrome's V8 JavaScript engine.

## 📑 Table of Contents

- [🔧 NVM (Node Version Manager)](#-nvm-node-version-manager)
- [📦 NPM & Package Management](#-npm--package-management)
- [🔌 Popular Packages](#-popular-packages)
- [🌍 Environment Variables](#-environment-variables)
- [🚀 Running Node Applications](#-running-node-applications)
- [🌐 REST API Fundamentals](#-rest-api-fundamentals)
- [🔀 HTTP Methods](#-http-methods)
- [📊 HTTP Status Codes](#-http-status-codes)
- [📥 Request Structure](#-request-structure)
- [📤 Response Structure](#-response-structure)
- [🚀 Express API Examples](#-express-api-examples)
- [✅ API Best Practices](#-api-best-practices)

---

## 🔧 NVM (Node Version Manager)

### Check current Node version

```bash
  node --version
```

### List available versions

```bash
  nvm ls
```

### Install a new version

```bash
  nvm install v<version>
```

### Switch Node version

```bash
  nvm use v<version>
```

### Set default version

```bash
  nvm alias default <version>
```

### Uninstall a version

```bash
  nvm uninstall <version>
```

---

## 📦 NPM & Package Management

### Initialize a new project

```bash
  npm init
```

Note: Entry point is typically `index.js` or `server.js`

### Install dependencies

```bash
  npm install <package-name>
```

### Install as dev dependency

```bash
  npm install --save-dev <package-name>
```

### Install globally

```bash
  npm install -g <package-name>
```

### Update dependencies

```bash
  npm update
```

### Security audit

```bash
  npm audit
  npm audit fix
```

### Run scripts

```bash
  npm run <script-name>
  npm start
  npm test
```

---

## 🔌 Popular Packages

### Express

Web framework for Node.js

```bash
  npm install express
```

### Mongoose

MongoDB - Object Modeling Tool

```bash
  npm install mongoose
```

### Nodemon

Auto-restart development server on file changes

```bash
  npm install -g nodemon
```

Global installation:
→ Available for all projects

```bash
  npm install --save-dev nodemon
```

Dev dependency:
→ Project-specific, version-controlled

### Body Parser

(Deprecated since Express 4.16+ - use `express.json()` instead)

```bash
  npm install body-parser
```

---

## 🌍 Environment Variables

### Create .env file

```bash
  touch .env
```

### Load environment variables

Using `dotenv` package:

```bash
  npm install dotenv
```

In your code:
```javascript
require('dotenv').config();
const port = process.env.PORT || 3000;
```

---

## 🚀 Running Node Applications

### Run with Node

```bash
  node server.js
```

### Run with Nodemon (development)

```bash
  nodemon server.js
```

---

## 🌐 REST API Fundamentals

### What is a REST API?

**REST** (Representational State Transfer) is an architectural style for designing networked applications. A REST API uses HTTP requests to access and manipulate resources.

**Key principles:**
- Stateless communication
- Client-Server architecture
- Uniform interface
- Resource-based (URL structure)

### API Structure

```
https://api.example.com/v1/users/123/posts
│                        │  │     │   │
│                        │  │     │   └─ Resource
│                        │  │     └───── ID (parameter)
│                        │  └─────────── Resource
│                        └────────────── Version
```

---

## 🔀 HTTP Methods

### GET - Retrieve data

```javascript
app.get('/api/users', (req, res) => {
  res.json({ users: [] });
});
```

Used for: Fetching resources <br>
Idempotent: ✅ Yes <br>
Has body: ❌ No

### POST - Create a new resource

```javascript
app.post('/api/users', (req, res) => {
  const newUser = req.body;
  res.status(201).json({ user: newUser });
});
```

Used for: Creating resources<br>
Idempotent: ❌ No <br>
Has body: ✅ Yes

### PUT - Update the entire resource

```javascript
app.put('/api/users/:id', (req, res) => {
  const updatedUser = req.body;
  res.json({ user: updatedUser });
});
```

Used for: Replacing resources <br>
Idempotent: ✅ Yes <br>
Has body: ✅ Yes

### PATCH - Partial update

```javascript
app.patch('/api/users/:id', (req, res) => {
  const updates = req.body;
  res.json({ user: updates });
});
```

Used for: Modifying specific fields <br>
Idempotent: ✅ Yes <br>
Has body: ✅ Yes

### DELETE - Remove resource

```javascript
app.delete('/api/users/:id', (req, res) => {
  res.status(204).send();
});
```

Used for: Deleting resources <br>
Idempotent: ✅ Yes <br>
Has body: ❌ No

---

## 📊 HTTP Status Codes

### 2xx - Success

| Code | Meaning    | Usage                      |
|------|------------|----------------------------|
| 200  | OK         | Successful GET, PUT, PATCH |
| 201  | Created    | Successful POST            |
| 204  | No Content | Successful DELETE          |

### 3xx - Redirection

| Code | Meaning           | Usage                 |
|------|-------------------|-----------------------|
| 301  | Moved Permanently | Resource relocated    |
| 302  | Found             | Temporary redirect    |
| 304  | Not Modified      | Cached response valid |

### 4xx - Client Errors

| Code | Meaning              | Usage                           |
|------|----------------------|---------------------------------|
| 400  | Bad Request          | Invalid syntax/data             |
| 401  | Unauthorized         | Missing/invalid authentication  |
| 403  | Forbidden            | Authenticated but no permission |
| 404  | Not Found            | Resource doesn't exist          |
| 422  | Unprocessable Entity | Validation errors               |
| 429  | Too Many Requests    | Rate limit exceeded             |

### 5xx - Server Errors

| Code | Meaning               | Usage                          |
|------|-----------------------|--------------------------------|
| 500  | Internal Server Error | Generic server error           |
| 502  | Bad Gateway           | Invalid response from upstream |
| 503  | Service Unavailable   | Server temporarily down        |

---

## 📥 Request Structure

### Headers

Common request headers:

```json
{
  "Content-Type": "application/json",
  "Authorization": "Bearer <token>",
  "Accept": "application/json",
  "User-Agent": "MyApp/1.0"
}
```

### Query Parameters

```javascript
// GET /api/users?page=2&limit=10&sort=name

app.get('/api/users', (req, res) => {
  const { page, limit, sort } = req.query;
  res.json({ page, limit, sort });
});
```

### URL Parameters

```javascript
// GET /api/users/123

app.get('/api/users/:id', (req, res) => {
  const { id } = req.params;
  res.json({ userId: id });
});
```

### Request Body

```javascript
// POST /api/users
// Body: { "name": "John", "email": "john@example.com" }

app.post('/api/users', (req, res) => {
  const { name, email } = req.body;
  res.status(201).json({ name, email });
});
```

---

## 📤 Response Structure

### JSON Response Format

Success response:
```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "John Doe"
  }
}
```

Error response:
```json
{
  "success": false,
  "error": {
    "message": "User not found",
    "code": "USER_NOT_FOUND"
  }
}
```

### Response Headers

```javascript
app.get('/api/users', (req, res) => {
  res.set({
    'Content-Type': 'application/json',
    'X-Total-Count': '100',
    'Cache-Control': 'no-cache'
  });
  res.json({ users: [] });
});
```

---

## 🚀 Express API Examples

### Basic Server Setup

```javascript
const express = require('express');
const app = express();

// Middleware
app.use(express.json()); // Parse JSON bodies
app.use(express.urlencoded({ extended: true })); // Parse URL-encoded bodies

// Routes
app.get('/', (req, res) => {
  res.json({ message: 'API is running' });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

### CRUD Operations Example

```javascript
const users = [];

// CREATE
app.post('/api/users', (req, res) => {
  const user = { id: Date.now(), ...req.body };
  users.push(user);
  res.status(201).json(user);
});

// READ ALL
app.get('/api/users', (req, res) => {
  res.json(users);
});

// READ ONE
app.get('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
});

// UPDATE
app.put('/api/users/:id', (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'User not found' });
  users[index] = { id: parseInt(req.params.id), ...req.body };
  res.json(users[index]);
});

// DELETE
app.delete('/api/users/:id', (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'User not found' });
  users.splice(index, 1);
  res.status(204).send();
});
```

### Middleware Examples

```javascript
// Logging middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

// Authentication middleware
const authenticate = (req, res, next) => {
  const token = req.headers.authorization;
  if (!token) return res.status(401).json({ error: 'No token provided' });
  // Verify token logic here
  next();
};

app.get('/api/protected', authenticate, (req, res) => {
  res.json({ message: 'Protected route' });
});
```

### Error Handling

```javascript
// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// Global error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: 'Internal server error',
    message: err.message
  });
});
```

### CORS Configuration

```javascript
const cors = require('cors');

// Allow all origins
app.use(cors());

// Custom CORS configuration
app.use(cors({
  origin: 'http://localhost:3000',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

---

## ✅ API Best Practices

### Naming Conventions

```
✅ Good:
GET    /api/users
GET    /api/users/123
POST   /api/users
PUT    /api/users/123
DELETE /api/users/123

❌ Bad:
GET    /api/getUsers
POST   /api/createUser
GET    /api/user_data
```

**Rules:**
- Use plural nouns (`/users` not `/user`)
- Use lowercase
- Use hyphens for multi-word resources (`/product-categories`)
- No verbs in URLs (use HTTP methods instead)

### API Versioning

```javascript
// Version in URL (recommended)
app.use('/api/v1/users', usersRouterV1);
app.use('/api/v2/users', usersRouterV2);

// Version in header
app.use((req, res, next) => {
  const version = req.headers['api-version'];
  if (version === '2.0') {
    // Use v2 logic
  }
  next();
});
```

### Authentication Methods

**Bearer Token (JWT):**
```javascript
const jwt = require('jsonwebtoken');

// Generate token
const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET, {
  expiresIn: '24h'
});

// Verify token
const verifyToken = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
};
```

**Request format:**
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Rate Limiting

```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per windowMs
  message: 'Too many requests, please try again later'
});

app.use('/api/', limiter);
```

### Input Validation

```javascript
const validateUser = (req, res, next) => {
  const { name, email } = req.body;

  if (!name || !email) {
    return res.status(400).json({
      error: 'Name and email are required'
    });
  }

  if (!/\S+@\S+\.\S+/.test(email)) {
    return res.status(400).json({
      error: 'Invalid email format'
    });
  }

  next();
};

app.post('/api/users', validateUser, (req, res) => {
  // Create user logic
});
```

### Pagination

```javascript
app.get('/api/users', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;
  const skip = (page - 1) * limit;

  const paginatedUsers = users.slice(skip, skip + limit);

  res.json({
    data: paginatedUsers,
    pagination: {
      page,
      limit,
      total: users.length,
      totalPages: Math.ceil(users.length / limit)
    }
  });
});
```

---

## 🧱 SOLID Principles

[SOLID](https://medium.com/@abderrahmane.roumane.ext/tout-comprendre-des-principes-solid-en-10-minutes-votre-guide-rapide-pour-un-code-plus-efficace-bc625c3634f5)

- Single Responsibility Principle (SRP)
  - [SRP](https://medium.com/@goubardleo/les-principes-solid-7111d2131b1c)
- Open/Closed Principle (OCP)
  - [OCP](https://medium.com/@heinrickratajczakpro/07-52-comprendre-le-principe-ouvert-ferm%C3%A9-open-closed-principle-de-solid-guide-pratique-pour-8325f3bac58c)
- Liskov Substitution Principle (LSP)
  - [LSP](https://devcookies.medium.com/day-three-understanding-solid-principles-liskov-substitution-principle-lsp-5587d7bc7cf1)
- Interface Segregation Principle (ISP)
  - [ISP](https://medium.com/@ramdhas/4-interface-segregation-principle-isp-solid-principle-39e477bae2e3)
- Dependency Inversion Principle (DIP)
  - [DIP](https://dev.to/paulocappa/solid-d-dependency-inversion-principle-dip-34hd)

---
