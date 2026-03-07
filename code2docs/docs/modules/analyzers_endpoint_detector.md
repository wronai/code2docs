# analyzers.endpoint_detector

> Source: `/home/tom/github/wronai/code2docs/code2docs/analyzers/endpoint_detector.py` | 113 lines | CC avg: 4.0

## Overview

Detect web framework endpoints (Flask, FastAPI, Django) from AST analysis.

## Classes

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

## Metrics

| Metric | Value |
|--------|-------|
| Lines | 113 |
| Complexity (avg) | 4.0 |
| Functions | 3 |
| Classes | 2 |
| Fan-out | 23 |
