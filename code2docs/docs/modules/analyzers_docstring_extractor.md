# analyzers.docstring_extractor

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/docstring_extractor.py` | 140 lines | CC avg: 3.5

## Overview

Extract and analyze docstrings from source code.

## Classes

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

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 140 |
| Complexity (avg) | 3.5 |
| Functions | 10 |
| Classes | 2 |
| Fan-out | 36 |
