# sync

> Source: `/home/tom/github/wronai/code2docs/code2docs/sync/__init__.py` | 6 lines

## Overview

Sync — detect changes and selectively regenerate documentation.

## Classes

### Updater

Apply selective documentation updates based on detected changes.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | 2 |
| `apply` | `self, project_path, changes` | `—` | 12 ⚠️ |

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

## Functions

### `start_watcher(project_path, config)`

Start watching project for file changes and auto-resync docs.

Requires watchdog package: pip install code2docs[watch]

**Calls:** `None.resolve`, `DocsHandler`, `Observer`, `observer.schedule`, `observer.start`, `observer.join`, `Code2DocsConfig`, `str`, `ImportError`, `Path`

**Called by:** `cli._run_watch`, `cli._run_watch`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 6 |
| Functions | 0 |
| Classes | 0 |
