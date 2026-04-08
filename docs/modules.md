# code2docs — Module Reference

> 55 modules | 298 functions | 60 classes

## Module Overview

| Module | Lines | Functions | Classes | CC avg | Description | Source |
|--------|-------|-----------|---------|--------|-------------|--------|
| `code2docs` | 24 | 1 | 0 | 4.0 | code2docs - Auto-generate and sync project documentation fro | [source](https://github.com/wronai/code2docs/blob/main/code2docs/__init__.py) |
| `code2docs.analyzers.dependency_scanner` | 248 | 0 | 3 | 6.0 | Scan project dependencies from requirements.txt, pyproject.t | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py) |
| `code2docs.analyzers.docstring_extractor` | 140 | 0 | 2 | 3.5 | Extract and analyze docstrings from source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py) |
| `code2docs.analyzers.endpoint_detector` | 113 | 0 | 2 | 4.0 | Detect web framework endpoints (Flask, FastAPI, Django) from | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py) |
| `code2docs.analyzers.project_scanner` | 42 | 1 | 1 | 1.2 | Wrapper around code2llm's ProjectAnalyzer for documentation  | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py) |
| `code2docs.base` | 46 | 0 | 2 | 1.0 | Base generator interface and generation context. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py) |
| `code2docs.cli` | 245 | 13 | 1 | 3.4 | CLI interface for code2docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py) |
| `code2docs.config` | 155 | 0 | 7 | 3.4 | Configuration for code2docs documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py) |
| `code2docs.formatters.badges` | 52 | 2 | 0 | 7.5 | Badge generation using shields.io URLs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py) |
| `code2docs.formatters.markdown` | 73 | 0 | 1 | 1.2 | Markdown formatting utilities. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py) |
| `code2docs.formatters.toc` | 63 | 3 | 0 | 3.3 | Table of contents generator from Markdown headings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py) |
| `code2docs.generators` | 59 | 1 | 0 | 5.0 | Documentation generators — produce Markdown, examples, and d | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py) |
| `code2docs.generators._registry_adapters` | 290 | 0 | 15 | 2.4 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py) |
| `code2docs.generators._source_links` | 76 | 0 | 1 | 3.0 | Helper for generating source code links in documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py) |
| `code2docs.generators.api_changelog_gen` | 196 | 0 | 2 | 5.4 | API changelog generator — diff function/class signatures bet | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py) |
| `code2docs.generators.api_reference_gen` | 163 | 0 | 1 | 8.7 | API reference documentation generator — single consolidated  | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py) |
| `code2docs.generators.architecture_gen` | 294 | 0 | 1 | 6.9 | Architecture documentation generator with Mermaid diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py) |
| `code2docs.generators.changelog_gen` | 121 | 0 | 2 | 3.5 | Changelog generator from git log and API diff. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py) |
| `code2docs.generators.code2llm_gen` | 206 | 2 | 1 | 7.0 | code2llm integration generator — produces analysis files in  | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py) |
| `code2docs.generators.config_docs_gen` | 125 | 0 | 1 | 4.2 | Configuration documentation generator. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py) |
| `code2docs.generators.contributing_gen` | 231 | 0 | 1 | 4.6 | CONTRIBUTING.md generator from project tooling detection. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py) |
| `code2docs.generators.coverage_gen` | 104 | 0 | 1 | 4.4 | Docstring coverage report generator. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py) |
| `code2docs.generators.depgraph_gen` | 140 | 0 | 1 | 3.9 | Dependency graph generator — Mermaid diagram from coupling m | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py) |
| `code2docs.generators.examples_gen` | 456 | 0 | 1 | 6.1 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py) |
| `code2docs.generators.getting_started_gen` | 196 | 0 | 1 | 7.1 | Getting Started guide generator. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py) |
| `code2docs.generators.mkdocs_gen` | 110 | 0 | 1 | 3.2 | MkDocs configuration generator — auto-generate mkdocs.yml fr | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py) |
| `code2docs.generators.module_docs_gen` | 198 | 0 | 1 | 8.0 | Module documentation generator — single consolidated modules | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py) |
| `code2docs.generators.org_readme_gen` | 227 | 0 | 1 | 5.2 | Organization README generator - generates overview of multip | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/org_readme_gen.py) |
| `code2docs.generators.readme_gen` | 322 | 1 | 1 | 6.0 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py) |
| `code2docs.llm_helper` | 161 | 1 | 1 | 2.3 | LLM helper — optional LLM-assisted documentation generation  | [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py) |
| `code2docs.registry` | 35 | 0 | 1 | 2.5 | Generator registry — pluggable generator system. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py) |
| `code2docs.sync.differ` | 125 | 0 | 2 | 3.6 | Detect changes in source code for selective documentation re | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py) |
| `code2docs.sync.updater` | 51 | 0 | 1 | 3.0 | Selectively regenerate documentation for changed modules. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py) |
| `code2docs.sync.watcher` | 75 | 1 | 0 | 5.0 | File watcher for auto-resync on source changes (requires wat | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py) |
| `examples.01_cli_usage` | 70 | 2 | 0 | 1.0 | Example 1: CLI Usage - Generate documentation from command l | [source](https://github.com/wronai/code2docs/blob/main/examples/01_cli_usage.py) |
| `examples.02_configuration` | 161 | 4 | 0 | 1.0 | Example 2: Configuration - Set up code2docs with custom sett | [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py) |
| `examples.03_programmatic_api` | 85 | 5 | 0 | 2.4 | Example 3: Programmatic API - Use code2docs in your Python c | [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py) |
| `examples.04_sync_and_watch` | 120 | 6 | 0 | 2.2 | — | [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py) |
| `examples.05_custom_generators` | 144 | 1 | 3 | 2.2 | Example 5: Custom Generators - Build your own documentation  | [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py) |
| `examples.06_formatters` | 96 | 5 | 0 | 1.6 | Example 6: Formatters and Utilities - Working with markdown  | [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py) |
| `examples.07_web_frameworks` | 221 | 5 | 0 | 4.2 | Example 7: Web Framework Integration - Document Flask/FastAP | [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py) |

## code2docs

### `code2docs.analyzers.dependency_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py)

Scan project dependencies from requirements.txt, pyproject.toml, setup.py, package.json, Cargo.toml, go.mod.

**`DependencyInfo`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L15)
: Information about a project dependency.

