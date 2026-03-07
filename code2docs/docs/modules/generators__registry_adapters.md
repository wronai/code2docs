# generators._registry_adapters

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/_registry_adapters.py` | 173 lines | CC avg: 1.8

## Overview

Registry adapters — wrap existing generators into BaseGenerator interface.

## Classes

### ReadmeGeneratorAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 1 |
| `run` | `self, ctx` | `—` | 3 |

### ApiReferenceAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 2 |
| `run` | `self, ctx` | `—` | 2 |

### ModuleDocsAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 2 |
| `run` | `self, ctx` | `—` | 2 |

### ArchitectureAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 2 |
| `run` | `self, ctx` | `—` | 2 |

### DepGraphAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 1 |
| `run` | `self, ctx` | `—` | 2 |

### CoverageAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 1 |
| `run` | `self, ctx` | `—` | 2 |

### ApiChangelogAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 1 |
| `run` | `self, ctx` | `—` | 2 |

### ExamplesAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 2 |
| `run` | `self, ctx` | `—` | 2 |

### MkDocsAdapter

*Bases:* `BaseGenerator`

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `self` | `—` | 1 |
| `run` | `self, ctx` | `—` | 2 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 173 |
| Complexity (avg) | 1.8 |
| Functions | 18 |
| Classes | 9 |
| Fan-out | 47 |
