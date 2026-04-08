# code2docs — API Reference

> 55 modules | 298 functions | 60 classes

## Contents

- [Core](#core) (1 modules)
- [code2docs](#code2docs) (36 modules)
- [examples](#examples) (7 modules)

## Core

### `code2docs` [source](https://github.com/wronai/code2docs/blob/main/code2docs/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DependencyInfo` | 0 | Information about a project dependency. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L15) |
| `DependencyScanner` | 1 | Scan and parse project dependency files. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L38) |
| `ProjectDependencies` | 0 | All detected project dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L23) |
| `DocstringExtractor` | 3 | Extract and parse docstrings from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L23) |
| `DocstringInfo` | 0 | Parsed docstring with sections. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L12) |
| `Endpoint` | 0 | Represents a detected web endpoint. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L13) |
| `EndpointDetector` | 1 | Detects web endpoints from decorator patterns in source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L26) |
| `ProjectScanner` | 1 | Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L11) |
| `BaseGenerator` | 2 | Abstract base for all documentation generators. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L22) |
| `GenerateContext` | 0 | Shared context passed to all generators during a run. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L14) |
| `DefaultGroup` | 1 | Click Group that routes unknown subcommands to 'generate'. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L13) |
| `Code2DocsConfig` | 2 | Main configuration for code2docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L76) |
| `Code2LlmConfig` | 0 | Configuration for code2llm analysis generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L43) |
| `DocsConfig` | 0 | Configuration for docs/ generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L22) |
| `ExamplesConfig` | 0 | Configuration for examples/ generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L30) |
| `LLMConfig` | 1 | Configuration for optional LLM-assisted documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L55) |
| `ReadmeConfig` | 0 | Configuration for README generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L15) |
| `SyncConfig` | 0 | Configuration for synchronization. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L36) |
| `MarkdownFormatter` | 12 | Helper for constructing Markdown documents. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py#L6) |
| `ApiChangelogAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L111) |
| `ApiReferenceAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L34) |
| `ArchitectureAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L66) |
| `Code2LlmAdapter` | 2 | Adapter for code2llm analysis generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L206) |
| `ConfigDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L174) |
| `ContributingAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L190) |
| `CoverageAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L96) |
| `DepGraphAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L81) |
| `ExamplesAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L127) |
| `GettingStartedAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L158) |
| `IndexHtmlAdapter` | 2 | Adapter for generating index.html for GitHub Pages browsing. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L247) |
| `MkDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L143) |
| `ModuleDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L50) |
| `OrgReadmeAdapter` | 2 | Adapter for organization README generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L224) |
| `ReadmeGeneratorAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L11) |
| `SourceLinker` | 2 | Build source-code links (relative paths + optional GitHub/GitLab URLs). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py#L11) |
| `ApiChange` | 1 | A single API change between two analysis snapshots. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L16) |
| `ApiChangelogGenerator` | 2 | Generate API changelog by diffing current analysis with a saved snapshot. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L30) |
| `ApiReferenceGenerator` | 1 | Generate docs/api.md — consolidated API reference. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py#L13) |
| `ArchitectureGenerator` | 1 | Generate docs/architecture.md — architecture overview with diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py#L12) |
| `ChangelogEntry` | 0 | A single changelog entry. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L14) |
| `ChangelogGenerator` | 1 | Generate CHANGELOG.md from git log and analysis diff. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L23) |
| `Code2LlmGenerator` | 2 | Generate code2llm analysis files in project/ directory. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L62) |
| `ConfigDocsGenerator` | 1 | Generate docs/configuration.md from Code2DocsConfig dataclass. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py#L11) |
| `ContributingGenerator` | 1 | Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py#L11) |
| `CoverageGenerator` | 1 | Generate docs/coverage.md — docstring coverage report. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py#L11) |
| `DepGraphGenerator` | 1 | Generate docs/dependency-graph.md with Mermaid diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py#L12) |
| `ExamplesGenerator` | 2 | Generate examples/ — usage examples from public API signatures. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py#L66) |
| `GettingStartedGenerator` | 1 | Generate docs/getting-started.md from entry points and dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py#L12) |
| `MkDocsGenerator` | 2 | Generate mkdocs.yml from the docs/ directory structure. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py#L13) |
| `ModuleDocsGenerator` | 1 | Generate docs/modules.md — consolidated module documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py#L14) |
| `OrgReadmeGenerator` | 2 | Generate organization README with list of projects and brief descriptions. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/org_readme_gen.py#L12) |
| `ReadmeGenerator` | 2 | Generate README.md from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L24) |
| `LLMHelper` | 6 | Thin wrapper around litellm for documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py#L31) |
| `GeneratorRegistry` | 3 | Registry of documentation generators. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py#L6) |
| `ChangeInfo` | 0 | Describes a detected change. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L15) |
| `Differ` | 2 | Detect changes between current source and previous state. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L27) |
| `Updater` | 1 | Apply selective documentation updates based on detected changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py#L10) |