**`DependencyScanner`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L38)
: Scan and parse project dependency files.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `scan` | `project_path` | `—` | 8 |

**`ProjectDependencies`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L23)
: All detected project dependencies.

### `code2docs.analyzers.docstring_extractor` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py)

Extract and analyze docstrings from source code.

**`DocstringExtractor`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L23)
: Extract and parse docstrings from AnalysisResult.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `extract_all` | `result` | `—` | 5 |
| `parse` | `docstring` | `—` | 2 |
| `coverage_report` | `result` | `—` | 8 |

**`DocstringInfo`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L12)
: Parsed docstring with sections.

### `code2docs.analyzers.endpoint_detector` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py)

Detect web framework endpoints (Flask, FastAPI, Django) from AST analysis.

**`Endpoint`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L13)
: Represents a detected web endpoint.

**`EndpointDetector`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L26)
: Detects web endpoints from decorator patterns in source code.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `detect` | `result, project_path` | `—` | 5 |

### `code2docs.analyzers.project_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py)

Wrapper around code2llm's ProjectAnalyzer for documentation purposes.

**`ProjectScanner`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L11)
: Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `analyze` | `project_path` | `—` | 1 |

- `analyze_and_document(project_path, config)` — Convenience function: analyze a project in one call. [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L39)

### `code2docs.base` [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py)

Base generator interface and generation context.

**`BaseGenerator`** (ABC) [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L22)
: Abstract base for all documentation generators.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 1 |

**`GenerateContext`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L14)
: Shared context passed to all generators during a run.

### `code2docs.cli` [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py)

CLI interface for code2docs.

**`DefaultGroup`** (click.Group) [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L13)
: Click Group that routes unknown subcommands to 'generate'.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `parse_args` | `ctx, args` | `—` | 4 |

- `check(project_path, config_path, target)` — Health check — verify documentation completeness. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L91)
- `diff(project_path, config_path)` — Preview what would change without writing anything. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L99)
- `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run, llm_model, org_name)` — Generate documentation (default command). [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L37)
- `init(project_path, output)` — Initialize code2docs.yaml configuration file. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L79)
- `main()` — code2docs — Auto-generate project documentation from source code. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L24)
- `sync(project_path, config_path, verbose, dry_run)` — Synchronize documentation with source code changes. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L58)
- `watch(project_path, config_path, verbose)` — Watch for file changes and auto-regenerate docs. [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L69)

