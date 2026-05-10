# Contributing to Awesome OpenClaw

Thank you for your interest in contributing!

## Website

This repo powers [openclawsearch.com](https://openclawsearch.com). The website **automatically renders README.md** — any change you make to the README will appear on the website after merge. No separate website edits needed.

### How It Works

- `index.html` fetches `README.md` at runtime and renders it with [marked.js](https://github.com/markedjs/marked)
- Tables, code blocks, sections, and nav links are all generated from your markdown
- `directory.html` is a separate curated page for ecosystem projects built with OpenClaw

## Validation

### Before opening a PR

Run the lightweight static checks:

```bash
python3 scripts/validate_static.py
```

This validates JSON, basic HTML structure, Vercel rewrite destinations, and README anchors for both GitHub and the website renderer.

## How to Add a Resource

1. Fork this repository
2. Add your resource to the appropriate section in `README.md`
3. Follow the existing format (title, link, description)
4. Submit a pull request

### Format

Use the existing patterns in each section:

**For links/tools:**
```markdown
- [Resource Name](https://link.com) — Short description (1-2 sentences)
```

**For table rows:**
```markdown
| **Provider** | Link | Price | Details |
```

## How to Add a Project to the Directory

The [Ecosystem Directory](https://openclawsearch.com/directory.html) showcases projects built with OpenClaw.

1. Fork this repository
2. Edit `directory.html`
3. Add a card in the appropriate category section
4. Use this template:

```html
<div class="card" data-cat="CATEGORY" data-tier="TIER">
<div class="card-tier TIER">TIER_LETTER</div>
<div class="card-header">
<div class="card-icon">EMOJI</div>
<div class="card-title-wrap">
<div class="card-title"><a href="URL" target="_blank" rel="noopener">Project Name</a></div>
<div class="card-author">by @author</div>
</div>
</div>
<div class="card-desc">Short description of what the project does.</div>
<div class="card-meta">
<span class="card-tag">Tag1</span>
<span class="card-tag">Tag2</span>
<span class="card-stars">&#9733; STARS</span>
</div>
</div>
```

**Categories:** `social`, `devtools`, `automation`, `infra`, `hardware`, `defi`, `voice`, `memory`

**Tiers:** `s` (must-see), `a` (excellent), `b` (solid), `c` (notable)

## Guidelines

- Ensure the resource is relevant to OpenClaw
- Check that the link is working
- Keep descriptions concise (1-2 sentences)
- Add new resources at the bottom of the relevant section
- One resource per pull request is preferred
- Do NOT edit `index.html` to add content — edit `README.md` instead

## Reporting Issues

- Broken links
- Outdated information
- Incorrect pricing or specifications
- Missing important resources
- Website rendering issues

Please open an [issue](https://github.com/rohitg00/awesome-openclaw/issues) with details.
