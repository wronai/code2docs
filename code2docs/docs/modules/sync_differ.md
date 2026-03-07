# sync.differ

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/differ.py` | 125 lines | CC avg: 3.6

## Overview

Detect changes in source code for selective documentation regeneration.

## Classes

### ChangeInfo

Describes a detected change.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__str__` | `self` | `—` | 1 |

### Differ

Detect changes between current source and previous state.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | 2 |
| `detect_changes` | `self, project_path` | `—` | 6 |
| `save_state` | `self, project_path` | `—` | 1 |
| `_load_state` | `self, state_path` | `—` | 3 |
| `_compute_state` | `self, project` | `—` | 6 |
| `_file_to_module` | `filepath, project` | `—` | 6 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 125 |
| Complexity (avg) | 3.6 |
| Functions | 7 |
| Classes | 2 |
| Fan-out | 39 |
