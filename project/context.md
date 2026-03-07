# System Architecture Analysis

## Overview

- **Project**: /home/tom/github/wronai/code2docs
- **Analysis Mode**: static
- **Total Functions**: 54
- **Total Classes**: 16
- **Modules**: 13
- **Entry Points**: 50

## Architecture by Module

### code2docs.generators.module_docs_gen
- **Functions**: 11
- **Classes**: 1
- **File**: `module_docs_gen.py`

### code2docs.generators.readme_gen
- **Functions**: 8
- **Classes**: 1
- **File**: `readme_gen.py`

### code2docs.cli
- **Functions**: 8
- **File**: `cli.py`

### code2docs.generators.api_reference_gen
- **Functions**: 7
- **Classes**: 1
- **File**: `api_reference_gen.py`

### code2docs.analyzers.dependency_scanner
- **Functions**: 6
- **Classes**: 3
- **File**: `dependency_scanner.py`

### code2docs.analyzers.project_scanner
- **Functions**: 4
- **Classes**: 1
- **File**: `project_scanner.py`

### code2docs.analyzers.endpoint_detector
- **Functions**: 3
- **Classes**: 2
- **File**: `endpoint_detector.py`

### code2docs.analyzers.docstring_extractor
- **Functions**: 3
- **Classes**: 2
- **File**: `docstring_extractor.py`

### code2docs.config
- **Functions**: 2
- **Classes**: 5
- **File**: `config.py`

### code2docs
- **Functions**: 1
- **File**: `__init__.py`

### code2docs.generators
- **Functions**: 1
- **File**: `__init__.py`

## Key Entry Points

Main execution flows into the system:

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._generate_module
> Generate detailed documentation for a single module.
- **Calls**: lines.append, self._count_file_lines, self._calc_module_avg_cc, lines.append, self._get_module_docstring, self._get_module_classes, self._get_module_functions, self._get_module_metrics

### code2docs.generators.readme_gen.ReadmeGenerator._build_manual
> Fallback manual README builder.
- **Calls**: context.get, context.get, None.join, parts.append, parts.append, context.get, context.get, context.get

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._generate_module_api
> Generate API reference for a single module.
- **Calls**: lines.append, None.join, lines.append, sorted, lines.append, sorted, lines.append, sorted

### code2docs.config.Code2DocsConfig.from_yaml
> Load configuration from code2docs.yaml.
- **Calls**: Path, cls, data.get, project.get, project.get, project.get, project.get, project.get

### code2docs.analyzers.docstring_extractor.DocstringExtractor.parse
> Parse a docstring into structured sections.
- **Calls**: None.splitlines, DocstringInfo, None.strip, DocstringInfo, None.strip, line.strip, stripped.lower, lower.startswith

### code2docs.cli.main
> code2docs — Auto-generate project documentation from source code.

Analyzes PROJECT_PATH using code2llm and generates human-readable documentation.
- **Calls**: click.group, click.argument, click.option, click.option, click.option, click.option, click.option, click.option

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_module_metrics
- **Calls**: self._count_file_lines, self._calc_module_avg_cc, str, str, self.result.functions.values, str, str, len

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject
> Parse pyproject.toml for dependencies.
- **Calls**: ProjectDependencies, data.get, project.get, project.get, None.items, project.get, self._parse_pyproject_regex, open

### code2docs.generators.generate_docs
> High-level function to generate all documentation.
- **Calls**: ProjectScanner, scanner.analyze, None.generate, Code2DocsConfig, None.generate_all, None.generate_all, None.generate, ReadmeGenerator

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._generate_index
> Generate API index page.
- **Calls**: sorted, self.result.modules.keys, None.replace, len, len, lines.append, None.join, len

### code2docs.cli.init
> Initialize code2docs.yaml configuration file.
- **Calls**: main.command, click.argument, click.option, None.resolve, Code2DocsConfig, config.to_yaml, click.echo, str

### code2docs.analyzers.endpoint_detector.EndpointDetector._parse_decorator
> Try to parse a route decorator string.
- **Calls**: self.FLASK_PATTERNS.search, self.FASTAPI_PATTERNS.search, None.upper, Endpoint, Endpoint, match.group, match.group, None.upper

### code2docs.analyzers.endpoint_detector.EndpointDetector._scan_django_urls
> Scan urls.py files for Django URL patterns.
- **Calls**: Path, project.rglob, urls_file.read_text, self.DJANGO_URL_PATTERN.finditer, endpoints.append, Endpoint, match.group, str

### code2docs.generators.readme_gen.ReadmeGenerator._build_context
> Build template context from analysis result.
- **Calls**: DependencyScanner, dep_scanner.scan, EndpointDetector, endpoint_detector.detect, self._calc_avg_complexity, self._build_module_tree, generate_badges, self.result.functions.items