### `code2docs.config` [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py)

Configuration for code2docs documentation generation.

**`Code2DocsConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L76)
: Main configuration for code2docs.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `from_yaml` | `cls, path` | `—` | 10 |
| `to_yaml` | `path` | `—` | 1 |

**`Code2LlmConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L43)
: Configuration for code2llm analysis generation.

**`DocsConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L22)
: Configuration for docs/ generation.

**`ExamplesConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L30)
: Configuration for examples/ generation.

**`LLMConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L55)
: Configuration for optional LLM-assisted documentation generation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `from_env` | `cls` | `—` | 1 |

**`ReadmeConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L15)
: Configuration for README generation.

**`SyncConfig`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L36)
: Configuration for synchronization.

### `code2docs.formatters.badges` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py)

Badge generation using shields.io URLs.

- `generate_badges(project_name, badge_types, stats, deps)` — Generate shields.io badge Markdown strings. [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py#L7)

### `code2docs.formatters.markdown` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py)

Markdown formatting utilities.

**`MarkdownFormatter`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py#L6)
: Helper for constructing Markdown documents.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `heading` | `text, level` | `—` | 1 |
| `paragraph` | `text` | `—` | 1 |
| `blockquote` | `text` | `—` | 1 |
| `code_block` | `code, language` | `—` | 1 |
| `inline_code` | `text` | `—` | 1 |
| `bold` | `text` | `—` | 1 |
| `link` | `text, url` | `—` | 1 |
| `list_item` | `text, indent` | `—` | 1 |
| `table` | `headers, rows` | `—` | 4 |
| `separator` | `` | `—` | 1 |
| `blank` | `` | `—` | 1 |
| `render` | `` | `—` | 1 |

### `code2docs.formatters.toc` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py)

Table of contents generator from Markdown headings.

- `extract_headings(content, max_depth)` — Extract headings from Markdown content. [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L30)
- `generate_toc(markdown_content, max_depth)` — Generate a table of contents from Markdown headings. [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L7)

### `code2docs.generators` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py)

Documentation generators — produce Markdown, examples, and diagrams.

- `generate_docs(project_path, config)` — High-level function to generate all documentation. [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py#L35)

### `code2docs.generators._registry_adapters` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py)

**`ApiChangelogAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L111)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ApiReferenceAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L34)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`ArchitectureAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L66)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`Code2LlmAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L206)
: Adapter for code2llm analysis generation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 7 |

**`ConfigDocsAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L174)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ContributingAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L190)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`CoverageAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L96)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`DepGraphAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L81)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ExamplesAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L127)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`GettingStartedAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L158)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`IndexHtmlAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L247)
: Adapter for generating index.html for GitHub Pages browsing.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`MkDocsAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L143)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 2 |

**`ModuleDocsAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L50)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 2 |

**`OrgReadmeAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L224)
: Adapter for organization README generation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 2 |
| `run` | `ctx` | `—` | 4 |

**`ReadmeGeneratorAdapter`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L11)

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `should_run` | `` | `—` | 1 |
| `run` | `ctx` | `—` | 4 |

### `code2docs.generators._source_links` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py)

Helper for generating source code links in documentation.

**`SourceLinker`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py#L11)
: Build source-code links (relative paths + optional GitHub/GitLab URLs).

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `source_link` | `file, line` | `—` | 5 |
| `file_link` | `file` | `—` | 1 |

### `code2docs.generators.api_changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py)

API changelog generator — diff function/class signatures between versions.

**`ApiChange`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L16)
: A single API change between two analysis snapshots.

**`ApiChangelogGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L30)
: Generate API changelog by diffing current analysis with a saved snapshot.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `project_path` | `—` | 2 |
| `save_snapshot` | `project_path` | `—` | 1 |

### `code2docs.generators.api_reference_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py)

API reference documentation generator — single consolidated api.md.

**`ApiReferenceGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py#L13)
: Generate docs/api.md — consolidated API reference.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 11 |

### `code2docs.generators.architecture_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py)

Architecture documentation generator with Mermaid diagrams.

**`ArchitectureGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py#L12)
: Generate docs/architecture.md — architecture overview with diagrams.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 13 |

### `code2docs.generators.changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py)

Changelog generator from git log and API diff.

**`ChangelogEntry`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L14)
: A single changelog entry.

