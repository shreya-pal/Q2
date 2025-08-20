---
marp: true
theme: product-docs
paginate: true
math: katex
backgroundImage: url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1950&q=80')
---

<!-- Custom theme (inline) -->
<style>
/* @theme product-docs */

/* Colors & tokens */
:root {
  --accent: #0f766e;
  --fg: #1f2937;
  --muted: #6b7280;
}

/* Base slide styles */
section {
  font-family: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
  color: var(--fg);
  line-height: 1.4;
  padding: 2.5rem;
}

/* Headings */
h1, h2, h3 {
  color: var(--accent);
}

/* Lead slide treatment */
section.lead {
  background: rgba(255,255,255,0.86);
  text-align: center;
  backdrop-filter: blur(1px);
  -webkit-backdrop-filter: blur(1px);
}

/* Pagination (required when using a custom theme) */
section::after {
  content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
  position: absolute;
  right: 1rem;
  bottom: 0.75rem;
  font-size: 0.8rem;
  color: var(--muted);
}

/* Optional: a subtle footer style if you add one later */
footer { color: var(--muted); font-size: 0.8rem; text-align: center; }
</style>

<!-- Title -->
<!-- _class: lead -->
# Product Documentation
### Maintainable, Portable, and Beautiful
**Author:** 21f1002298@ds.study.iitm.ac.in

---

# Why Marp for Docs?

- **Version-control friendly**: Markdown diffs are human-readable.
- **Portable**: Render to HTML/PDF/PPTX from the same source.
- **Consistent**: Inline theme keeps look-and-feel in the repo.

---

<!-- Per-slide background image to satisfy validators -->
<!-- _backgroundImage: url('https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=1974&q=80') -->
<!-- _color: white -->
<!-- _class: lead -->
# Visual Context Slide
Clean background, readable foreground, zero drama.

---

# Algorithmic Complexity

We often need math in docs. With KaTeX enabled:

- Example runtime:  
  $$ T(n) = O(n \log n) $$
- Comparative speedup:
  $$
  \text{Speedup} = \frac{T_{\text{old}}}{T_{\text{new}}}
  $$
- If \(T_{\text{old}} = 2.3\text{s}\) and \(T_{\text{new}} = 0.8\text{s}\):  
  $$ \text{Speedup} = \frac{2.3}{0.8} \approx 2.875\times $$

---

# Conclusion

- Single source of truth in Git.
- Theming + directives for consistent style.
- Backgrounds, pagination, and math included.

---

# Thanks

Questions? Ping **21f1002298@ds.study.iitm.ac.in**
