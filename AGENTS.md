# Repository instructions

This repository is public. Treat every tracked file as internet-visible.

## Content rules

- Keep examples fictional and vendor-neutral unless an official public capability is being documented.
- Never add real names, employers, customers, internal product names, private URLs, absolute home-directory paths, credentials, tokens, IDs, screenshots, or proprietary data.
- Separate personal practice from official product behavior. Link official sources for claims about Codex or Obsidian.
- Maintain one canonical document per topic. Update existing files instead of creating `final`, `latest`, `v2`, or duplicate summaries.
- Prefer plain Chinese. Keep the English README concise unless the task explicitly expands the English documentation.

## Verification

After changing public content, run:

```bash
python3 scripts/privacy_scan.py .
python3 -m unittest discover -s tests -v
```

For link or structure changes, also check that every relative Markdown link resolves.

Do not claim publication, security, or end-to-end usability until the corresponding check has actually passed.
