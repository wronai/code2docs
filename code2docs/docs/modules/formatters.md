# formatters

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/__init__.py` | 7 lines

## Overview

Formatters — Markdown rendering, badges, TOC generation.

## Classes

### MarkdownFormatter

Helper for constructing Markdown documents.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self` | `—` | 1 |
| `heading` | `self, text, level` | `—` | 1 |
| `paragraph` | `self, text` | `—` | 1 |
| `blockquote` | `self, text` | `—` | 1 |
| `code_block` | `self, code, language` | `—` | 1 |
| `inline_code` | `self, text` | `—` | 1 |
| `bold` | `self, text` | `—` | 1 |
| `link` | `self, text, url` | `—` | 1 |
| `list_item` | `self, text, indent` | `—` | 1 |
| `table` | `self, headers, rows` | `—` | 4 |
| `separator` | `self` | `—` | 1 |
| `blank` | `self` | `—` | 1 |
| `render` | `self` | `—` | 1 |

## Functions

### `generate_badges(project_name, badge_types, stats, deps)`

Generate shields.io badge Markdown strings.

**Calls:** `None.join`, `formatters.badges._make_badge`, `badges.append`

**Called by:** `generators.readme_gen.ReadmeGenerator._build_context`, `generators.readme_gen.ReadmeGenerator._build_context`

### `_make_badge(badge_type, project_name, stats, deps)`

Create a single badge Markdown string.

**Calls:** `quote`, `quote`, `hasattr`, `stats.get`

**Called by:** `formatters.badges.generate_badges`, `formatters.badges.generate_badges`

### `generate_toc(markdown_content, max_depth)`

Generate a table of contents from Markdown headings.

Args:
    markdown_content: Full Markdown document.
    max_depth: Maximum heading level to include (1-6).

Returns:
    TOC as Markdown string.

**Calls:** `formatters.toc.extract_headings`, `lines.append`, `None.join`, `lines.append`

### `extract_headings(content, max_depth)`

Extract headings from Markdown content.

Returns list of (level, text, anchor) tuples.

**Calls:** `content.splitlines`, `None.startswith`, `re.match`, `len`, `line.strip`, `match.group`, `None.strip`, `formatters.toc._slugify`, `headings.append`, `match.group`

**Called by:** `formatters.toc.generate_toc`, `formatters.toc.generate_toc`

### `_slugify(text)`

Convert heading text to GitHub-compatible anchor slug.

**Calls:** `text.lower`, `re.sub`, `re.sub`, `slug.strip`

**Called by:** `formatters.toc.extract_headings`, `formatters.toc.extract_headings`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 7 |
| Functions | 0 |
| Classes | 0 |
