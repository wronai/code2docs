# generators.examples_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/examples_gen.py` | 198 lines | CC avg: 6.0

## Overview

Auto-generate usage examples from public signatures and entry points.

## Classes

### ExamplesGenerator

Generate examples/ — usage examples from public API signatures.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate_all` | `self` | `—` | 4 |
| `_generate_basic_usage` | `self` | `—` | 10 |
| `_generate_import_section` | `self, project_name, public_classes, public_functions` | `—` | 7 |
| `_generate_class_usage_section` | `self, public_classes` | `—` | 8 |
| `_generate_function_usage_section` | `self, public_functions` | `—` | 5 |
| `_generate_entry_point_examples` | `self` | `—` | 7 |
| `_generate_class_examples` | `self, classes` | `—` | 12 ⚠️ |
| `_get_major_classes` | `self` | `—` | 3 |
| `_get_init_args` | `self, cls` | `—` | 7 |
| `_get_public_methods` | `self, cls` | `—` | 6 |
| `write_all` | `self, output_dir, files` | `—` | 2 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 198 |
| Complexity (avg) | 6.0 |
| Functions | 12 |
| Classes | 1 |
| Fan-out | 71 |
