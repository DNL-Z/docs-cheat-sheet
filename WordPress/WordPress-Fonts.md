# 🔤 WordPress Fonts

A comprehensive guide for adding and managing custom fonts in WordPress themes, including web font integration and @font-face implementation.

## 📑 Table of Contents

- [🌐 Font Sources](#-font-sources)
- [📥 Generating Font Files](#-generating-font-files)
- [⚙️ Font Installation](#-font-installation)
  - [Step-by-Step Guide](#step-by-step-guide)
  - [File Structure](#file-structure)
- [💻 Implementation](#-implementation)
  - [@font-face Declaration](#font-face-declaration)
  - [CSS Integration](#css-integration)
- [💡 Best Practices](#-best-practices)

---

## 🌐 Font Sources

### Google Fonts
Access thousands of free, open-source fonts:
- Visit [Google Fonts](https://fonts.google.com/)
- Select and download font families
- Ready-to-use with @font-face or link tags

### Font Squirrel
Generate custom font packages with optimal formats:
- Visit [Font Squirrel](https://www.fontsquirrel.com/)
- Use the **Webfont Generator** for custom fonts
- Supports multiple font formats (WOFF, WOFF2, TTF, EOT, SVG)

---

## 📥 Generating Font Files

### Using Font Squirrel Generator

**1. Access the Generator:**
- Go to Font Squirrel's [Webfont Generator](https://www.fontsquirrel.com/tools/webfont-generator)
- Upload your font file(s)

**2. Select Expert Mode:**
- Choose "Expert" mode for full control
- Access all available options and formats

**3. Choose Font Formats:**
Check all necessary formats for maximum browser compatibility:
- ✅ **WOFF2** (Web Open Font Format 2) - Modern browsers
- ✅ **WOFF** (Web Open Font Format) - Older modern browsers
- ✅ **TTF** (TrueType Font) - Fallback support
- ✅ **EOT** (Embedded OpenType) - Legacy IE support
- ✅ **SVG** (Scalable Vector Graphics) - Legacy mobile support

**4. Download Your Kit:**
- Click "Download your kit"
- Extract the ZIP file
- Review the generated files

---

## ⚙️ Font Installation

### Step-by-Step Guide

**1. Create Fonts Directory:**
```bash
# In your WordPress theme directory
mkdir fonts
```

**2. Copy Font Files:**
- Extract font files from the downloaded kit
- Copy all font format files (`.woff`, `.woff2`, `.ttf`, `.eot`, `.svg`)
- Place them in your theme's `fonts/` directory

**3. Review Generated CSS:**
- Open the `stylesheet.css` file from the kit
- Locate the `@font-face` declarations
- Prepare to copy them to your theme's stylesheet

### File Structure

```
your-theme/
├── fonts/
│   ├── font-name.woff2
│   ├── font-name.woff
│   ├── font-name.ttf
│   ├── font-name.eot
│   └── font-name.svg
└── style.css
```

---

## 💻 Implementation

### @font-face Declaration

Copy the `@font-face` rules from the generated `stylesheet.css` to your theme's `style.css`:

```css
@font-face {
  font-family: 'YourFontName';
  src: url('fonts/font-name.eot'); /* IE9 Compat Modes */
  src: url('fonts/font-name.eot?#iefix') format('embedded-opentype'), /* IE6-IE8 */
       url('fonts/font-name.woff2') format('woff2'), /* Modern Browsers */
       url('fonts/font-name.woff') format('woff'), /* Pretty Modern Browsers */
       url('fonts/font-name.ttf') format('truetype'), /* Safari, Android, iOS */
       url('fonts/font-name.svg#font-name') format('svg'); /* Legacy iOS */
  font-weight: normal;
  font-style: normal;
  font-display: swap; /* Improves performance */
}
```

### CSS Integration

**⚠️ Important: Update Font Paths**

Ensure the URL paths in your `@font-face` declarations match your directory structure:

```css
/* If fonts are in a fonts/ subdirectory */
src: url('fonts/font-name.woff2') format('woff2');

/* If fonts are in the theme root */
src: url('font-name.woff2') format('woff2');

/* Absolute path (if needed) */
src: url('/wp-content/themes/your-theme/fonts/font-name.woff2') format('woff2');
```

**Apply Font to Elements:**

```css
body {
  font-family: 'YourFontName', Arial, sans-serif;
}

h1, h2, h3 {
  font-family: 'YourFontName', Georgia, serif;
}
```

---

## 💡 Best Practices

### Performance Optimization

**1. Use Modern Formats First:**
```css
@font-face {
  font-family: 'YourFont';
  src: url('fonts/font.woff2') format('woff2'),
       url('fonts/font.woff') format('woff');
  font-display: swap;
}
```
- WOFF2 provides the best compression
- Omit legacy formats (EOT, SVG) for modern browsers only

**2. Font Display Strategy:**
```css
font-display: swap; /* Show fallback text while font loads */
```

**3. Subset Fonts:**
- Remove unused characters to reduce file size
- Use Font Squirrel's subsetting options
- Consider language-specific subsets

### File Organization

**Recommended structure:**
```
theme/
├── assets/
│   └── fonts/
│       ├── primary-font-regular.woff2
│       ├── primary-font-bold.woff2
│       └── secondary-font-regular.woff2
└── style.css
```

### WordPress Functions

**Enqueue fonts properly in `functions.php`:**
```php
function theme_enqueue_fonts() {
    wp_enqueue_style(
        'custom-fonts',
        get_template_directory_uri() . '/assets/css/fonts.css',
        array(),
        '1.0.0'
    );
}
add_action('wp_enqueue_scripts', 'theme_enqueue_fonts');
```

### Google Fonts Integration

**Alternative: Use Google Fonts API:**
```php
function theme_google_fonts() {
    wp_enqueue_style(
        'google-fonts',
        'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap',
        array(),
        null
    );
}
add_action('wp_enqueue_scripts', 'theme_google_fonts');
```

### Troubleshooting

**Common Issues:**

1. **Fonts are not loading:**
   - Verify file paths in `@font-face` declarations
   - Check file permissions (644 for files, 755 for directories)
   - Inspect the browser console for 404 errors

2. **Cross-Origin Resource Sharing (CORS):**
   ```apache
   # Add to .htaccess if hosting fonts on CDN
   <FilesMatch "\.(ttf|otf|eot|woff|woff2)$">
     Header set Access-Control-Allow-Origin "*"
   </FilesMatch>
   ```

3. **Font not displaying correctly:**
   - Clear browser cache
   - Verify font-family name matches exactly
   - Check for CSS specificity conflicts
