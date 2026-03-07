# generators.changelog_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/changelog_gen.py` | 121 lines | CC avg: 3.5

## Overview

Changelog generator from git log and API diff.

## Classes

### ChangelogEntry

A single changelog entry.

### ChangelogGenerator

Generate CHANGELOG.md from git log and analysis diff.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self, project_path, max_entries` | `—` | 3 |
| `_get_git_log` | `self, project_path, max_entries` | `—` | 5 |
| `_classify_message` | `self, message` | `—` | 4 |
| `_group_by_type` | `self, entries` | `—` | 2 |
| `_render` | `self, grouped` | `—` | 6 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 121 |
| Complexity (avg) | 3.5 |
| Functions | 6 |
| Classes | 2 |
| Fan-out | 28 |
