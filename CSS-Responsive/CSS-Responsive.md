# 📱 CSS - Responsive

## 📏 Standard Breakpoints

### 📱 Mobile-First Approach (Recommended)

```css
/* Mobile default (< 480px) */
body {
  font-size: 14px;
}

/* Small tablet */
@media (min-width: 480px) {
  body {
    font-size: 15px;
  }
}

/* Tablet */
@media (min-width: 768px) {
  body {
    font-size: 16px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  body {
    font-size: 16px;
  }
}

/* Large Desktop */
@media (min-width: 1280px) {
  body {
    font-size: 18px;
  }
}

/* Extra Large Desktop */
@media (min-width: 1440px) {
  body {
    font-size: 18px;
  }
}
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
