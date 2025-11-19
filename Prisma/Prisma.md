# 🔷 Prisma ORM

A modern database toolkit for TypeScript and Node.js that simplifies database access with type-safe queries and intuitive data modeling.

## 📑 Table of Contents

- [🛠️ CLI Commands](#-cli-commands)
  - [Core Commands](#core-commands)
  - [Database Commands](#database-commands)
  - [Development Tools](#development-tools)
- [💻 Prisma Client](#-prisma-client)
  - [Client API Methods](#client-api-methods)
  - [CRUD Operations](#crud-operations)
  - [Query Examples](#query-examples)

---

## 🛠️ CLI Commands

### Core Commands

**`npx prisma generate`** — Generates the Prisma Client based on your schema

```bash
  npx prisma generate
```

Regenerates the Prisma Client whenever you make changes to your schema. This ensures your client is always in sync with your data model.

**`npx prisma validate`** — Validates the Prisma schema for errors

```bash
  npx prisma validate
```

Checks your schema for syntax errors and validates relationships between models.

**`npx prisma migrate`** — Manages database migrations

```bash
  npx prisma migrate dev        # Create and apply migrations in development
  npx prisma migrate deploy     # Apply pending migrations in production
  npx prisma migrate reset      # Reset the database and apply all migrations
```

Creates SQL migration files and applies them to your database.

### Database Commands

**`npx prisma db pull`** — Pulls the schema from an existing database

```bash
  npx prisma db pull
```

Introspects your database and generates a Prisma schema based on the existing structure. Useful for adding Prisma to an existing project.

**`npx prisma db push`** — Synchronizes the Prisma schema with the database

```bash
  npx prisma db push
```

Pushes schema changes directly to the database without creating migration files. Best for prototyping and development.

### Development Tools

**`npx prisma studio`** — Opens Prisma Studio GUI

```bash
  npx prisma studio
```

Launches a visual database browser in your browser, allowing you to view and edit data in your database.

---

## 💻 Prisma Client

### Client API Methods

The Prisma Client provides auto-generated, type-safe database queries based on your schema.

### CRUD Operations

For each model in your schema, Prisma Client generates the following methods:

**`create()`** — Creates a new record

```typescript
await prisma.role.create({
  data: {
    name: "Admin",
    description: "Administrator role"
  }
})
```

**`findMany()`** — Retrieves multiple records

```typescript
await prisma.role.findMany({
  where: {
    active: true
  },
  orderBy: {
    name: 'asc'
  }
})
```

**`findUnique()`** — Finds a single unique record

```typescript
await prisma.role.findUnique({
  where: {
    id: 1
  }
})
```

**`update()`** — Updates an existing record

```typescript
await prisma.role.update({
  where: {
    id: 1
  },
  data: {
    name: "Super Admin"
  }
})
```

**`delete()`** — Deletes a record

```typescript
await prisma.role.delete({
  where: {
    id: 1
  }
})
```

**`upsert()`** — Updates or creates a record

```typescript
await prisma.role.upsert({
  where: {
    id: 1
  },
  update: {
    name: "Admin"
  },
  create: {
    name: "Admin",
    description: "Administrator role"
  }
})
```

### Query Examples

**Filtering and Relations:**

```typescript
// Find users with their posts
await prisma.user.findMany({
  include: {
    posts: true
  }
})

// Complex filtering
await prisma.post.findMany({
  where: {
    AND: [
      { published: true },
      { author: { email: { contains: "prisma.io" } } }
    ]
  }
})
```

**Aggregations:**

```typescript
// Count records
const count = await prisma.user.count()

// Aggregate operations
const result = await prisma.post.aggregate({
  _avg: {
    views: true
  },
  _count: {
    id: true
  }
})
```