**`DocstringExtractor` methods:**

- `extract_all(result)` — Extract docstrings for all functions and classes.
- `parse(docstring)` — Parse a docstring into structured sections (orchestrator).
- `coverage_report(result)` — Calculate docstring coverage statistics.

**`BaseGenerator` methods:**

- `should_run()` — Return True if this generator should execute.
- `run(ctx)` — Execute generation and write output.

**`Code2DocsConfig` methods:**

- `from_yaml(cls, path)` — Load configuration from code2docs.yaml.
- `to_yaml(path)` — Save configuration to YAML file.

**`MarkdownFormatter` methods:**

- `heading(text, level)` — Add a heading.
- `paragraph(text)` — Add a paragraph.
- `blockquote(text)` — Add a blockquote.
- `code_block(code, language)` — Add a fenced code block.
- `inline_code(text)` — Return inline code string.
- `bold(text)` — Return bold string.
- `link(text, url)` — Return a Markdown link.
- `list_item(text, indent)` — Add a list item.
- `table(headers, rows)` — Add a Markdown table.
- `separator()` — Add a horizontal rule.
- `blank()` — Add a blank line.
- `render()` — Render accumulated Markdown to string.

**`ApiChangelogAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ApiReferenceAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ArchitectureAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`Code2LlmAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ConfigDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ContributingAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`CoverageAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`DepGraphAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ExamplesAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`GettingStartedAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`IndexHtmlAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`MkDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ModuleDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`OrgReadmeAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ReadmeGeneratorAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`SourceLinker` methods:**

- `source_link(file, line)` — Return a Markdown link to source, or empty string if unavailable.
- `file_link(file)` — Return a Markdown link to a file (no line number).

**`ApiChangelogGenerator` methods:**

- `generate(project_path)` — Generate api-changelog.md by comparing with previous snapshot.
- `save_snapshot(project_path)` — Save current API state as snapshot for future diffs.

**`Code2LlmGenerator` methods:**

- `generate_all()` — Generate all code2llm analysis files.
- `get_analysis_summary()` — Get a summary of the analysis for integration with other docs.

**`ExamplesGenerator` methods:**

- `generate_all()` — Generate all example files. Returns {filename: content}.
- `write_all(output_dir, files)` — Write all generated example files.

**`MkDocsGenerator` methods:**

- `generate(docs_dir)` — Generate mkdocs.yml content.
- `write(output_path, content)` — Write mkdocs.yml file.

**`OrgReadmeGenerator` methods:**

- `generate()` — Generate organization README content.
- `write(output_path, content)` — Write README to output path.

**`ReadmeGenerator` methods:**

- `generate()` — Generate full README content.
- `write(path, content)` — Write README, respecting sync markers if existing file has them.

**`LLMHelper` methods:**

- `complete(prompt, system)` — Send a completion request. Returns None on any failure.
- `generate_project_description(project_name, modules_summary, entry_points)` — Generate a concise project description from analysis data.
- `generate_architecture_summary(project_name, layers, patterns, metrics)` — Generate a natural-language architecture overview.
- `generate_getting_started_summary(project_name, cli_commands, public_api)` — Generate a getting-started introduction.
- `enhance_module_docstring(module_name, functions, classes)` — Generate a module-level summary from its contents.

**`GeneratorRegistry` methods:**

- `add(generator)` — Add a generator instance to the registry.
- `run_all(ctx)` — Run every registered generator that should execute.
- `run_only(name, ctx)` — Run a single generator by name.

**`Differ` methods:**

