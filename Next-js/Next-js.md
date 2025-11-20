# ▲ Next.js

A comprehensive React framework for building production-ready web applications with server-side rendering, static site generation, and powerful developer tooling.

## 📑 Table of Contents

- [🚀 Getting Started](#-getting-started)
  - [Create a New Project](#create-a-new-project)
  - [Project Structure](#project-structure)
  - [Running the Development Server](#running-the-development-server)
- [📁 File-Based Routing](#-file-based-routing)
  - [Pages Directory](#pages-directory)
  - [App Directory (App Router)](#app-directory-app-router)
  - [Dynamic Routes](#dynamic-routes)
  - [Route Groups](#route-groups)
- [🎨 Rendering Methods](#-rendering-methods)
  - [Static Site Generation (SSG)](#static-site-generation-ssg)
  - [Server-Side Rendering (SSR)](#server-side-rendering-ssr)
  - [Incremental Static Regeneration (ISR)](#incremental-static-regeneration-isr)
  - [Client-Side Rendering (CSR)](#client-side-rendering-csr)
- [🔧 Data Fetching](#-data-fetching)
  - [getStaticProps](#getstaticprops)
  - [getServerSideProps](#getserversideprops)
  - [getStaticPaths](#getstaticpaths)
  - [App Router Data Fetching](#app-router-data-fetching)
- [🖼️ Image Optimization](#-image-optimization)
  - [Next Image Component](#next-image-component)
- [🛣️ Navigation](#-navigation)
  - [Link Component](#link-component)
  - [useRouter Hook](#userouter-hook)
  - [Navigation in App Router](#navigation-in-app-router)
- [📦 API Routes](#-api-routes)
  - [Creating API Endpoints](#creating-api-endpoints)
  - [Dynamic API Routes](#dynamic-api-routes)
  - [Route Handlers (App Router)](#route-handlers-app-router)
- [⚙️ Configuration](#-configuration)
  - [next.config.js](#nextconfigjs)
  - [Environment Variables](#environment-variables)
- [🎯 Best Practices](#-best-practices)
- [📚 Resources](#-resources)

---

## 🚀 Getting Started

### Create a New Project

Using the latest version of Next.js:

```bash
  npx create-next-app@latest
```

**Interactive prompts:**
- Project name
- TypeScript support
- ESLint configuration
- Tailwind CSS
- `src/` directory
- App Router (recommended)
- Import alias customization

**Create with specific options:**

```bash
  # TypeScript with App Router and Tailwind CSS
  npx create-next-app@latest my-app --typescript --tailwind --app

  # JavaScript with Pages Router
  npx create-next-app@latest my-app --js --no-app
```

### Project Structure

**App Router structure (recommended):**

```
my-app/
├── app/
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Home page
│   ├── about/
│   │   └── page.tsx        # /about route
│   └── api/
│       └── route.ts        # API endpoint
├── public/                 # Static assets
├── next.config.js          # Next.js configuration
└── package.json
```

**Pages Router structure (legacy):**

```
my-app/
├── pages/
│   ├── _app.tsx            # Custom App component
│   ├── _document.tsx       # Custom Document
│   ├── index.tsx           # Home page
│   ├── about.tsx           # /about route
│   └── api/
│       └── hello.ts        # API endpoint
├── public/
├── styles/
├── next.config.js
└── package.json
```

### Running the Development Server

```bash
  # Development mode
  npm run dev

  # Production build
  npm run build

  # Start production server
  npm run start

  # Linting
  npm run lint
```

**Development server:** http://localhost:3000

---

## 📁 File-Based Routing

Next.js uses a file-based routing system where the file structure determines the routes.

### Pages Directory

In the Pages Router, files in the `pages/` directory automatically become routes:

```
pages/
├── index.tsx               # / (home page)
├── about.tsx               # /about
├── blog/
│   ├── index.tsx           # /blog
│   └── [slug].tsx          # /blog/:slug (dynamic)
└── products/
    └── [id].tsx            # /products/:id
```

### App Directory (App Router)

The App Router uses the `app/` directory with special file conventions:

**Special files:**
- **`page.tsx`** - Defines a route's UI
- **`layout.tsx`** - Shared UI for segments
- **`loading.tsx`** - Loading UI
- **`error.tsx`** - Error UI
- **`not-found.tsx`** - 404 UI
- **`template.tsx`** - Re-rendered layout

**Example:**

```typescript
// app/page.tsx
export default function HomePage() {
  return <h1>Welcome to Next.js</h1>;
}

// app/about/page.tsx
export default function AboutPage() {
  return <h1>About Us</h1>;
}

// app/layout.tsx
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
```

### Dynamic Routes

**Pages Router:**

```typescript
// pages/blog/[slug].tsx
import { useRouter } from 'next/router';

export default function BlogPost() {
  const router = useRouter();
  const { slug } = router.query;

  return <h1>Post: {slug}</h1>;
}
```

**App Router:**

```typescript
// app/blog/[slug]/page.tsx
export default function BlogPost({ params }: { params: { slug: string } }) {
  return <h1>Post: {params.slug}</h1>;
}
```

**Catch-all routes:**

```typescript
// app/blog/[...slug]/page.tsx - Matches /blog/a, /blog/a/b, /blog/a/b/c
// app/blog/[[...slug]]/page.tsx - Also matches /blog
export default function BlogPost({ params }: { params: { slug: string[] } }) {
  return <h1>Post: {params.slug.join('/')}</h1>;
}
```

### Route Groups

Organize routes without affecting the URL structure using parentheses:

```
app/
├── (marketing)/
│   ├── about/
│   │   └── page.tsx        # /about
│   └── contact/
│       └── page.tsx        # /contact
└── (shop)/
    └── products/
        └── page.tsx        # /products
```

---

## 🎨 Rendering Methods

Next.js supports multiple rendering strategies.

### Static Site Generation (SSG)

Pre-renders pages at build time. Best for content that doesn't change frequently.

```typescript
// Pages Router
export async function getStaticProps() {
  const data = await fetchData();

  return {
    props: { data },
  };
}

export default function Page({ data }) {
  return <div>{data.title}</div>;
}
```

### Server-Side Rendering (SSR)

Pre-renders pages on each request. Best for frequently changing data.

```typescript
// Pages Router
export async function getServerSideProps() {
  const data = await fetchData();

  return {
    props: { data },
  };
}

export default function Page({ data }) {
  return <div>{data.title}</div>;
}
```

**App Router (default is Server Components):**

```typescript
// app/page.tsx
async function getData() {
  const res = await fetch('https://api.example.com/data');
  return res.json();
}

export default async function Page() {
  const data = await getData();
  return <div>{data.title}</div>;
}
```

### Incremental Static Regeneration (ISR)

Updates static pages after deployment without rebuilding the entire site.

```typescript
// Pages Router
export async function getStaticProps() {
  const data = await fetchData();

  return {
    props: { data },
    revalidate: 60, // Revalidate every 60 seconds
  };
}
```

**App Router:**

```typescript
// app/page.tsx
export const revalidate = 60; // Revalidate every 60 seconds

async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 60 }
  });
  return res.json();
}

export default async function Page() {
  const data = await getData();
  return <div>{data.title}</div>;
}
```

### Client-Side Rendering (CSR)

Renders content in the browser using React hooks.

```typescript
'use client'; // Mark as Client Component in App Router

import { useState, useEffect } from 'react';

export default function Page() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/data')
      .then(res => res.json())
      .then(setData);
  }, []);

  if (!data) return <div>Loading...</div>;
  return <div>{data.title}</div>;
}
```

---

## 🔧 Data Fetching

### getStaticProps

Fetches data at build time for SSG:

```typescript
export async function getStaticProps(context) {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();

  return {
    props: { data },
    revalidate: 10, // Optional: ISR
  };
}
```

### getServerSideProps

Fetches data on every request for SSR:

```typescript
export async function getServerSideProps(context) {
  const { params, query, req, res } = context;

  const data = await fetch(`https://api.example.com/data/${params.id}`);

  return {
    props: { data },
  };
}
```

### getStaticPaths

Defines dynamic routes to pre-render with SSG:

```typescript
export async function getStaticPaths() {
  const posts = await getAllPosts();

  const paths = posts.map(post => ({
    params: { slug: post.slug },
  }));

  return {
    paths,
    fallback: false, // or 'blocking' or true
  };
}

export async function getStaticProps({ params }) {
  const post = await getPostBySlug(params.slug);

  return {
    props: { post },
  };
}
```

**Fallback options:**
- **`false`** - Returns 404 for non-generated paths
- **`true`** - Serves a fallback page then generates and caches the page
- **`'blocking'`** - Waits for the page to be generated (no fallback shown)

### App Router Data Fetching

Server Components can fetch data directly:

```typescript
// app/posts/[id]/page.tsx
async function getPost(id: string) {
  const res = await fetch(`https://api.example.com/posts/${id}`, {
    next: { revalidate: 3600 } // Optional: revalidate after 1 hour
  });

  if (!res.ok) throw new Error('Failed to fetch');
  return res.json();
}

export default async function PostPage({ params }: { params: { id: string } }) {
  const post = await getPost(params.id);

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  );
}

// Generate static params
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts').then(res => res.json());

  return posts.map((post) => ({
    id: post.id,
  }));
}
```

---

## 🖼️ Image Optimization

### Next Image Component

Automatically optimizes images for performance:

```typescript
import Image from 'next/image';

export default function Page() {
  return (
    <div>
      {/* Static import */}
      <Image
        src="/hero.png"
        alt="Hero"
        width={500}
        height={300}
        priority // Load immediately
      />

      {/* External image */}
      <Image
        src="https://example.com/image.jpg"
        alt="External"
        width={500}
        height={300}
        loading="lazy" // Default
      />

      {/* Fill container */}
      <div style={{ position: 'relative', width: '100%', height: '400px' }}>
        <Image
          src="/banner.jpg"
          alt="Banner"
          fill
          style={{ objectFit: 'cover' }}
        />
      </div>
    </div>
  );
}
```

**Key features:**
- Automatic lazy loading
- Prevents layout shift
- Serves modern formats (WebP, AVIF)
- Responsive images
- On-demand optimization

**Configure external images in `next.config.js`:**

```javascript
module.exports = {
  images: {
    domains: ['example.com', 'cdn.example.com'],
  },
};
```

---

## 🛣️ Navigation

### Link Component

Client-side navigation between pages:

```typescript
import Link from 'next/link';

export default function Nav() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
      <Link href="/blog/hello-world">Blog Post</Link>

      {/* Dynamic route */}
      <Link href={`/products/${productId}`}>Product</Link>

      {/* With object */}
      <Link
        href={{
          pathname: '/blog/[slug]',
          query: { slug: 'hello' },
        }}
      >
        Blog Post
      </Link>
    </nav>
  );
}
```

### useRouter Hook

Programmatic navigation in Pages Router:

```typescript
import { useRouter } from 'next/router';

export default function Page() {
  const router = useRouter();

  const handleClick = () => {
    router.push('/about');
    // router.replace('/about'); // Without adding to history
    // router.back(); // Go back
    // router.reload(); // Reload page
  };

  return <button onClick={handleClick}>Go to About</button>;
}
```

**Access query parameters:**

```typescript
const router = useRouter();
const { slug, id } = router.query;
```

### Navigation in App Router

```typescript
'use client';

import { useRouter, usePathname, useSearchParams } from 'next/navigation';

export default function Page() {
  const router = useRouter();
  const pathname = usePathname(); // Current path
  const searchParams = useSearchParams(); // Query params

  const handleClick = () => {
    router.push('/about');
    // router.replace('/about');
    // router.back();
    // router.forward();
    // router.refresh(); // Refresh Server Components
  };

  return <button onClick={handleClick}>Navigate</button>;
}
```

---

## 📦 API Routes

### Creating API Endpoints

**Pages Router:**

```typescript
// pages/api/hello.ts
import type { NextApiRequest, NextApiResponse } from 'next';

type Data = {
  message: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  // Check method
  if (req.method !== 'GET') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  res.status(200).json({ message: 'Hello World' });
}
```

**Handle different HTTP methods:**

```typescript
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  switch (req.method) {
    case 'GET':
      return res.status(200).json({ message: 'GET request' });
    case 'POST':
      const { name } = req.body;
      return res.status(201).json({ message: `Created ${name}` });
    case 'PUT':
      return res.status(200).json({ message: 'Updated' });
    case 'DELETE':
      return res.status(204).end();
    default:
      return res.status(405).json({ message: 'Method not allowed' });
  }
}
```

### Dynamic API Routes

```typescript
// pages/api/users/[id].ts
export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { id } = req.query;

  res.status(200).json({ userId: id });
}
```

### Route Handlers (App Router)

```typescript
// app/api/hello/route.ts
import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  return NextResponse.json({ message: 'Hello World' });
}

export async function POST(request: Request) {
  const body = await request.json();
  return NextResponse.json({ received: body }, { status: 201 });
}
```

**Dynamic route handlers:**

```typescript
// app/api/users/[id]/route.ts
export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  const { id } = params;

  const user = await getUserById(id);

  if (!user) {
    return NextResponse.json({ error: 'User not found' }, { status: 404 });
  }

  return NextResponse.json(user);
}
```

**Access query parameters:**

```typescript
export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('query');

  return NextResponse.json({ query });
}
```

---

## ⚙️ Configuration

### next.config.js

Configure Next.js behavior:

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  // React strict mode
  reactStrictMode: true,

  // Image domains
  images: {
    domains: ['example.com', 'cdn.example.com'],
    formats: ['image/avif', 'image/webp'],
  },

  // Redirects
  async redirects() {
    return [
      {
        source: '/old-path',
        destination: '/new-path',
        permanent: true,
      },
    ];
  },

  // Rewrites (URL stays the same)
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'https://api.example.com/:path*',
      },
    ];
  },

  // Headers
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-Custom-Header',
            value: 'my-value',
          },
        ],
      },
    ];
  },

  // Environment variables
  env: {
    CUSTOM_KEY: process.env.CUSTOM_KEY,
  },

  // Webpack config
  webpack: (config, { isServer }) => {
    // Custom webpack configuration
    return config;
  },
};

module.exports = nextConfig;
```

### Environment Variables

Create environment variable files:

```dotenv
# .env.local (loaded on all environments, ignored by git)
DATABASE_URL=postgresql://localhost:5432/mydb
API_KEY=secret123

# .env.development (loaded on npm run dev)
API_URL=http://localhost:3000/api

# .env.production (loaded on npm run build && npm start)
API_URL=https://api.production.com
```

**Access in code:**

```typescript
// Server-side (Pages API or Server Components)
const apiKey = process.env.API_KEY;

// Client-side (must prefix with NEXT_PUBLIC_)
const publicKey = process.env.NEXT_PUBLIC_API_KEY;
```

**Example `.env.local`:**

```dotenv
# Private (server-side only)
DATABASE_URL=postgresql://user:pass@localhost:5432/db
SECRET_KEY=my-secret-key

# Public (exposed to browser)
NEXT_PUBLIC_API_URL=https://api.example.com
NEXT_PUBLIC_ANALYTICS_ID=UA-123456789-1
```

---

## 🎯 Best Practices

### Performance Optimization

1. **Use `next/image` for all images** - Automatic optimization and lazy loading
2. **Implement ISR for dynamic content** - Balance between SSG and SSR
3. **Code splitting** - Automatically handled by Next.js
4. **Dynamic imports** - Load components only when needed

```typescript
import dynamic from 'next/dynamic';

const DynamicComponent = dynamic(() => import('../components/HeavyComponent'), {
  loading: () => <p>Loading...</p>,
  ssr: false, // Disable server-side rendering
});
```

### SEO Optimization

Use the `Metadata` API in App Router:

```typescript
// app/page.tsx
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'My Page Title',
  description: 'My page description',
  openGraph: {
    title: 'My Page Title',
    description: 'My page description',
    images: ['/og-image.jpg'],
  },
};

export default function Page() {
  return <h1>My Page</h1>;
}
```

**Dynamic metadata:**

```typescript
// app/blog/[slug]/page.tsx
export async function generateMetadata({ params }): Promise<Metadata> {
  const post = await getPost(params.slug);

  return {
    title: post.title,
    description: post.excerpt,
  };
}
```

**Pages Router (legacy):**

```typescript
import Head from 'next/head';

export default function Page() {
  return (
    <>
      <Head>
        <title>My Page Title</title>
        <meta name="description" content="My page description" />
        <meta property="og:title" content="My Page Title" />
      </Head>
      <h1>My Page</h1>
    </>
  );
}
```

### TypeScript Support

Next.js has built-in TypeScript support:

```typescript
// tsconfig.json is created automatically
// Install types
npm install --save-dev @types/react @types/node
```

### Project Organization

```
src/
├── app/                    # App Router pages
├── components/             # React components
│   ├── ui/                # UI components
│   └── features/          # Feature-specific components
├── lib/                   # Utility functions
│   ├── api.ts            # API helpers
│   └── utils.ts          # General utilities
├── types/                # TypeScript types
└── styles/               # Global styles
```

### Error Handling

**App Router:**

```typescript
// app/error.tsx
'use client';

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button onClick={reset}>Try again</button>
    </div>
  );
}

// app/not-found.tsx
export default function NotFound() {
  return (
    <div>
      <h2>404 - Page Not Found</h2>
      <p>Could not find requested resource</p>
    </div>
  );
}
```

---

## 📚 Resources

**Official Documentation:** https://nextjs.org/docs

**Learn Next.js:** https://nextjs.org/learn

**Next.js Examples:** https://github.com/vercel/next.js/tree/canary/examples

**Deployment:** https://vercel.com

**Community:** https://github.com/vercel/next.js/discussions

---
