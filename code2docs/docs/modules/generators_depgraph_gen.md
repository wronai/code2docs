# generators.depgraph_gen

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/depgraph_gen.py` | 140 lines | CC avg: 3.9

## Overview

Dependency graph generator — Mermaid diagram from coupling matrix.

## Classes

### DepGraphGenerator

Generate docs/dependency-graph.md with Mermaid diagrams.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self` | `—` | 2 |
| `_collect_edges` | `self` | `—` | 7 |
| `_extract_imports_from_file` | `file_path` | `—` | 7 |
| `_import_matches` | `imp, module` | `—` | 2 |
| `_render_mermaid` | `self, edges` | `—` | 3 |
| `_render_matrix` | `self, edges` | `—` | 9 |
| `_calc_degrees` | `edges` | `—` | 2 |
| `_render_degree_table` | `self, in_deg, out_deg` | `—` | 2 |

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 140 |
| Complexity (avg) | 3.9 |
| Functions | 9 |
| Classes | 1 |
| Fan-out | 51 |