- `detect_changes(project_path)` — Compare current file hashes with saved state. Return list of changes.
- `save_state(project_path)` — Save current file hashes as state.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `analyze_and_document` | `analyze_and_document(project_path, config)` | 1 | Convenience function: analyze a project in one call. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L39) |
| `check` | `check(project_path, config_path, target)` | 1 | Health check — verify documentation completeness. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L91) |
| `diff` | `diff(project_path, config_path)` | 1 | Preview what would change without writing anything. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L99) |
| `generate` | `generate(project_path, config_path, readme_only, sections, ...)` | 7 | Generate documentation (default command). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L37) |
| `init` | `init(project_path, output)` | 1 | Initialize code2docs.yaml configuration file. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L79) |
| `main` | `main()` | 1 | code2docs — Auto-generate project documentation from source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L24) |
| `sync` | `sync(project_path, config_path, verbose, dry_run)` | 2 | Synchronize documentation with source code changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L58) |
| `watch` | `watch(project_path, config_path, verbose)` | 2 | Watch for file changes and auto-regenerate docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L69) |
| `generate_badges` | `generate_badges(project_name, badge_types, stats, deps)` | 4 | Generate shields.io badge Markdown strings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py#L7) |
| `extract_headings` | `extract_headings(content, max_depth)` | 6 | Extract headings from Markdown content. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L30) |
| `generate_toc` | `generate_toc(markdown_content, max_depth)` | 3 | Generate a table of contents from Markdown headings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L7) |
| `generate_code2llm_analysis` | `generate_code2llm_analysis(project_path, config)` | 2 | Convenience function to generate code2llm analysis. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L188) |
| `parse_gitignore` | `parse_gitignore(project_path)` | 15 ⚠️ | Parse .gitignore file and return list of patterns to exclude. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L12) |
| `generate_docs` | `generate_docs(project_path, config)` | 5 | High-level function to generate all documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py#L35) |
| `generate_readme` | `generate_readme(project_path, output, sections, sync_markers, ...)` | 3 | Convenience function to generate a README. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L310) |
| `start_watcher` | `start_watcher(project_path, config)` | 5 | Start watching project for file changes and auto-resync docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py#L10) |

## code2docs

### `code2docs.analyzers` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DependencyInfo` | 0 | Information about a project dependency. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L15) |
| `DependencyScanner` | 1 | Scan and parse project dependency files. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L38) |
| `ProjectDependencies` | 0 | All detected project dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L23) |
| `DocstringExtractor` | 3 | Extract and parse docstrings from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L23) |
| `DocstringInfo` | 0 | Parsed docstring with sections. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L12) |
| `Endpoint` | 0 | Represents a detected web endpoint. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L13) |
| `EndpointDetector` | 1 | Detects web endpoints from decorator patterns in source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L26) |
| `ProjectScanner` | 1 | Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L11) |

**`DocstringExtractor` methods:**

- `extract_all(result)` — Extract docstrings for all functions and classes.
- `parse(docstring)` — Parse a docstring into structured sections (orchestrator).
- `coverage_report(result)` — Calculate docstring coverage statistics.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `analyze_and_document` | `analyze_and_document(project_path, config)` | 1 | Convenience function: analyze a project in one call. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L39) |

### `code2docs.analyzers.dependency_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DependencyInfo` | 0 | Information about a project dependency. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L15) |
| `DependencyScanner` | 1 | Scan and parse project dependency files. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L38) |
| `ProjectDependencies` | 0 | All detected project dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/dependency_scanner.py#L23) |

### `code2docs.analyzers.docstring_extractor` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DocstringExtractor` | 3 | Extract and parse docstrings from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L23) |
| `DocstringInfo` | 0 | Parsed docstring with sections. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/docstring_extractor.py#L12) |

**`DocstringExtractor` methods:**

- `extract_all(result)` — Extract docstrings for all functions and classes.
- `parse(docstring)` — Parse a docstring into structured sections (orchestrator).
- `coverage_report(result)` — Calculate docstring coverage statistics.

### `code2docs.analyzers.endpoint_detector` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `Endpoint` | 0 | Represents a detected web endpoint. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L13) |
| `EndpointDetector` | 1 | Detects web endpoints from decorator patterns in source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/endpoint_detector.py#L26) |

### `code2docs.analyzers.project_scanner` [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ProjectScanner` | 1 | Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L11) |

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `analyze_and_document` | `analyze_and_document(project_path, config)` | 1 | Convenience function: analyze a project in one call. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/analyzers/project_scanner.py#L39) |

### `code2docs.base` [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `BaseGenerator` | 2 | Abstract base for all documentation generators. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L22) |
| `GenerateContext` | 0 | Shared context passed to all generators during a run. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/base.py#L14) |

**`BaseGenerator` methods:**

- `should_run()` — Return True if this generator should execute.
- `run(ctx)` — Execute generation and write output.

