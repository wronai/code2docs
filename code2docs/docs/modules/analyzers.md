# analyzers

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/__init__.py` | 13 lines

## Overview

Analyzers — adapters to code2llm and custom detectors.

## Classes

### ProjectScanner

Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `__init__` | `self, config` | `—` | 2 |
| `_build_llm_config` | `self` | `—` | 1 |
| `analyze` | `self, project_path` | `—` | 1 |

### DocstringInfo

Parsed docstring with sections.

### DocstringExtractor

Extract and parse docstrings from AnalysisResult.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `extract_all` | `self, result` | `—` | 5 |
| `parse` | `self, docstring` | `—` | 2 |
| `_extract_summary` | `lines` | `—` | 2 |
| `_classify_section` | `line` | `—` | 5 |
| `_parse_sections` | `self, lines, info` | `—` | 8 |
| `_parse_param_line` | `info, line` | `—` | 2 |
| `_parse_returns_line` | `info, line` | `—` | 1 |
| `_parse_raises_line` | `info, line` | `—` | 1 |
| `_parse_examples_line` | `info, line` | `—` | 1 |
| `coverage_report` | `self, result` | `—` | 8 |

### DependencyInfo

Information about a project dependency.

### ProjectDependencies

All detected project dependencies.

### DependencyScanner

Scan and parse project dependency files.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `scan` | `self, project_path` | `—` | 4 |
| `_parse_pyproject` | `self, path` | `—` | 8 |
| `_parse_pyproject_regex` | `self, path` | `—` | 4 |
| `_parse_setup_py` | `self, path` | `—` | 4 |
| `_parse_requirements_txt` | `self, path` | `—` | 5 |
| `_parse_dep_string` | `dep_str` | `—` | 2 |

### Endpoint

Represents a detected web endpoint.

### EndpointDetector

Detects web endpoints from decorator patterns in source code.

#### Methods

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `detect` | `self, result, project_path` | `—` | 5 |
| `_parse_decorator` | `self, decorator, func` | `—` | 3 |
| `_scan_django_urls` | `self, project_path` | `—` | 4 |

## Functions

### `analyze_and_document(project_path, config)`

Convenience function: analyze a project in one call.

**Calls:** `ProjectScanner`, `scanner.analyze`

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 13 |
| Functions | 0 |
| Classes | 0 |
