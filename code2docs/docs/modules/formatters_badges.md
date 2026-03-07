# formatters.badges

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/badges.py` | 52 lines | CC avg: 7.5

## Overview

Badge generation using shields.io URLs.

## Functions

### `generate_badges(project_name, badge_types, stats, deps)`

Generate shields.io badge Markdown strings.

**Calls:** `None.join`, `formatters.badges._make_badge`, `badges.append`

**Called by:** `generators.readme_gen.ReadmeGenerator._build_context`, `generators.readme_gen.ReadmeGenerator._build_context`

### `_make_badge(badge_type, project_name, stats, deps)`

Create a single badge Markdown string.

**Calls:** `quote`, `quote`, `hasattr`, `stats.get`

**Called by:** `formatters.badges.generate_badges`, `formatters.badges.generate_badges`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 52 |
| Complexity (avg) | 7.5 |
| Functions | 2 |
| Classes | 0 |
| Fan-in | 4 |
| Fan-out | 7 |