### `code2docs.cli` [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DefaultGroup` | 1 | Click Group that routes unknown subcommands to 'generate'. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L13) |

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `check` | `check(project_path, config_path, target)` | 1 | Health check — verify documentation completeness. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L91) |
| `diff` | `diff(project_path, config_path)` | 1 | Preview what would change without writing anything. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L99) |
| `generate` | `generate(project_path, config_path, readme_only, sections, ...)` | 7 | Generate documentation (default command). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L37) |
| `init` | `init(project_path, output)` | 1 | Initialize code2docs.yaml configuration file. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L79) |
| `main` | `main()` | 1 | code2docs — Auto-generate project documentation from source code. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L24) |
| `sync` | `sync(project_path, config_path, verbose, dry_run)` | 2 | Synchronize documentation with source code changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L58) |
| `watch` | `watch(project_path, config_path, verbose)` | 2 | Watch for file changes and auto-regenerate docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/cli.py#L69) |

### `code2docs.config` [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `Code2DocsConfig` | 2 | Main configuration for code2docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L76) |
| `Code2LlmConfig` | 0 | Configuration for code2llm analysis generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L43) |
| `DocsConfig` | 0 | Configuration for docs/ generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L22) |
| `ExamplesConfig` | 0 | Configuration for examples/ generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L30) |
| `LLMConfig` | 1 | Configuration for optional LLM-assisted documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L55) |
| `ReadmeConfig` | 0 | Configuration for README generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L15) |
| `SyncConfig` | 0 | Configuration for synchronization. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/config.py#L36) |

**`Code2DocsConfig` methods:**

- `from_yaml(cls, path)` — Load configuration from code2docs.yaml.
- `to_yaml(path)` — Save configuration to YAML file.

### `code2docs.formatters` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `MarkdownFormatter` | 12 | Helper for constructing Markdown documents. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py#L6) |

**`MarkdownFormatter` methods:**

- `heading(text, level)` — Add a heading.
- `paragraph(text)` — Add a paragraph.
- `blockquote(text)` — Add a blockquote.
- `code_block(code, language)` — Add a fenced code block.
- `inline_code(text)` — Return inline code string.
- `bold(text)` — Return bold string.
- `link(text, url)` — Return a Markdown link.
- `list_item(text, indent)` — Add a list item.
- `table(headers, rows)` — Add a Markdown table.
- `separator()` — Add a horizontal rule.
- `blank()` — Add a blank line.
- `render()` — Render accumulated Markdown to string.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_badges` | `generate_badges(project_name, badge_types, stats, deps)` | 4 | Generate shields.io badge Markdown strings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py#L7) |
| `extract_headings` | `extract_headings(content, max_depth)` | 6 | Extract headings from Markdown content. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L30) |
| `generate_toc` | `generate_toc(markdown_content, max_depth)` | 3 | Generate a table of contents from Markdown headings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L7) |

### `code2docs.formatters.badges` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_badges` | `generate_badges(project_name, badge_types, stats, deps)` | 4 | Generate shields.io badge Markdown strings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/badges.py#L7) |

### `code2docs.formatters.markdown` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `MarkdownFormatter` | 12 | Helper for constructing Markdown documents. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/markdown.py#L6) |

**`MarkdownFormatter` methods:**

- `heading(text, level)` — Add a heading.
- `paragraph(text)` — Add a paragraph.
- `blockquote(text)` — Add a blockquote.
- `code_block(code, language)` — Add a fenced code block.
- `inline_code(text)` — Return inline code string.
- `bold(text)` — Return bold string.
- `link(text, url)` — Return a Markdown link.
- `list_item(text, indent)` — Add a list item.
- `table(headers, rows)` — Add a Markdown table.
- `separator()` — Add a horizontal rule.
- `blank()` — Add a blank line.
- `render()` — Render accumulated Markdown to string.

### `code2docs.formatters.toc` [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `extract_headings` | `extract_headings(content, max_depth)` | 6 | Extract headings from Markdown content. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L30) |
| `generate_toc` | `generate_toc(markdown_content, max_depth)` | 3 | Generate a table of contents from Markdown headings. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/formatters/toc.py#L7) |