### code2docs.generators.readme_gen.ReadmeGenerator._build_module_tree
> Build text-based module tree.
- **Calls**: sorted, None.join, self.result.modules.keys, len, len, lines.append, detail.append, detail.append

### code2docs.generators.readme_gen.ReadmeGenerator.write
> Write README, respecting sync markers if existing file has them.
- **Calls**: Path, readme_path.exists, readme_path.parent.mkdir, readme_path.write_text, readme_path.read_text, re.compile, pattern.sub, re.escape

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex
> Fallback regex-based pyproject.toml parser.
- **Calls**: ProjectDependencies, path.read_text, re.search, re.search, re.findall, py_match.group, dep_match.group, deps.dependencies.append

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_setup_py
> Parse setup.py for dependencies (regex-based, no exec).
- **Calls**: ProjectDependencies, path.read_text, re.search, re.search, re.findall, py_match.group, match.group, deps.dependencies.append

### code2docs.cli.sync
> Synchronize documentation with source code changes.
- **Calls**: main.command, click.argument, click.option, click.option, click.option, code2docs.cli._load_config, code2docs.cli._run_sync, click.Path

### code2docs.analyzers.dependency_scanner.DependencyScanner.scan
> Scan project for dependency information.
- **Calls**: Path, ProjectDependencies, pyproject.exists, setup_py.exists, req_txt.exists, self._parse_pyproject, self._parse_setup_py, self._parse_requirements_txt

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt
> Parse requirements.txt.
- **Calls**: ProjectDependencies, None.splitlines, line.strip, deps.dependencies.append, path.read_text, line.startswith, line.startswith, self._parse_dep_string

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_dep_string
> Parse a dependency string like 'package>=1.0'.
- **Calls**: re.match, DependencyInfo, dep_str.strip, DependencyInfo, dep_str.strip, match.group, None.strip, match.group

### code2docs.cli.watch
> Watch for file changes and auto-regenerate docs.
- **Calls**: main.command, click.argument, click.option, click.option, code2docs.cli._load_config, code2docs.cli._run_watch, click.Path

### code2docs.generators.readme_gen.ReadmeGenerator._calc_avg_complexity
> Calculate average cyclomatic complexity.
- **Calls**: self.result.functions.values, func.complexity.get, round, complexities.append, sum, len

### code2docs.generators.readme_gen.generate_readme
> Convenience function to generate a README.
- **Calls**: ProjectScanner, scanner.analyze, ReadmeGenerator, gen.generate, gen.write, Code2DocsConfig

### code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate_all
> Generate API reference for all modules. Returns {filename: content}.
- **Calls**: self._generate_index, sorted, self.result.modules.items, None.replace, self._generate_module_api, mod_name.replace

### code2docs.generators.module_docs_gen.ModuleDocsGenerator._calc_module_avg_cc
> Calculate average cyclomatic complexity for module functions.
- **Calls**: self.result.functions.values, round, func.complexity.get, complexities.append, sum, len

### code2docs.analyzers.docstring_extractor.DocstringExtractor.coverage_report
> Calculate docstring coverage statistics.
- **Calls**: len, len, sum, sum, result.functions.values, result.classes.values

### code2docs.generators.readme_gen.ReadmeGenerator.generate
> Generate full README content.
- **Calls**: self._build_context, self.env.get_template, template.render, Path, self._build_manual

### code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate_all
> Generate documentation for all modules. Returns {filename: content}.
- **Calls**: sorted, self.result.modules.items, None.replace, self._generate_module, mod_name.replace

## Process Flows

Key execution flows identified:

### Flow 1: _generate_module
```
_generate_module [code2docs.generators.module_docs_gen.ModuleDocsGenerator]
```

### Flow 2: _build_manual
```
_build_manual [code2docs.generators.readme_gen.ReadmeGenerator]
```

### Flow 3: _generate_module_api
```
_generate_module_api [code2docs.generators.api_reference_gen.ApiReferenceGenerator]
```

### Flow 4: from_yaml
```
from_yaml [code2docs.config.Code2DocsConfig]
```

### Flow 5: parse
```
parse [code2docs.analyzers.docstring_extractor.DocstringExtractor]
```

### Flow 6: main
```
main [code2docs.cli]
```

### Flow 7: _get_module_metrics
```
_get_module_metrics [code2docs.generators.module_docs_gen.ModuleDocsGenerator]
```

### Flow 8: _parse_pyproject
```
_parse_pyproject [code2docs.analyzers.dependency_scanner.DependencyScanner]
```

### Flow 9: generate_docs
```
generate_docs [code2docs.generators]
```

### Flow 10: _generate_index
```
_generate_index [code2docs.generators.api_reference_gen.ApiReferenceGenerator]
```

