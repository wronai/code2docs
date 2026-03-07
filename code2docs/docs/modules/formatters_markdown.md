# formatters.markdown

> Source: `/home/tom/github/wronai/code2docs/code2docs/formatters/markdown.py` | 73 lines | CC avg: 1.2

## Overview

Markdown formatting utilities.

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

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 73 |
| Complexity (avg) | 1.2 |
| Functions | 13 |
| Classes | 1 |
| Fan-out | 18 |