### `code2docs.generators` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiChangelogAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L111) |
| `ApiReferenceAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L34) |
| `ArchitectureAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L66) |
| `Code2LlmAdapter` | 2 | Adapter for code2llm analysis generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L206) |
| `ConfigDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L174) |
| `ContributingAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L190) |
| `CoverageAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L96) |
| `DepGraphAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L81) |
| `ExamplesAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L127) |
| `GettingStartedAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L158) |
| `IndexHtmlAdapter` | 2 | Adapter for generating index.html for GitHub Pages browsing. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L247) |
| `MkDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L143) |
| `ModuleDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L50) |
| `OrgReadmeAdapter` | 2 | Adapter for organization README generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L224) |
| `ReadmeGeneratorAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L11) |
| `SourceLinker` | 2 | Build source-code links (relative paths + optional GitHub/GitLab URLs). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py#L11) |
| `ApiChange` | 1 | A single API change between two analysis snapshots. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L16) |
| `ApiChangelogGenerator` | 2 | Generate API changelog by diffing current analysis with a saved snapshot. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L30) |
| `ApiReferenceGenerator` | 1 | Generate docs/api.md — consolidated API reference. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py#L13) |
| `ArchitectureGenerator` | 1 | Generate docs/architecture.md — architecture overview with diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py#L12) |
| `ChangelogEntry` | 0 | A single changelog entry. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L14) |
| `ChangelogGenerator` | 1 | Generate CHANGELOG.md from git log and analysis diff. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L23) |
| `Code2LlmGenerator` | 2 | Generate code2llm analysis files in project/ directory. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L62) |
| `ConfigDocsGenerator` | 1 | Generate docs/configuration.md from Code2DocsConfig dataclass. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py#L11) |
| `ContributingGenerator` | 1 | Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py#L11) |
| `CoverageGenerator` | 1 | Generate docs/coverage.md — docstring coverage report. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py#L11) |
| `DepGraphGenerator` | 1 | Generate docs/dependency-graph.md with Mermaid diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py#L12) |
| `ExamplesGenerator` | 2 | Generate examples/ — usage examples from public API signatures. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py#L66) |
| `GettingStartedGenerator` | 1 | Generate docs/getting-started.md from entry points and dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py#L12) |
| `MkDocsGenerator` | 2 | Generate mkdocs.yml from the docs/ directory structure. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py#L13) |
| `ModuleDocsGenerator` | 1 | Generate docs/modules.md — consolidated module documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py#L14) |
| `OrgReadmeGenerator` | 2 | Generate organization README with list of projects and brief descriptions. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/org_readme_gen.py#L12) |
| `ReadmeGenerator` | 2 | Generate README.md from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L24) |

**`ApiChangelogAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ApiReferenceAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ArchitectureAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`Code2LlmAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ConfigDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ContributingAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`CoverageAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`DepGraphAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ExamplesAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`GettingStartedAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`IndexHtmlAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`MkDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ModuleDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`OrgReadmeAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ReadmeGeneratorAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`SourceLinker` methods:**

- `source_link(file, line)` — Return a Markdown link to source, or empty string if unavailable.
- `file_link(file)` — Return a Markdown link to a file (no line number).

**`ApiChangelogGenerator` methods:**

- `generate(project_path)` — Generate api-changelog.md by comparing with previous snapshot.
- `save_snapshot(project_path)` — Save current API state as snapshot for future diffs.

**`Code2LlmGenerator` methods:**

- `generate_all()` — Generate all code2llm analysis files.
- `get_analysis_summary()` — Get a summary of the analysis for integration with other docs.

**`ExamplesGenerator` methods:**

- `generate_all()` — Generate all example files. Returns {filename: content}.
- `write_all(output_dir, files)` — Write all generated example files.

**`MkDocsGenerator` methods:**

- `generate(docs_dir)` — Generate mkdocs.yml content.
- `write(output_path, content)` — Write mkdocs.yml file.

**`OrgReadmeGenerator` methods:**

- `generate()` — Generate organization README content.
- `write(output_path, content)` — Write README to output path.

**`ReadmeGenerator` methods:**

- `generate()` — Generate full README content.
- `write(path, content)` — Write README, respecting sync markers if existing file has them.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_code2llm_analysis` | `generate_code2llm_analysis(project_path, config)` | 2 | Convenience function to generate code2llm analysis. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L188) |
| `parse_gitignore` | `parse_gitignore(project_path)` | 15 ⚠️ | Parse .gitignore file and return list of patterns to exclude. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L12) |
| `generate_docs` | `generate_docs(project_path, config)` | 5 | High-level function to generate all documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/__init__.py#L35) |
| `generate_readme` | `generate_readme(project_path, output, sections, sync_markers, ...)` | 3 | Convenience function to generate a README. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L310) |