## Key Classes

### code2docs.generators.module_docs_gen.ModuleDocsGenerator
> Generate docs/modules/ — detailed per-module documentation.
- **Methods**: 11
- **Key Methods**: code2docs.generators.module_docs_gen.ModuleDocsGenerator.__init__, code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate_all, code2docs.generators.module_docs_gen.ModuleDocsGenerator._generate_module, code2docs.generators.module_docs_gen.ModuleDocsGenerator._count_file_lines, code2docs.generators.module_docs_gen.ModuleDocsGenerator._calc_module_avg_cc, code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_module_docstring, code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_module_classes, code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_module_functions, code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_class_methods, code2docs.generators.module_docs_gen.ModuleDocsGenerator._get_module_metrics

### code2docs.generators.readme_gen.ReadmeGenerator
> Generate README.md from AnalysisResult.
- **Methods**: 7
- **Key Methods**: code2docs.generators.readme_gen.ReadmeGenerator.__init__, code2docs.generators.readme_gen.ReadmeGenerator.generate, code2docs.generators.readme_gen.ReadmeGenerator._build_context, code2docs.generators.readme_gen.ReadmeGenerator._calc_avg_complexity, code2docs.generators.readme_gen.ReadmeGenerator._build_module_tree, code2docs.generators.readme_gen.ReadmeGenerator._build_manual, code2docs.generators.readme_gen.ReadmeGenerator.write

### code2docs.generators.api_reference_gen.ApiReferenceGenerator
> Generate docs/api/ — per-module API reference from signatures.
- **Methods**: 7
- **Key Methods**: code2docs.generators.api_reference_gen.ApiReferenceGenerator.__init__, code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate_all, code2docs.generators.api_reference_gen.ApiReferenceGenerator._generate_index, code2docs.generators.api_reference_gen.ApiReferenceGenerator._generate_module_api, code2docs.generators.api_reference_gen.ApiReferenceGenerator._get_class_methods, code2docs.generators.api_reference_gen.ApiReferenceGenerator._format_signature, code2docs.generators.api_reference_gen.ApiReferenceGenerator.write_all

### code2docs.analyzers.dependency_scanner.DependencyScanner
> Scan and parse project dependency files.
- **Methods**: 6
- **Key Methods**: code2docs.analyzers.dependency_scanner.DependencyScanner.scan, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_setup_py, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_dep_string

### code2docs.analyzers.endpoint_detector.EndpointDetector
> Detects web endpoints from decorator patterns in source code.
- **Methods**: 3
- **Key Methods**: code2docs.analyzers.endpoint_detector.EndpointDetector.detect, code2docs.analyzers.endpoint_detector.EndpointDetector._parse_decorator, code2docs.analyzers.endpoint_detector.EndpointDetector._scan_django_urls

### code2docs.analyzers.docstring_extractor.DocstringExtractor
> Extract and parse docstrings from AnalysisResult.
- **Methods**: 3
- **Key Methods**: code2docs.analyzers.docstring_extractor.DocstringExtractor.extract_all, code2docs.analyzers.docstring_extractor.DocstringExtractor.parse, code2docs.analyzers.docstring_extractor.DocstringExtractor.coverage_report

### code2docs.analyzers.project_scanner.ProjectScanner
> Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.
- **Methods**: 3
- **Key Methods**: code2docs.analyzers.project_scanner.ProjectScanner.__init__, code2docs.analyzers.project_scanner.ProjectScanner._build_llm_config, code2docs.analyzers.project_scanner.ProjectScanner.analyze

### code2docs.config.Code2DocsConfig
> Main configuration for code2docs.
- **Methods**: 2
- **Key Methods**: code2docs.config.Code2DocsConfig.from_yaml, code2docs.config.Code2DocsConfig.to_yaml

### code2docs.config.ReadmeConfig
> Configuration for README generation.
- **Methods**: 0

### code2docs.config.DocsConfig
> Configuration for docs/ generation.
- **Methods**: 0

### code2docs.config.ExamplesConfig
> Configuration for examples/ generation.
- **Methods**: 0

### code2docs.config.SyncConfig
> Configuration for synchronization.
- **Methods**: 0

### code2docs.analyzers.endpoint_detector.Endpoint
> Represents a detected web endpoint.
- **Methods**: 0

### code2docs.analyzers.docstring_extractor.DocstringInfo
> Parsed docstring with sections.
- **Methods**: 0

### code2docs.analyzers.dependency_scanner.DependencyInfo
> Information about a project dependency.
- **Methods**: 0

### code2docs.analyzers.dependency_scanner.ProjectDependencies
> All detected project dependencies.
- **Methods**: 0

## Data Transformation Functions

Key functions that process and transform data:

