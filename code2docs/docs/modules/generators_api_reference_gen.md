# generators.api_reference_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/api_reference_gen.py` | 162 lines | CC avg: 4.0

## Overview

API reference documentation generator — per-module API docs.

## Classes

### ApiReferenceGenerator

Generate docs/api/ — per-module API reference from signatures.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate_all` | `self` | `—` | 2 |
| `_generate_index` | `self` | `—` | 2 |
| `_generate_module_api` | `self, mod_name, mod_info` | `—` | 3 |
| `_render_api_header` | `self, mod_name, mod_info` | `—` | 1 |
| `_render_api_classes` | `self, mod_name` | `—` | 13 ⚠️ |
| `_render_api_functions` | `self, mod_name` | `—` | 11 ⚠️ |
| `_render_api_imports` | `self, mod_info` | `—` | 3 |
| `_get_class_methods` | `self, cls_info` | `—` | 4 |
| `_format_signature` | `func` | `—` | 2 |
| `write_all` | `self, output_dir, files` | `—` | 2 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 162 |
| Complexity (avg) | 4.0 |
| Functions | 11 |
| Classes | 1 |
| Fan-out | 68 |