### `code2docs.generators._registry_adapters` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiChangelogAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L111) |
| `ApiReferenceAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L34) |
| `ArchitectureAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L66) |
| `Code2LlmAdapter` | 2 | Adapter for code2llm analysis generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L206) |
| `ConfigDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L174) |
| `ContributingAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L190) |
| `CoverageAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L96) |
| `DepGraphAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L81) |
| `ExamplesAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L127) |
| `GettingStartedAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L158) |
| `IndexHtmlAdapter` | 2 | Adapter for generating index.html for GitHub Pages browsing. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L247) |
| `MkDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L143) |
| `ModuleDocsAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L50) |
| `OrgReadmeAdapter` | 2 | Adapter for organization README generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L224) |
| `ReadmeGeneratorAdapter` | 2 | — | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_registry_adapters.py#L11) |

**`ApiChangelogAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ApiReferenceAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ArchitectureAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`Code2LlmAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ConfigDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ContributingAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`CoverageAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`DepGraphAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ExamplesAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`GettingStartedAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`IndexHtmlAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`MkDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ModuleDocsAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`OrgReadmeAdapter` methods:**

- `should_run()`
- `run(ctx)`

**`ReadmeGeneratorAdapter` methods:**

- `should_run()`
- `run(ctx)`

### `code2docs.generators._source_links` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `SourceLinker` | 2 | Build source-code links (relative paths + optional GitHub/GitLab URLs). | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/_source_links.py#L11) |

**`SourceLinker` methods:**

- `source_link(file, line)` — Return a Markdown link to source, or empty string if unavailable.
- `file_link(file)` — Return a Markdown link to a file (no line number).

### `code2docs.generators.api_changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiChange` | 1 | A single API change between two analysis snapshots. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L16) |
| `ApiChangelogGenerator` | 2 | Generate API changelog by diffing current analysis with a saved snapshot. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_changelog_gen.py#L30) |

**`ApiChangelogGenerator` methods:**

- `generate(project_path)` — Generate api-changelog.md by comparing with previous snapshot.
- `save_snapshot(project_path)` — Save current API state as snapshot for future diffs.

### `code2docs.generators.api_reference_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ApiReferenceGenerator` | 1 | Generate docs/api.md — consolidated API reference. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/api_reference_gen.py#L13) |

### `code2docs.generators.architecture_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ArchitectureGenerator` | 1 | Generate docs/architecture.md — architecture overview with diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/architecture_gen.py#L12) |

### `code2docs.generators.changelog_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ChangelogEntry` | 0 | A single changelog entry. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L14) |
| `ChangelogGenerator` | 1 | Generate CHANGELOG.md from git log and analysis diff. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/changelog_gen.py#L23) |

### `code2docs.generators.code2llm_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `Code2LlmGenerator` | 2 | Generate code2llm analysis files in project/ directory. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L62) |

**`Code2LlmGenerator` methods:**

- `generate_all()` — Generate all code2llm analysis files.
- `get_analysis_summary()` — Get a summary of the analysis for integration with other docs.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_code2llm_analysis` | `generate_code2llm_analysis(project_path, config)` | 2 | Convenience function to generate code2llm analysis. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L188) |
| `parse_gitignore` | `parse_gitignore(project_path)` | 15 ⚠️ | Parse .gitignore file and return list of patterns to exclude. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/code2llm_gen.py#L12) |

### `code2docs.generators.config_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ConfigDocsGenerator` | 1 | Generate docs/configuration.md from Code2DocsConfig dataclass. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/config_docs_gen.py#L11) |

### `code2docs.generators.contributing_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ContributingGenerator` | 1 | Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/contributing_gen.py#L11) |

### `code2docs.generators.coverage_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `CoverageGenerator` | 1 | Generate docs/coverage.md — docstring coverage report. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/coverage_gen.py#L11) |

### `code2docs.generators.depgraph_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `DepGraphGenerator` | 1 | Generate docs/dependency-graph.md with Mermaid diagrams. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/depgraph_gen.py#L12) |

### `code2docs.generators.examples_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ExamplesGenerator` | 2 | Generate examples/ — usage examples from public API signatures. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/examples_gen.py#L66) |

**`ExamplesGenerator` methods:**

- `generate_all()` — Generate all example files. Returns {filename: content}.
- `write_all(output_dir, files)` — Write all generated example files.

### `code2docs.generators.getting_started_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `GettingStartedGenerator` | 1 | Generate docs/getting-started.md from entry points and dependencies. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/getting_started_gen.py#L12) |

### `code2docs.generators.mkdocs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `MkDocsGenerator` | 2 | Generate mkdocs.yml from the docs/ directory structure. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/mkdocs_gen.py#L13) |

