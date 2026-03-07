<!-- code2docs:start --># code2docs

![version](https://img.shields.io/badge/version-0.1.0-blue) ![python](https://img.shields.io/badge/python-%3E%3D3.9-blue) ![coverage](https://img.shields.io/badge/coverage-unknown-lightgrey) ![functions](https://img.shields.io/badge/functions-185-green)
> **185** functions | **42** classes | **31** files | CC̄ = 3.8

## Installation

```bash
pip install .
```


## Quick Start

```python
# Entry point: registry.GeneratorRegistry.__init__
# Entry point: registry.GeneratorRegistry.add
# Entry point: registry.GeneratorRegistry.run_all
```

## API Overview

### Classes

- **`GeneratorRegistry`** — Registry of documentation generators.
- **`Updater`** — Apply selective documentation updates based on detected changes.
- **`ChangeInfo`** — Describes a detected change.
- **`Differ`** — Detect changes between current source and previous state.
- **`MarkdownFormatter`** — Helper for constructing Markdown documents.
- **`ReadmeGenerator`** — Generate README.md from AnalysisResult.
- **`CoverageGenerator`** — Generate docs/coverage.md — docstring coverage report.
- **`DepGraphGenerator`** — Generate docs/dependency-graph.md with Mermaid diagrams.
- **`GenerateContext`** — Shared context passed to all generators during a run.
- **`BaseGenerator`** — Abstract base for all documentation generators.
- **`ChangelogEntry`** — A single changelog entry.
- **`ChangelogGenerator`** — Generate CHANGELOG.md from git log and analysis diff.
- **`ApiReferenceGenerator`** — Generate docs/api/ — per-module API reference from signatures.
- **`ModuleDocsGenerator`** — Generate docs/modules/ — detailed per-module documentation.
- **`MkDocsGenerator`** — Generate mkdocs.yml from the docs/ directory structure.
- **`ExamplesGenerator`** — Generate examples/ — usage examples from public API signatures.
- **`ReadmeGeneratorAdapter`**
- **`ApiReferenceAdapter`**
- **`ModuleDocsAdapter`**
- **`ArchitectureAdapter`**
- **`DepGraphAdapter`**
- **`CoverageAdapter`**
- **`ApiChangelogAdapter`**
- **`ExamplesAdapter`**
- **`MkDocsAdapter`**
- **`ArchitectureGenerator`** — Generate docs/architecture.md — architecture overview with diagrams.
- **`ApiChange`** — A single API change between two analysis snapshots.
- **`ApiChangelogGenerator`** — Generate API changelog by diffing current analysis with a saved snapshot.
- **`DefaultGroup`** — Click Group that routes unknown subcommands to 'generate'.
- **`ReadmeConfig`** — Configuration for README generation.
- **`DocsConfig`** — Configuration for docs/ generation.
- **`ExamplesConfig`** — Configuration for examples/ generation.
- **`SyncConfig`** — Configuration for synchronization.
- **`Code2DocsConfig`** — Main configuration for code2docs.
- **`ProjectScanner`** — Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.
- **`DocstringInfo`** — Parsed docstring with sections.
- **`DocstringExtractor`** — Extract and parse docstrings from AnalysisResult.
- **`DependencyInfo`** — Information about a project dependency.
- **`ProjectDependencies`** — All detected project dependencies.
- **`DependencyScanner`** — Scan and parse project dependency files.
- **`Endpoint`** — Represents a detected web endpoint.
- **`EndpointDetector`** — Detects web endpoints from decorator patterns in source code.

### Functions

- `start_watcher(project_path, config)` — Start watching project for file changes and auto-resync docs.
- `generate_badges(project_name, badge_types, stats, deps)` — Generate shields.io badge Markdown strings.
- `generate_toc(markdown_content, max_depth)` — Generate a table of contents from Markdown headings.
- `extract_headings(content, max_depth)` — Extract headings from Markdown content.
- `generate_readme(project_path, output, sections, sync_markers, config)` — Convenience function to generate a README.
- `generate_docs(project_path, config)` — High-level function to generate all documentation.
- `main()` — code2docs — Auto-generate project documentation from source code.
- `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run)` — Generate documentation (default command).
- `sync(project_path, config_path, verbose, dry_run)` — Synchronize documentation with source code changes.
- `watch(project_path, config_path, verbose)` — Watch for file changes and auto-regenerate docs.
- `init(project_path, output)` — Initialize code2docs.yaml configuration file.
- `analyze_and_document(project_path, config)` — Convenience function: analyze a project in one call.

## Project Structure

📄 `__main__`
📦 `analyzers`
📄 `analyzers.dependency_scanner` (6 functions, 3 classes)
📄 `analyzers.docstring_extractor` (10 functions, 2 classes)
📄 `analyzers.endpoint_detector` (3 functions, 2 classes)
📄 `analyzers.project_scanner` (4 functions, 1 classes)
📄 `base` (3 functions, 2 classes)
📄 `cli` (10 functions, 1 classes)
📦 `code2docs` (1 functions)
📄 `config` (2 functions, 5 classes)
📦 `formatters`
📄 `formatters.badges` (2 functions)
📄 `formatters.markdown` (13 functions, 1 classes)
📄 `formatters.toc` (3 functions)
📦 `generators` (1 functions)
📄 `generators._registry_adapters` (18 functions, 9 classes)
📄 `generators.api_changelog_gen` (9 functions, 2 classes)
📄 `generators.api_reference_gen` (11 functions, 1 classes)
📄 `generators.architecture_gen` (6 functions, 1 classes)
📄 `generators.changelog_gen` (6 functions, 2 classes)
📄 `generators.coverage_gen` (7 functions, 1 classes)
📄 `generators.depgraph_gen` (9 functions, 1 classes)
📄 `generators.examples_gen` (12 functions, 1 classes)
📄 `generators.mkdocs_gen` (4 functions, 1 classes)
📄 `generators.module_docs_gen` (17 functions, 1 classes)
📄 `generators.readme_gen` (14 functions, 1 classes)
📄 `registry` (4 functions, 1 classes)
📦 `sync`
📄 `sync.differ` (7 functions, 2 classes)
📄 `sync.updater` (2 functions, 1 classes)
📄 `sync.watcher` (1 functions)


<!-- code2docs:end -->