# generators

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/__init__.py` | 53 lines | CC avg: 5.0

## Overview

Documentation generators — produce Markdown, examples, and diagrams.

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

### CoverageGenerator

Generate docs/coverage.md — docstring coverage report.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self` | `—` | 2 |
| `_render_summary` | `report` | `—` | 3 |
| `_render_per_module` | `self` | `—` | 1 |
| `_collect_module_stats` | `self` | `—` | 12 ⚠️ |
| `_format_coverage_table` | `stats` | `—` | 4 |
| `_render_undocumented` | `self` | `—` | 8 |

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

### ChangelogEntry

A single changelog entry.

### ChangelogGenerator

Generate CHANGELOG.md from git log and analysis diff.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self, project_path, max_entries` | `—` | 3 |
| `_get_git_log` | `self, project_path, max_entries` | `—` | 5 |
| `_classify_message` | `self, message` | `—` | 4 |
| `_group_by_type` | `self, entries` | `—` | 2 |
| `_render` | `self, grouped` | `—` | 6 |

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

### MkDocsGenerator

Generate mkdocs.yml from the docs/ directory structure.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self, docs_dir` | `—` | 2 |
| `_build_nav` | `self, docs_dir` | `—` | 8 |
| `write` | `self, output_path, content` | `—` | 1 |

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

### ArchitectureGenerator

Generate docs/architecture.md — architecture overview with diagrams.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self` | `—` | 12 ⚠️ |
| `_generate_module_graph` | `self` | `—` | 9 |
| `_generate_class_diagram` | `self` | `—` | 11 ⚠️ |
| `_detect_layers` | `self` | `—` | 8 |
| `_generate_metrics_table` | `self` | `—` | 6 |

### ApiChange

A single API change between two analysis snapshots.

### ApiChangelogGenerator

Generate API changelog by diffing current analysis with a saved snapshot.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config, result` | `—` | 1 |
| `generate` | `self, project_path` | `—` | 2 |
| `save_snapshot` | `self, project_path` | `—` | 1 |
| `_build_snapshot` | `self` | `—` | 6 |
| `_load_snapshot` | `path` | `—` | 3 |
| `_diff` | `self, old, new` | `—` | 2 |
| `_diff_functions` | `old, new, changes` | `—` | 10 |
| `_diff_classes` | `old, new, changes` | `—` | 10 |
| `_render` | `project_name, changes, has_baseline` | `—` | 14 ⚠️ |

## Functions

### `generate_readme(project_path, output, sections, sync_markers, config)`

Convenience function to generate a README.

**Calls:** `ProjectScanner`, `scanner.analyze`, `ReadmeGenerator`, `gen.generate`, `gen.write`, `Code2DocsConfig`

### `generate_docs(project_path, config)`

High-level function to generate all documentation.

**Calls:** `ProjectScanner`, `scanner.analyze`, `None.generate`, `None.generate`, `None.generate`, `Code2DocsConfig`, `None.generate_all`, `None.generate_all`, `None.generate`, `ReadmeGenerator`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 53 |
| Complexity (avg) | 5.0 |
| Functions | 1 |
| Classes | 0 |
| Fan-out | 15 |