### code2docs.generators.api_reference_gen.ApiReferenceGenerator._format_signature
> Format a function signature string.
- **Output to**: None.join

### code2docs.analyzers.endpoint_detector.EndpointDetector._parse_decorator
> Try to parse a route decorator string.
- **Output to**: self.FLASK_PATTERNS.search, self.FASTAPI_PATTERNS.search, None.upper, Endpoint, Endpoint

### code2docs.analyzers.docstring_extractor.DocstringExtractor.parse
> Parse a docstring into structured sections.
- **Output to**: None.splitlines, DocstringInfo, None.strip, DocstringInfo, None.strip

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject
> Parse pyproject.toml for dependencies.
- **Output to**: ProjectDependencies, data.get, project.get, project.get, None.items

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex
> Fallback regex-based pyproject.toml parser.
- **Output to**: ProjectDependencies, path.read_text, re.search, re.search, re.findall

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_setup_py
> Parse setup.py for dependencies (regex-based, no exec).
- **Output to**: ProjectDependencies, path.read_text, re.search, re.search, re.findall

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt
> Parse requirements.txt.
- **Output to**: ProjectDependencies, None.splitlines, line.strip, deps.dependencies.append, path.read_text

### code2docs.analyzers.dependency_scanner.DependencyScanner._parse_dep_string
> Parse a dependency string like 'package>=1.0'.
- **Output to**: re.match, DependencyInfo, dep_str.strip, DependencyInfo, dep_str.strip

## Public API Surface

Functions exposed as public API (no underscore prefix):

- `code2docs.config.Code2DocsConfig.from_yaml` - 34 calls
- `code2docs.analyzers.docstring_extractor.DocstringExtractor.parse` - 21 calls
- `code2docs.cli.main` - 14 calls
- `code2docs.generators.generate_docs` - 11 calls
- `code2docs.cli.init` - 10 calls
- `code2docs.generators.readme_gen.ReadmeGenerator.write` - 9 calls
- `code2docs.cli.sync` - 8 calls
- `code2docs.analyzers.dependency_scanner.DependencyScanner.scan` - 8 calls
- `code2docs.cli.watch` - 7 calls
- `code2docs.generators.readme_gen.generate_readme` - 6 calls
- `code2docs.generators.api_reference_gen.ApiReferenceGenerator.generate_all` - 6 calls
- `code2docs.analyzers.docstring_extractor.DocstringExtractor.coverage_report` - 6 calls
- `code2docs.generators.readme_gen.ReadmeGenerator.generate` - 5 calls
- `code2docs.generators.module_docs_gen.ModuleDocsGenerator.generate_all` - 5 calls
- `code2docs.analyzers.endpoint_detector.EndpointDetector.detect` - 5 calls
- `code2docs.generators.api_reference_gen.ApiReferenceGenerator.write_all` - 4 calls
- `code2docs.generators.module_docs_gen.ModuleDocsGenerator.write_all` - 4 calls
- `code2docs.analyzers.docstring_extractor.DocstringExtractor.extract_all` - 4 calls
- `code2docs.config.Code2DocsConfig.to_yaml` - 2 calls
- `code2docs.analyzers.project_scanner.ProjectScanner.analyze` - 2 calls
- `code2docs.analyzers.project_scanner.analyze_and_document` - 2 calls

## System Interactions

How components interact:

```mermaid
graph TD
    _generate_module --> append
    _generate_module --> _count_file_lines
    _generate_module --> _calc_module_avg_cc
    _generate_module --> _get_module_docstrin
    _build_manual --> get
    _build_manual --> join
    _build_manual --> append
    _generate_module_api --> append
    _generate_module_api --> join
    _generate_module_api --> sorted
    from_yaml --> Path
    from_yaml --> cls
    from_yaml --> get
    parse --> splitlines
    parse --> DocstringInfo
    parse --> strip
    main --> group
    main --> argument
    main --> option
    _get_module_metrics --> _count_file_lines
    _get_module_metrics --> _calc_module_avg_cc
    _get_module_metrics --> str
    _get_module_metrics --> values
    _parse_pyproject --> ProjectDependencies
    _parse_pyproject --> get
    _parse_pyproject --> items
    generate_docs --> ProjectScanner
    generate_docs --> analyze
    generate_docs --> generate
    generate_docs --> Code2DocsConfig
```

## Reverse Engineering Guidelines

1. **Entry Points**: Start analysis from the entry points listed above
2. **Core Logic**: Focus on classes with many methods
3. **Data Flow**: Follow data transformation functions
4. **Process Flows**: Use the flow diagrams for execution paths
5. **API Surface**: Public API functions reveal the interface

## Context for LLM

Maintain the identified architectural patterns and public API surface when suggesting changes.