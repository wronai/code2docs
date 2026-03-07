# registry

> Source: `/home/tom/github/wronai/code2docs/code2docs/registry.py` | 39 lines | CC avg: 2.5

## Overview

Generator registry — pluggable generator system.

## Classes

### GeneratorRegistry

Registry of documentation generators.

Generators register themselves via :meth:`register`. The CLI calls
:meth:`run_all` which iterates registered generators in priority order.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self` | `—` | 1 |
| `add` | `self, generator` | `—` | 1 |
| `run_all` | `self, ctx` | `—` | 4 |
| `run_only` | `self, name, ctx` | `—` | 4 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 39 |
| Complexity (avg) | 2.5 |
| Functions | 4 |
| Classes | 1 |
| Fan-out | 6 |
