# generators.readme_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/readme_gen.py` | 261 lines | CC avg: 3.9

## Overview

README.md generator from AnalysisResult.

## Classes

### ReadmeGenerator

Generate README.md from AnalysisResult.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self` | `—` | 3 |
| `_build_context` | `self, project_name` | `—` | 7 |
| `_calc_avg_complexity` | `self` | `—` | 4 |
| `_build_module_tree` | `self` | `—` | 7 |
| `_build_manual` | `self, project_name, sections, context` | `—` | 6 |
| `_build_overview_section` | `project_name, context` | `—` | 3 |
| `_build_install_section` | `_project_name, context` | `—` | 4 |
| `_build_quickstart_section` | `_project_name, context` | `—` | 2 |
| `_build_api_section` | `_project_name, context` | `—` | 5 |
| `_build_structure_section` | `_project_name, context` | `—` | 2 |
| `_build_endpoints_section` | `_project_name, context` | `—` | 3 |
| `write` | `self, path, content` | `—` | 4 |

## Functions

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

**Calls:** `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 261 |
| Complexity (avg) | 3.9 |
| Functions | 14 |
| Classes | 1 |
| Fan-out | 92 |
