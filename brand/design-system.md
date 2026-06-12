---
layout: default
title: Design System
nav_order: 1
parent: Brand
permalink: /brand/design-system/
---

# Dew Monday Design System

Full design token specifications for all brand concepts. These JSON blocks are structured to be portable across web apps, docs sites, and static site generators.

---

## Global Foundation Tokens

```json
{
	"$schema": "https://design-tokens.github.io/community-group/format/",
	"color": {
		"bg": { "value": "#F5F0E8" },
		"bgAlt": { "value": "#FDFAF4" },
		"text": { "value": "#1C1C1C" },
		"textMuted": { "value": "#6B6B6B" },
		"border": { "value": "#E2DDD6" },
		"primary": { "value": "#2D5A27" },
		"accent": { "value": "#6BA3BE" },
		"accentWarm": { "value": "#D4703A" },
		"success": { "value": "#2E7D32" },
		"warning": { "value": "#C77D2B" },
		"danger": { "value": "#B23A2F" }
	},
	"font": {
		"family": {
			"display": { "value": "DM Serif Display, Georgia, serif" },
			"body": { "value": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" },
			"mono": { "value": "JetBrains Mono, ui-monospace, SFMono-Regular, monospace" }
		},
		"size": {
			"xs": { "value": "0.75rem" },
			"sm": { "value": "0.875rem" },
			"md": { "value": "1rem" },
			"lg": { "value": "1.25rem" },
			"xl": { "value": "1.5rem" },
			"2xl": { "value": "2rem" },
			"3xl": { "value": "2.75rem" }
		},
		"weight": {
			"light": { "value": "300" },
			"regular": { "value": "400" },
			"medium": { "value": "500" },
			"semibold": { "value": "600" },
			"bold": { "value": "700" }
		},
		"lineHeight": {
			"tight": { "value": "1.2" },
			"normal": { "value": "1.5" },
			"relaxed": { "value": "1.7" }
		}
	},
	"space": {
		"1": { "value": "0.25rem" },
		"2": { "value": "0.5rem" },
		"3": { "value": "0.75rem" },
		"4": { "value": "1rem" },
		"6": { "value": "1.5rem" },
		"8": { "value": "2rem" },
		"10": { "value": "2.5rem" },
		"12": { "value": "3rem" },
		"16": { "value": "4rem" }
	},
	"radius": {
		"sm": { "value": "6px" },
		"md": { "value": "10px" },
		"lg": { "value": "16px" },
		"pill": { "value": "999px" }
	},
	"shadow": {
		"sm": { "value": "0 1px 2px rgba(28, 28, 28, 0.08)" },
		"md": { "value": "0 6px 20px rgba(28, 28, 28, 0.12)" },
		"lg": { "value": "0 12px 32px rgba(28, 28, 28, 0.16)" }
	},
	"motion": {
		"duration": {
			"fast": { "value": "120ms" },
			"normal": { "value": "220ms" },
			"slow": { "value": "360ms" }
		},
		"easing": {
			"standard": { "value": "cubic-bezier(0.2, 0, 0, 1)" },
			"inOut": { "value": "cubic-bezier(0.4, 0, 0.2, 1)" }
		}
	}
}
```

---

## Semantic UI Tokens

```json
{
	"surface": {
		"page": { "value": "{color.bg}" },
		"card": { "value": "{color.bgAlt}" },
		"inverse": { "value": "{color.text}" }
	},
	"content": {
		"primary": { "value": "{color.text}" },
		"secondary": { "value": "{color.textMuted}" },
		"onPrimary": { "value": "#FFFFFF" },
		"onAccent": { "value": "#10242E" }
	},
	"action": {
		"primaryBg": { "value": "{color.primary}" },
		"primaryText": { "value": "#FFFFFF" },
		"secondaryBg": { "value": "{color.accent}" },
		"secondaryText": { "value": "#10242E" },
		"dangerBg": { "value": "{color.danger}" },
		"dangerText": { "value": "#FFFFFF" }
	},
	"focus": {
		"ring": { "value": "0 0 0 3px rgba(107, 163, 190, 0.45)" }
	}
}
```

---

## Concept Theme Tokens

```json
{
	"themes": {
		"cameraDropshipping": {
			"color": {
				"primary": "#1E3A5F",
				"accent": "#5CA0D3",
				"bg": "#F3F6FA",
				"bgAlt": "#FFFFFF"
			}
		},
		"artDropshipping": {
			"color": {
				"primary": "#5A2D4F",
				"accent": "#D6853E",
				"bg": "#F8F3EF",
				"bgAlt": "#FFFDF9"
			}
		},
		"artTutorialApp": {
			"color": {
				"primary": "#1F5B47",
				"accent": "#E3A72F",
				"bg": "#F2F7F4",
				"bgAlt": "#FFFFFF"
			}
		},
		"creatorHub": {
			"color": {
				"primary": "#2F3A66",
				"accent": "#4CAEA3",
				"bg": "#F4F5FA",
				"bgAlt": "#FFFFFF"
			}
		},
		"littleMakers": {
			"color": {
				"primary": "#2D5A27",
				"accent": "#D4703A",
				"bg": "#FFF7EE",
				"bgAlt": "#FFFFFF"
			}
		}
	}
}
```

---

## CSS Variable Export (Reference)

```json
{
	"cssVariables": {
		"--dm-color-bg": "{color.bg}",
		"--dm-color-bg-alt": "{color.bgAlt}",
		"--dm-color-text": "{color.text}",
		"--dm-color-text-muted": "{color.textMuted}",
		"--dm-color-primary": "{color.primary}",
		"--dm-color-accent": "{color.accent}",
		"--dm-font-display": "{font.family.display}",
		"--dm-font-body": "{font.family.body}",
		"--dm-space-4": "{space.4}",
		"--dm-radius-md": "{radius.md}",
		"--dm-shadow-md": "{shadow.md}",
		"--dm-motion-normal": "{motion.duration.normal}"
	}
}
```

---

## Accessibility Guardrails

- Body text contrast target is 4.5:1 minimum.
- Interactive text contrast target is 4.5:1 minimum in default and hover states.
- Focus styles must remain visible on all themed surfaces.
- Motion tokens should support a reduced-motion fallback in implementation.

