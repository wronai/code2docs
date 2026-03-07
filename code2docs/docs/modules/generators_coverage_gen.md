# generators.coverage_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/coverage_gen.py` | 104 lines | CC avg: 4.4

## Overview

Docstring coverage report generator.

## Classes

### CoverageGenerator

Generate docs/coverage.md — docstring coverage report.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self` | `—` | 2 |
| `_render_summary` | `report` | `—` | 3 |
| `_render_per_module` | `self` | `—` | 1 |
| `_collect_module_stats` | `self` | `—` | 12 ⚠️ |
| `_format_coverage_table` | `stats` | `—` | 4 |
| `_render_undocumented` | `self` | `—` | 8 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 104 |
| Complexity (avg) | 4.4 |
| Functions | 7 |
| Classes | 1 |
| Fan-out | 30 |
