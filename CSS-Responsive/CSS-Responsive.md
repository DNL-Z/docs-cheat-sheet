# 📱 CSS - Responsive

## 📋 Table of Contents

- [📏 Standard Breakpoints](#standard-breakpoints)
- [🎯 Media Queries](#media-queries)
- [🛠️ Responsive Techniques](#responsive-techniques)
- [🖼️ Responsive Images](#responsive-images)
- [✍️ Fluid Typography](#fluid-typography)
- [📦 Container Queries](#container-queries)
- [✅ Best Practices](#best-practices)

---

## 📏 Standard Breakpoints

### 📱 Mobile-First Approach (Recommended)

```css
/* Mobile default (< 480px) */

/* Small tablet */
@media (min-width: 480px) { }

/* Tablet */
@media (min-width: 768px) { }

/* Desktop */
@media (min-width: 1024px) { }

/* Large Desktop */
@media (min-width: 1280px) { }

/* Extra Large Desktop */
@media (min-width: 1440px) { }
```

### 🖥️ Desktop-First Approach

```css
/* Desktop default */

/* Tablet */
@media (max-width: 1023px) { }

/* Mobile landscape */
@media (max-width: 767px) { }

/* Mobile portrait */
@media (max-width: 479px) { }
```

### 🎨 Custom Breakpoints

**Specific breakpoints reference:**
- `375px` - iPhone SE, small phones
- `414px` - iPhone Plus
- `768px` - iPad portrait
- `959px` - Custom tablet
- `1024px` - iPad landscape, small desktop
- `1279px` - Medium desktop
- `1280px` - Standard desktop
- `1330px` - Custom desktop
- `1400px` - Large desktop
- `1680px` - Extra large desktop
- `1990px` - Ultra wide screen

### 🎭 Popular Frameworks

**Bootstrap 5**
```css
/* Extra small (< 576px) */
@media (min-width: 576px) { }  /* Small */
@media (min-width: 768px) { }  /* Medium */
@media (min-width: 992px) { }  /* Large */
@media (min-width: 1200px) { } /* X-Large */
@media (min-width: 1400px) { } /* XX-Large */
```

**Tailwind CSS**
```css
@media (min-width: 640px) { }  /* sm */
@media (min-width: 768px) { }  /* md */
@media (min-width: 1024px) { } /* lg */
@media (min-width: 1280px) { } /* xl */
@media (min-width: 1536px) { } /* 2xl */
```

---

## 🎯 Media Queries

### 📐 Basic Syntax

```css
/* Minimum width */
@media (min-width: 768px) {
  .container {
    max-width: 720px;
  }
}

/* Maximum width */
@media (max-width: 767px) {
  .container {
    padding: 1rem;
  }
}

/* Width range */
@media (min-width: 768px) and (max-width: 1023px) {
  .container {
    max-width: 960px;
  }
}
```

### 🔄 Orientation

```css
/* Portrait */
@media (orientation: portrait) {
  .sidebar {
    display: none;
  }
}

/* Landscape */
@media (orientation: landscape) {
  .content {
    flex-direction: row;
  }
}
```

### 🖥️ Screen Resolution

```css
/* Retina displays */
@media (-webkit-min-device-pixel-ratio: 2),
       (min-resolution: 192dpi) {
  .logo {
    background-image: url("path/to/logo.png");
  }
}
```

### 👤 User Preferences

```css
/* Dark mode */
@media (prefers-color-scheme: dark) {
  body {
    background: #1a1a1a;
    color: #fff;
  }
}

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
}
```

### 🔗 Combined Media Queries

```css
/* Multiple conditions */
@media (min-width: 768px) and (max-width: 1023px) and (orientation: portrait) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* OR condition */
@media (max-width: 767px), (orientation: portrait) {
  .menu {
    display: block;
  }
}
```

---

## 🛠️ Responsive Techniques

### 📦 Flexbox

```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.item {
  flex: 1 1 300px; /* grow shrink basis */
}

/* Responsive with flexbox */
@media (max-width: 767px) {
  .container {
    flex-direction: column;
  }
}
```

### 🎛️ CSS Grid

```css
/* Responsive grid with auto-fit */
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

/* Grid with media queries */
.grid {
  display: grid;
  grid-template-columns: 1fr; /* Mobile */
  gap: 1rem;
}

@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### 📏 Relative Units

```css
/* Use rem/em instead of px */
.container {
  padding: 1rem;        /* 16px default */
  font-size: 1.125rem;  /* 18px */
  max-width: 75rem;     /* 1200px */
}

/* Viewport units */
.hero {
  height: 100vh;        /* 100% of viewport height */
  width: 100vw;         /* 100% of viewport width */
  font-size: 5vw;       /* 5% of viewport width */
}

/* Modern units */
.element {
  width: clamp(300px, 50%, 600px);  /* min, preferred, max */
  font-size: clamp(1rem, 2.5vw, 2rem);
}
```

### 📐 Aspect Ratio

```css
/* Maintain aspect ratio */
.video-container {
  aspect-ratio: 16 / 9;
  width: 100%;
}

.square {
  aspect-ratio: 1 / 1;
}

/* Fallback for older browsers */
.video-container {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 ratio */
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

---

## 🖼️ Responsive Images

### 🎨 Picture Element

```html
<picture>
  <source media="(min-width: 1024px)" srcset="path/to/large.jpg">
  <source media="(min-width: 768px)" srcset="path/to/medium.jpg">
  <img src="path/to/small.jpg" alt="Description">
</picture>
```

### 📸 Srcset & Sizes

```html
<img
  srcset="path/to/small.jpg 480w,
          path/to/medium.jpg 768w,
          path/to/large.jpg 1200w"
  sizes="(max-width: 768px) 100vw,
         (max-width: 1200px) 50vw,
         33vw"
  src="path/to/fallback.jpg"
  alt="Description">
```

### 🎯 CSS for Images

```css
/* Basic responsive image */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Object-fit to control ratio */
.image-cover {
  width: 100%;
  height: 300px;
  object-fit: cover;
  object-position: center;
}

/* Responsive background */
.hero {
  background-image: url("path/to/mobile.jpg");
  background-size: cover;
  background-position: center;
}

@media (min-width: 768px) {
  .hero {
    background-image: url("path/to/desktop.jpg");
  }
}
```

---

## ✍️ Fluid Typography

### 📏 Clamp for Fluid Size

```css
/* Typography that adapts to viewport */
h1 {
  font-size: clamp(2rem, 5vw + 1rem, 4rem);
  /* min: 2rem (32px), preferred: 5vw + 1rem, max: 4rem (64px) */
}

h2 {
  font-size: clamp(1.5rem, 3vw + 1rem, 3rem);
}

p {
  font-size: clamp(1rem, 1.5vw + 0.5rem, 1.25rem);
}
```

### 🎚️ Responsive Typography Scale

```css
/* Typography base - Define custom properties first */
:root {
  --font-size-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --font-size-lg: clamp(1.25rem, 1.1rem + 0.75vw, 1.5rem);
  --font-size-xl: clamp(1.5rem, 1.3rem + 1vw, 2rem);
  --font-size-2xl: clamp(2rem, 1.7rem + 1.5vw, 3rem);
}

/* Then use them in your elements */
body {
  font-size: var(--font-size-base);
  line-height: 1.6;
}

h1 { font-size: var(--font-size-2xl); }
h2 { font-size: var(--font-size-xl); }
h3 { font-size: var(--font-size-lg); }
```

### 📝 Responsive Line-Height and Letter-Spacing

```css
.text {
  line-height: 1.8;
  letter-spacing: 0.02em;
}

@media (max-width: 767px) {
  .text {
    line-height: 1.6;
    letter-spacing: 0.01em;
  }
}
```

---

## 📦 Container Queries

### 🎯 Basic Syntax (Modern CSS)

```css
/* Define a container */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Container-based query */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 1fr 2fr;
  }
}

/* Container query without name */
.sidebar {
  container-type: inline-size;
}

.widget {
  padding: 1rem;
}

@container (min-width: 300px) {
  .widget {
    padding: 2rem;
    display: flex;
  }
}
```

### 📐 Container Query Units

```css
.container {
  container-type: inline-size;
}

.element {
  font-size: 5cqw;  /* 5% of container width */
  padding: 2cqh;    /* 2% of container height */
  width: 50cqi;     /* 50% of inline dimension */
  height: 30cqb;    /* 30% of block dimension */
}
```

---

## ✅ Best Practices

### 📱 Mobile-First

```css
/* ✅ Good: Mobile default, desktop override */
.element {
  font-size: 1rem;
  padding: 1rem;
}

@media (min-width: 768px) {
  .element {
    font-size: 1.25rem;
    padding: 2rem;
  }
}

/* ❌ Avoid: Desktop default */
.element {
  font-size: 1.25rem;
  padding: 2rem;
}

@media (max-width: 767px) {
  .element {
    font-size: 1rem;
    padding: 1rem;
  }
}
```

### 📐 Viewport Meta Tag

```html
<!-- Required for responsive design -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Advanced options -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
```

### 🎨 Responsive CSS Variables

```css
/* Define custom properties in :root */
:root {
  --spacing: 1rem;
  --container-width: 100%;
  --columns: 1;
}

/* Override values at different breakpoints */
@media (min-width: 768px) {
  :root {
    --spacing: 1.5rem;
    --container-width: 720px;
    --columns: 2;
  }
}

@media (min-width: 1024px) {
  :root {
    --spacing: 2rem;
    --container-width: 960px;
    --columns: 3;
  }
}

/* Use custom properties in your elements */
.container {
  max-width: var(--container-width);
  padding: var(--spacing);
}

.grid {
  grid-template-columns: repeat(var(--columns), 1fr);
}
```

### ⚡ Performance

```css
/* Use transform instead of position for animations */
@media (prefers-reduced-motion: no-preference) {
  .element {
    transition: transform 0.3s ease;
  }

  .element:hover {
    transform: scale(1.05);
  }
}

/* Lazy loading for images */
img {
  loading: lazy;
}

/* Content-visibility to optimize rendering */
.section {
  content-visibility: auto;
  contain-intrinsic-size: 0 500px;
}
```

### 👆 Touch-Friendly

```css
/* Minimum click area 44x44px (WCAG recommendation) */
.button {
  min-width: 44px;
  min-height: 44px;
  padding: 0.75rem 1.5rem;
}

/* Hover only on devices with hover */
@media (hover: hover) and (pointer: fine) {
  .button:hover {
    background-color: #0056b3;
  }
}

/* Remove tap highlight on mobile */
button {
  -webkit-tap-highlight-color: transparent;
}
```

### 🧪 Testing Responsive

```css
/* Display active breakpoint (dev only) */
body::after {
  content: "Mobile";
  position: fixed;
  bottom: 10px;
  right: 10px;
  background: red;
  color: white;
  padding: 5px 10px;
  font-size: 12px;
  z-index: 9999;
}

@media (min-width: 480px) {
  body::after { content: "Tablet Small"; background: orange; }
}

@media (min-width: 768px) {
  body::after { content: "Tablet"; background: yellow; color: black; }
}

@media (min-width: 1024px) {
  body::after { content: "Desktop"; background: green; }
}

@media (min-width: 1280px) {
  body::after { content: "Desktop Large"; background: blue; }
}
```

---

## 🔗 Useful Resources

### 🛠️ Testing Tools
- Chrome DevTools (Device Mode)
- Firefox Responsive Design Mode
- BrowserStack
- Responsively App

### 📚 References
- [MDN: Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
- [Can I Use](https://caniuse.com/) - Browser support
- [CSS Tricks: Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS Tricks: Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
