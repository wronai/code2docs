# generators.module_docs_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/module_docs_gen.py` | 220 lines | CC avg: 4.6

## Overview

Per-module detailed documentation generator.

## Classes

### ModuleDocsGenerator

Generate docs/modules/ — detailed per-module documentation.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate_all` | `self` | `—` | 2 |
| `_generate_module` | `self, mod_name, mod_info` | `—` | 3 |
| `_render_header` | `self, mod_name, mod_info` | `—` | 3 |
| `_render_overview` | `self, mod_info` | `—` | 2 |
| `_render_classes_section` | `self, mod_name` | `—` | 12 ⚠️ |
| `_render_functions_section` | `self, mod_name` | `—` | 9 |
| `_render_dependencies_section` | `self, mod_info` | `—` | 10 |
| `_render_metrics_section` | `self, mod_name, mod_info` | `—` | 3 |
| `_count_file_lines` | `self, file_path` | `—` | 3 |
| `_calc_module_avg_cc` | `self, mod_name` | `—` | 5 |
| `_get_module_docstring` | `self, mod_info` | `—` | 4 |
| `_get_module_classes` | `self, mod_name` | `—` | 4 |
| `_get_module_functions` | `self, mod_name` | `—` | 5 |
| `_get_class_methods` | `self, cls_info` | `—` | 4 |
| `_get_module_metrics` | `self, mod_name, mod_info` | `—` | 7 |
| `write_all` | `self, output_dir, files` | `—` | 2 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 220 |
| Complexity (avg) | 4.6 |
| Functions | 17 |
| Classes | 1 |
| Fan-out | 105 |
