# Static validation

This repo is mostly static Markdown, HTML, JSON, and Vercel routing.

Run the lightweight local validation before opening PRs:

```bash
python3 scripts/validate_static.py
```

The script uses only the Python standard library and checks:

- JSON parsing.
- basic HTML parser sanity.
- Vercel rewrite destinations.
- README internal anchor links for GitHub and the website renderer.
