# base

> Source: `/home/tom/github/wronai/code2docs/code2docs/base.py` | 46 lines | CC avg: 1.0

## Overview

Base generator interface and generation context.

## Classes

### GenerateContext

Shared context passed to all generators during a run.

### BaseGenerator

*Bases:* `ABC`

Abstract base for all documentation generators.

Subclasses must define ``name`` and implement ``should_run`` / ``run``.
Adding a new generator requires only creating a subclass and registering it
with the :class:`GeneratorRegistry`; no changes to ``cli.py`` needed.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `should_run` | `self` | `—` | 1 |
| `run` | `self, ctx` | `—` | 1 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 46 |
| Complexity (avg) | 1.0 |
| Functions | 3 |
| Classes | 2 |