**`ChangelogGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L23)
: Generate CHANGELOG.md from git log and analysis diff.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `project_path, max_entries` | `—` | 3 |

### `code2docs.generators.code2llm_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py)

code2llm integration generator — produces analysis files in project/ folder.

**`Code2LlmGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L62)
: Generate code2llm analysis files in project/ directory.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate_all` | `` | `—` | 5 |
| `get_analysis_summary` | `` | `—` | 2 |

- `generate_code2llm_analysis(project_path, config)` — Convenience function to generate code2llm analysis. [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L188)
- `parse_gitignore(project_path)` — Parse .gitignore file and return list of patterns to exclude. [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L12)

### `code2docs.generators.config_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py)

Configuration documentation generator.

**`ConfigDocsGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py#L11)
: Generate docs/configuration.md from Code2DocsConfig dataclass.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 4 |

### `code2docs.generators.contributing_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py)

CONTRIBUTING.md generator from project tooling detection.

**`ContributingGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py#L11)
: Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 2 |

### `code2docs.generators.coverage_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py)

Docstring coverage report generator.

**`CoverageGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py#L11)
: Generate docs/coverage.md — docstring coverage report.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 2 |

### `code2docs.generators.depgraph_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py)

Dependency graph generator — Mermaid diagram from coupling matrix.

**`DepGraphGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py#L12)
: Generate docs/dependency-graph.md with Mermaid diagrams.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 2 |

### `code2docs.generators.examples_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py)

**`ExamplesGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py#L66)
: Generate examples/ — usage examples from public API signatures.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate_all` | `` | `—` | 1 |
| `write_all` | `output_dir, files` | `—` | 2 |

### `code2docs.generators.getting_started_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py)

Getting Started guide generator.

**`GettingStartedGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py#L12)
: Generate docs/getting-started.md from entry points and dependencies.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 3 |

### `code2docs.generators.mkdocs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py)

MkDocs configuration generator — auto-generate mkdocs.yml from docs tree.

**`MkDocsGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py#L13)
: Generate mkdocs.yml from the docs/ directory structure.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `docs_dir` | `—` | 4 |
| `write` | `output_path, content` | `—` | 1 |

### `code2docs.generators.module_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py)

Module documentation generator — single consolidated modules.md.

**`ModuleDocsGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py#L14)
: Generate docs/modules.md — consolidated module documentation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 18 |

### `code2docs.generators.org_readme_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/org_readme_gen.py)

Organization README generator - generates overview of multiple projects.

**`OrgReadmeGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/org_readme_gen.py#L12)
: Generate organization README with list of projects and brief descriptions.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 2 |
| `write` | `output_path, content` | `—` | 1 |

### `code2docs.generators.readme_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py)

**`ReadmeGenerator`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L24)
: Generate README.md from AnalysisResult.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 3 |
| `write` | `path, content` | `—` | 4 |

- `generate_readme(project_path, output, sections, sync_markers, config)` — Convenience function to generate a README. [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L310)

### `code2docs.llm_helper` [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py)

LLM helper — optional LLM-assisted documentation generation via litellm.

**`LLMHelper`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py#L31)
: Thin wrapper around litellm for documentation generation.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `complete` | `prompt, system` | `—` | 7 |
| `generate_project_description` | `project_name, modules_summary, entry_points` | `—` | 1 |
| `generate_architecture_summary` | `project_name, layers, patterns` | `—` | 1 |
| `generate_getting_started_summary` | `project_name, cli_commands, public_api` | `—` | 1 |
| `enhance_module_docstring` | `module_name, functions, classes` | `—` | 1 |

### `code2docs.registry` [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py)

Generator registry — pluggable generator system.

**`GeneratorRegistry`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py#L6)
: Registry of documentation generators.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `add` | `generator` | `—` | 1 |
| `run_all` | `ctx` | `—` | 4 |
| `run_only` | `name, ctx` | `—` | 4 |

### `code2docs.sync.differ` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py)

Detect changes in source code for selective documentation regeneration.

**`ChangeInfo`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L15)
: Describes a detected change.

**`Differ`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L27)
: Detect changes between current source and previous state.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `detect_changes` | `project_path` | `—` | 6 |
| `save_state` | `project_path` | `—` | 1 |

### `code2docs.sync.updater` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py)

Selectively regenerate documentation for changed modules.

