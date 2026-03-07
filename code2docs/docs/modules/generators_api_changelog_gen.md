# generators.api_changelog_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/api_changelog_gen.py` | 196 lines | CC avg: 5.4

## Overview

API changelog generator — diff function/class signatures between versions.

## Classes

### ApiChange

A single API change between two analysis snapshots.

### ApiChangelogGenerator

Generate API changelog by diffing current analysis with a saved snapshot.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self, project_path` | `—` | 2 |
| `save_snapshot` | `self, project_path` | `—` | 1 |
| `_build_snapshot` | `self` | `—` | 6 |
| `_load_snapshot` | `path` | `—` | 3 |
| `_diff` | `self, old, new` | `—` | 2 |
| `_diff_functions` | `old, new, changes` | `—` | 10 |
| `_diff_classes` | `old, new, changes` | `—` | 10 |
| `_render` | `project_name, changes, has_baseline` | `—` | 14 ⚠️ |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 196 |
| Complexity (avg) | 5.4 |
| Functions | 9 |
| Classes | 2 |
| Fan-out | 80 |
