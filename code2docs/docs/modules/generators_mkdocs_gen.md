# generators.mkdocs_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/mkdocs_gen.py` | 79 lines | CC avg: 3.0

## Overview

MkDocs configuration generator — auto-generate mkdocs.yml from docs tree.

## Classes

### MkDocsGenerator

Generate mkdocs.yml from the docs/ directory structure.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self, docs_dir` | `—` | 2 |
| `_build_nav` | `self, docs_dir` | `—` | 8 |
| `write` | `self, output_path, content` | `—` | 1 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 79 |
| Complexity (avg) | 3.0 |
| Functions | 4 |
| Classes | 1 |
| Fan-out | 20 |