**`MkDocsGenerator` methods:**

- `generate(docs_dir)` — Generate mkdocs.yml content.
- `write(output_path, content)` — Write mkdocs.yml file.

### `code2docs.generators.module_docs_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ModuleDocsGenerator` | 1 | Generate docs/modules.md — consolidated module documentation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/module_docs_gen.py#L14) |

### `code2docs.generators.org_readme_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/org_readme_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `OrgReadmeGenerator` | 2 | Generate organization README with list of projects and brief descriptions. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/org_readme_gen.py#L12) |

**`OrgReadmeGenerator` methods:**

- `generate()` — Generate organization README content.
- `write(output_path, content)` — Write README to output path.

### `code2docs.generators.readme_gen` [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ReadmeGenerator` | 2 | Generate README.md from AnalysisResult. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L24) |

**`ReadmeGenerator` methods:**

- `generate()` — Generate full README content.
- `write(path, content)` — Write README, respecting sync markers if existing file has them.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_readme` | `generate_readme(project_path, output, sections, sync_markers, ...)` | 3 | Convenience function to generate a README. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/generators/readme_gen.py#L310) |

### `code2docs.llm_helper` [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `LLMHelper` | 6 | Thin wrapper around litellm for documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/llm_helper.py#L31) |

**`LLMHelper` methods:**

- `complete(prompt, system)` — Send a completion request. Returns None on any failure.
- `generate_project_description(project_name, modules_summary, entry_points)` — Generate a concise project description from analysis data.
- `generate_architecture_summary(project_name, layers, patterns, metrics)` — Generate a natural-language architecture overview.
- `generate_getting_started_summary(project_name, cli_commands, public_api)` — Generate a getting-started introduction.
- `enhance_module_docstring(module_name, functions, classes)` — Generate a module-level summary from its contents.

### `code2docs.registry` [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `GeneratorRegistry` | 3 | Registry of documentation generators. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/registry.py#L6) |

**`GeneratorRegistry` methods:**

- `add(generator)` — Add a generator instance to the registry.
- `run_all(ctx)` — Run every registered generator that should execute.
- `run_only(name, ctx)` — Run a single generator by name.

### `code2docs.sync` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/__init__.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ChangeInfo` | 0 | Describes a detected change. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L15) |
| `Differ` | 2 | Detect changes between current source and previous state. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L27) |
| `Updater` | 1 | Apply selective documentation updates based on detected changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py#L10) |

**`Differ` methods:**

- `detect_changes(project_path)` — Compare current file hashes with saved state. Return list of changes.
- `save_state(project_path)` — Save current file hashes as state.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `start_watcher` | `start_watcher(project_path, config)` | 5 | Start watching project for file changes and auto-resync docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py#L10) |

### `code2docs.sync.differ` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `ChangeInfo` | 0 | Describes a detected change. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L15) |
| `Differ` | 2 | Detect changes between current source and previous state. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/differ.py#L27) |

**`Differ` methods:**

- `detect_changes(project_path)` — Compare current file hashes with saved state. Return list of changes.
- `save_state(project_path)` — Save current file hashes as state.

### `code2docs.sync.updater` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `Updater` | 1 | Apply selective documentation updates based on detected changes. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/updater.py#L10) |

### `code2docs.sync.watcher` [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `start_watcher` | `start_watcher(project_path, config)` | 5 | Start watching project for file changes and auto-resync docs. | [source](https://github.com/wronai/code2docs/blob/main/code2docs/sync/watcher.py#L10) |

## examples

