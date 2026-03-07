# analyzers.dependency_scanner

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/dependency_scanner.py` | 159 lines | CC avg: 4.5

## Overview

Scan project dependencies from requirements.txt, pyproject.toml, setup.py.

## Classes

### DependencyInfo

Information about a project dependency.

### ProjectDependencies

All detected project dependencies.

### DependencyScanner

Scan and parse project dependency files.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `scan` | `self, project_path` | `—` | 4 |
| `_parse_pyproject` | `self, path` | `—` | 8 |
| `_parse_pyproject_regex` | `self, path` | `—` | 4 |
| `_parse_setup_py` | `self, path` | `—` | 4 |
| `_parse_requirements_txt` | `self, path` | `—` | 5 |
| `_parse_dep_string` | `dep_str` | `—` | 2 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 159 |
| Complexity (avg) | 4.5 |
| Functions | 6 |
| Classes | 3 |
| Fan-out | 55 |
