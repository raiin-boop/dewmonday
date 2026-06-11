# Dew Monday — Design System Parameters

> Central design token reference for all Dew Monday concepts. Each concept extends the global brand tokens with its own layout, color accent, and component styles.

---

## Global Brand Tokens

```json
{
  "brand": "Dew Monday",
  "version": "1.0.0",
  "colors": {
    "background": "#F5F0E8",
    "surface": "#FFFFFF",
    "primary": "#2D5A27",
    "primaryHover": "#1F4A1A",
    "accent": "#6BA3BE",
    "accentHover": "#5890A8",
    "text": "#1C1C1C",
    "textSecondary": "#5A5A5A",
    "muted": "#8C8C8C",
    "border": "#E0DAD0",
    "error": "#C43D3D",
    "success": "#2D5A27",
    "warning": "#C48B2C"
  },
  "typography": {
    "display": {
      "family": "DM Serif Display, serif",
      "weights": [400]
    },
    "heading": {
      "family": "DM Serif Display, serif",
      "weights": [400]
    },
    "body": {
      "family": "Inter, sans-serif",
      "weights": [400, 500, 600]
    },
    "ui": {
      "family": "Inter, sans-serif",
      "weights": [500, 600, 700]
    },
    "mono": {
      "family": "JetBrains Mono, monospace",
      "weights": [400, 500]
    }
  },
  "spacing": {
    "xs": "4px",
    "sm": "8px",
    "md": "16px",
    "lg": "24px",
    "xl": "32px",
    "2xl": "48px",
    "3xl": "64px",
    "4xl": "96px"
  },
  "radius": {
    "sm": "4px",
    "md": "8px",
    "lg": "12px",
    "xl": "16px",
    "full": "9999px"
  },
  "shadow": {
    "sm": "0 1px 2px rgba(0,0,0,0.06)",
    "md": "0 4px 12px rgba(0,0,0,0.08)",
    "lg": "0 8px 24px rgba(0,0,0,0.10)",
    "xl": "0 16px 48px rgba(0,0,0,0.12)"
  }
}
```

---

## Concept-Specific Design Systems

### 1. Camera Dropshipping

```json
{
  "concept": "camera-dropshipping",
  "archetype": "E-commerce + Photography",
  "layout": "product-first",
  "grid": "12-column, product cards 3-up desktop / 1-up mobile",
  "hero": "full-bleed product photography with editorial overlay",
  "colors": {
    "accent": "#D4A843",
    "accentHover": "#BF9635",
    "surface": "#FAFAFA",
    "badge": "#2D5A27"
  },
  "components": {
    "productCard": {
      "radius": "12px",
      "shadow": "md",
      "hoverLift": "4px",
      "imageRatio": "4:3",
      "priceFont": "ui / 600"
    },
    "trustBar": {
      "icons": ["shield-check", "truck", "rotate-ccw"],
      "background": "primary"
    },
    "comparisonTable": {
      "stickyHeader": true,
      "highlightColumn": "recommended"
    }
  }
}
```

### 2. Art Dropshipping

```json
{
  "concept": "art-dropshipping",
  "archetype": "Luxury E-commerce + Art Gallery",
  "layout": "masonry-gallery",
  "grid": "masonry, 3-col desktop / 1-col mobile, generous whitespace",
  "hero": "rotating featured artwork with artist name overlay",
  "colors": {
    "accent": "#8B5E3C",
    "accentHover": "#6F4A2D",
    "surface": "#FAF8F5",
    "limitedEdition": "#C43D3D"
  },
  "components": {
    "artCard": {
      "radius": "4px",
      "shadow": "lg",
      "hoverScale": "1.02",
      "imageRatio": "original (preserve aspect)",
      "artistBadge": true
    },
    "dropBanner": {
      "countdown": true,
      "background": "linear-gradient(135deg, #2D5A27, #1F4A1A)",
      "cta": "Shop the Drop"
    },
    "artistStory": {
      "layout": "split — portrait left, bio right",
      "pullQuote": true
    }
  }
}
```

### 3. Art Tutorial App

```json
{
  "concept": "art-tutorial-app",
  "archetype": "EdTech",
  "layout": "progress-centric",
  "grid": "content well max-w-3xl centered, sidebar for track nav",
  "hero": "current lesson progress + next-up card",
  "colors": {
    "accent": "#7C5CBF",
    "accentHover": "#6A4BA6",
    "surface": "#F8F6FF",
    "progressBar": "#2D5A27",
    "completed": "#A3D9A5"
  },
  "components": {
    "lessonCard": {
      "radius": "12px",
      "shadow": "sm",
      "statusDot": ["locked", "available", "in-progress", "completed"],
      "projectThumbnail": true
    },
    "videoPlayer": {
      "controls": "custom, brand-colored scrubber",
      "chaptering": true,
      "downloadButton": true
    },
    "projectGallery": {
      "layout": "grid 3-up",
      "lightbox": true,
      "communityVoting": false
    }
  }
}
```

### 4. Creator Hub

```json
{
  "concept": "creator-hub",
  "archetype": "Editorial Media",
  "layout": "newsletter-first",
  "grid": "single-column content well max-w-2xl, sidebar for nav/resources",
  "hero": "latest newsletter issue with featured pull-quote",
  "colors": {
    "accent": "#6BA3BE",
    "accentHover": "#5890A8",
    "surface": "#F5F8FA",
    "proTier": "#D4A843"
  },
  "components": {
    "newsletterCard": {
      "radius": "8px",
      "shadow": "sm",
      "readTime": true,
      "issueNumber": true
    },
    "resourceCard": {
      "radius": "8px",
      "tag": ["tool", "template", "guide", "community"],
      "externalLink": true
    },
    "memberCard": {
      "avatar": true,
      "tier": ["free", "pro", "founding"],
      "joinDate": true
    }
  }
}
```

---

## Pre-Delivery Checklist

Before shipping any concept page, verify:

- [ ] All colors reference global tokens or concept overrides above
- [ ] Typography uses DM Serif Display for headings, Inter for body, JetBrains Mono for code
- [ ] Spacing follows the spacing scale (no magic numbers)
- [ ] Radius values match token definitions
- [ ] Shadows use the defined scale (sm / md / lg / xl)
- [ ] Mobile-first responsive breakpoints at 768px and 1024px
- [ ] Touch targets minimum 44×44px
- [ ] Brand voice passes stop-slop review

---

## Font Loading

Include in every HTML page `<head>`:

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
```

---

*Part of the [Dew Monday](../README.md) brand incubator.*