**`Updater`** [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py#L10)
: Apply selective documentation updates based on detected changes.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `apply` | `project_path, changes` | `—` | 4 |

### `code2docs.sync.watcher` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py)

File watcher for auto-resync on source changes (requires watchdog).

- `start_watcher(project_path, config)` — Start watching project for file changes and auto-resync docs. [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py#L10)

## examples

### `examples.01_cli_usage` [source](https://github.com/wronai/code2docs/blob/main/examples/01_cli_usage.py)

Example 1: CLI Usage - Generate documentation from command line.

- `run_cli_basic(project_path)` — Run code2docs CLI programmatically. [source](https://github.com/wronai/code2docs/blob/main/examples/01_cli_usage.py#L47)
- `run_cli_with_config(project_path, config_path)` — Run with custom configuration. [source](https://github.com/wronai/code2docs/blob/main/examples/01_cli_usage.py#L58)

### `examples.02_configuration` [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py)

Example 2: Configuration - Set up code2docs with custom settings.

- `create_advanced_config()` — Create advanced configuration with all options. [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L34)
- `create_basic_config()` — Create a basic configuration. [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L16)
- `load_config_from_yaml(path)` — Load configuration from YAML file. [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L142)
- `save_yaml_config_example(path)` — Save example YAML config to file. [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L136)

### `examples.03_programmatic_api` [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py)

Example 3: Programmatic API - Use code2docs in your Python code.

- `custom_documentation_pipeline(project_path)` — Create a custom documentation pipeline. [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L34)
- `generate_docs_if_needed(project_path, force)` — Only generate docs if code has changed. [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L68)
- `generate_full_documentation(project_path)` — Generate complete documentation for a project. [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L19)
- `generate_readme_simple(project_path)` — Generate README.md content from a project. [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L12)
- `inspect_project_structure(project_path)` — Inspect project structure from analysis. [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L50)

### `examples.04_sync_and_watch` [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py)

- `custom_watcher_with_hooks(project_path)` — Set up a custom watcher with pre/post generation hooks. [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L69)
- `detect_changes_example(project_path)` — Detect what files have changed since last documentation generation. [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L15)
- `force_full_regeneration(project_path)` — Force full regeneration of all documentation. [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L45)
- `sync_with_git_changes(project_path)` — Only regenerate docs for files changed in git. [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L105)
- `update_docs_incrementally(project_path)` — Update only the parts of docs that need changing. [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L33)
- `watch_and_auto_regenerate(project_path, interval)` — Watch for file changes and auto-regenerate documentation. [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L54)

### `examples.05_custom_generators` [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py)

Example 5: Custom Generators - Build your own documentation generator.

**`APIChangelogGenerator`** [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L69)
: Generate changelog based on API changes.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `previous_result` | `—` | 8 |

**`CustomGenerator`** (BaseGenerator) [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L132)
: Example of extending the base generator class.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 1 |
| `write` | `path, content` | `—` | 1 |

**`MetricsReportGenerator`** [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L11)
: Generate a metrics report from code analysis.

| Method | Args | Returns | CC |
|--------|------|---------|----|
| `generate` | `` | `—` | 1 |

- `generate_custom_report(project_path)` — Generate a custom metrics report. [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L119)

### `examples.06_formatters` [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py)

Example 6: Formatters and Utilities - Working with markdown formatting.

- `badge_examples()` — Generate various badge examples. [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L53)
- `build_custom_readme()` — Build a custom README using formatters. [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L71)
- `generate_complex_document()` — Generate a complex markdown document using the formatter. [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L30)
- `markdown_formatting_examples()` — Demonstrate markdown formatting utilities. [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L10)
- `toc_examples()` — Demonstrate table of contents generation. [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L60)

### `examples.07_web_frameworks` [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py)

Example 7: Web Framework Integration - Document Flask/FastAPI endpoints.

- `create_example_web_apps(target_dir)` — Create example Flask and FastAPI apps for testing. [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L157)
- `detect_fastapi_endpoints(project_path)` — Detect FastAPI endpoints in a project. [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L33)
- `detect_flask_endpoints(project_path)` — Detect Flask endpoints in a project. [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L16)
- `document_web_project(project_path)` — Complete workflow: detect endpoints and generate docs. [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L177)
- `generate_api_docs_from_endpoints(project_path, output_dir)` — Generate API documentation from detected endpoints. [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L55)