### `examples.01_cli_usage` [source](https://github.com/wronai/code2docs/blob/main/examples/01_cli_usage.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `run_cli_basic` | `run_cli_basic(project_path)` | 1 | Run code2docs CLI programmatically. | [source](https://github.com/wronai/code2docs/blob/main/examples/01_cli_usage.py#L47) |
| `run_cli_with_config` | `run_cli_with_config(project_path, config_path)` | 1 | Run with custom configuration. | [source](https://github.com/wronai/code2docs/blob/main/examples/01_cli_usage.py#L58) |

### `examples.02_configuration` [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `create_advanced_config` | `create_advanced_config()` | 1 | Create advanced configuration with all options. | [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L34) |
| `create_basic_config` | `create_basic_config()` | 1 | Create a basic configuration. | [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L16) |
| `load_config_from_yaml` | `load_config_from_yaml(path)` | 1 | Load configuration from YAML file. | [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L142) |
| `save_yaml_config_example` | `save_yaml_config_example(path)` | 1 | Save example YAML config to file. | [source](https://github.com/wronai/code2docs/blob/main/examples/02_configuration.py#L136) |

### `examples.03_programmatic_api` [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `custom_documentation_pipeline` | `custom_documentation_pipeline(project_path)` | 1 | Create a custom documentation pipeline. | [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L34) |
| `generate_docs_if_needed` | `generate_docs_if_needed(project_path, force)` | 3 | Only generate docs if code has changed. | [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L68) |
| `generate_full_documentation` | `generate_full_documentation(project_path)` | 2 | Generate complete documentation for a project. | [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L19) |
| `generate_readme_simple` | `generate_readme_simple(project_path)` | 1 | Generate README.md content from a project. | [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L12) |
| `inspect_project_structure` | `inspect_project_structure(project_path)` | 5 | Inspect project structure from analysis. | [source](https://github.com/wronai/code2docs/blob/main/examples/03_programmatic_api.py#L50) |

### `examples.04_sync_and_watch` [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `custom_watcher_with_hooks` | `custom_watcher_with_hooks(project_path)` | 3 | Set up a custom watcher with pre/post generation hooks. | [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L69) |
| `detect_changes_example` | `detect_changes_example(project_path)` | 1 | Detect what files have changed since last documentation generation. | [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L15) |
| `force_full_regeneration` | `force_full_regeneration(project_path)` | 1 | Force full regeneration of all documentation. | [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L45) |
| `sync_with_git_changes` | `sync_with_git_changes(project_path)` | 4 | Only regenerate docs for files changed in git. | [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L105) |
| `update_docs_incrementally` | `update_docs_incrementally(project_path)` | 2 | Update only the parts of docs that need changing. | [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L33) |
| `watch_and_auto_regenerate` | `watch_and_auto_regenerate(project_path, interval)` | 2 | Watch for file changes and auto-regenerate documentation. | [source](https://github.com/wronai/code2docs/blob/main/examples/04_sync_and_watch.py#L54) |

### `examples.05_custom_generators` [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py)

| Class | Methods | Description | Source |
|-------|---------|-------------|--------|
| `APIChangelogGenerator` | 1 | Generate changelog based on API changes. | [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L69) |
| `CustomGenerator` | 2 | Example of extending the base generator class. | [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L132) |
| `MetricsReportGenerator` | 1 | Generate a metrics report from code analysis. | [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L11) |

**`CustomGenerator` methods:**

- `generate()` — Override to provide custom generation logic.
- `write(path, content)` — Override to customize file writing.

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `generate_custom_report` | `generate_custom_report(project_path)` | 1 | Generate a custom metrics report. | [source](https://github.com/wronai/code2docs/blob/main/examples/05_custom_generators.py#L119) |

### `examples.06_formatters` [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `badge_examples` | `badge_examples()` | 2 | Generate various badge examples. | [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L53) |
| `build_custom_readme` | `build_custom_readme()` | 2 | Build a custom README using formatters. | [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L71) |
| `generate_complex_document` | `generate_complex_document()` | 1 | Generate a complex markdown document using the formatter. | [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L30) |
| `markdown_formatting_examples` | `markdown_formatting_examples()` | 1 | Demonstrate markdown formatting utilities. | [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L10) |
| `toc_examples` | `toc_examples()` | 2 | Demonstrate table of contents generation. | [source](https://github.com/wronai/code2docs/blob/main/examples/06_formatters.py#L60) |

### `examples.07_web_frameworks` [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py)

| Function | Signature | CC | Description | Source |
|----------|-----------|----|-----------  |--------|
| `create_example_web_apps` | `create_example_web_apps(target_dir)` | 1 | Create example Flask and FastAPI apps for testing. | [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L157) |
| `detect_fastapi_endpoints` | `detect_fastapi_endpoints(project_path)` | 4 | Detect FastAPI endpoints in a project. | [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L33) |
| `detect_flask_endpoints` | `detect_flask_endpoints(project_path)` | 4 | Detect Flask endpoints in a project. | [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L16) |
| `document_web_project` | `document_web_project(project_path)` | 3 | Complete workflow: detect endpoints and generate docs. | [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L177) |
| `generate_api_docs_from_endpoints` | `generate_api_docs_from_endpoints(project_path, output_dir)` | 9 | Generate API documentation from detected endpoints. | [source](https://github.com/wronai/code2docs/blob/main/examples/07_web_frameworks.py#L55) |
