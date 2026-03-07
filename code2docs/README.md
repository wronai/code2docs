<!-- code2docs:start --># code2docs

![version](https://img.shields.io/badge/version-0.1.0-blue) ![python](https://img.shields.io/badge/python-%3E%3D3.9-blue) ![coverage](https://img.shields.io/badge/coverage-unknown-lightgrey) ![functions](https://img.shields.io/badge/functions-229-green)
> **229** functions | **51** classes | **38** files | CC̄ = 4.0

> Auto-generated project documentation from source code analysis.

**Author:** Tom Softreck <tom@sapletta.com>  
**License:** MIT[(LICENSE)](./LICENSE)  
**Repository:** [https://github.com/wronai/code2docs](https://github.com/wronai/code2docs)

## Installation

### From PyPI

```bash
pip install code2docs
```

### From Source

```bash
git clone https://github.com/wronai/code2docs
cd code2docs
pip install -e .
```


## Quick Start

### CLI Usage

```bash
# Generate full documentation for your project
code2docs ./my-project

# Only regenerate README
code2docs ./my-project --readme-only

# Preview what would be generated (no file writes)
code2docs ./my-project --dry-run

# Check documentation health
code2docs check ./my-project

# Sync — regenerate only changed modules
code2docs sync ./my-project
```

### Python API

```python
from code2docs import generate_readme, generate_docs, Code2DocsConfig

# Quick: generate README
generate_readme("./my-project")

# Full: generate all documentation
config = Code2DocsConfig(project_name="mylib", verbose=True)
docs = generate_docs("./my-project", config=config)
```

## Generated Output

When you run `code2docs`, the following files are produced:

```
<project>/
├── README.md                 # Main project README (auto-generated sections)
├── docs/
│   ├── api.md               # Consolidated API reference
│   ├── modules.md           # Module documentation with metrics
│   ├── architecture.md      # Architecture overview with diagrams
│   ├── dependency-graph.md  # Module dependency graphs
│   ├── coverage.md          # Docstring coverage report
│   ├── getting-started.md   # Getting started guide
│   ├── configuration.md    # Configuration reference
│   └── api-changelog.md    # API change tracking
├── examples/
│   ├── quickstart.py       # Basic usage examples
│   └── advanced_usage.py   # Advanced usage examples
├── CONTRIBUTING.md         # Contribution guidelines
└── mkdocs.yml             # MkDocs site configuration
```

## Configuration

Create `code2docs.yaml` in your project root (or run `code2docs init`):

```yaml
project:
  name: my-project
  source: ./
  output: ./docs/

readme:
  sections:
    - overview
    - install
    - quickstart
    - api
    - structure
  badges:
    - version
    - python
    - coverage
  sync_markers: true

docs:
  api_reference: true
  module_docs: true
  architecture: true
  changelog: true

examples:
  auto_generate: true
  from_entry_points: true

sync:
  strategy: markers    # markers | full | git-diff
  watch: false
  ignore:
    - "tests/"
    - "__pycache__"
```

## Sync Markers

code2docs can update only specific sections of an existing README using HTML comment markers:

```markdown
<!-- code2docs:start -->
# Project Title
... auto-generated content ...
<!-- code2docs:end -->
```

Content outside the markers is preserved when regenerating. Enable this with `sync_markers: true` in your configuration.

## Architecture

```
code2docs/
├── registry├── llm_helper├── code2docs/    ├── updater├── sync/    ├── watcher    ├── differ    ├── quickstart    ├── advanced_usage    ├── markdown    ├── badges    ├── toc├── formatters/    ├── readme_gen├── base    ├── coverage_gen    ├── _source_links    ├── depgraph_gen    ├── getting_started_gen    ├── config_docs_gen    ├── changelog_gen├── generators/    ├── module_docs_gen    ├── api_reference_gen    ├── mkdocs_gen    ├── examples_gen    ├── _registry_adapters├── cli    ├── api_changelog_gen    ├── contributing_gen├── analyzers/    ├── architecture_gen├── config    ├── project_scanner    ├── dependency_scanner    ├── endpoint_detector    ├── docstring_extractor```

## API Overview

### Classes

- **`GeneratorRegistry`** — Registry of documentation generators.
- **`LLMHelper`** — Thin wrapper around litellm for documentation generation.
- **`Updater`** — Apply selective documentation updates based on detected changes.
- **`ChangeInfo`** — Describes a detected change.
- **`Differ`** — Detect changes between current source and previous state.
- **`MarkdownFormatter`** — Helper for constructing Markdown documents.
- **`ReadmeGenerator`** — Generate README.md from AnalysisResult.
- **`GenerateContext`** — Shared context passed to all generators during a run.
- **`BaseGenerator`** — Abstract base for all documentation generators.
- **`CoverageGenerator`** — Generate docs/coverage.md — docstring coverage report.
- **`SourceLinker`** — Build source-code links (relative paths + optional GitHub/GitLab URLs).
- **`DepGraphGenerator`** — Generate docs/dependency-graph.md with Mermaid diagrams.
- **`GettingStartedGenerator`** — Generate docs/getting-started.md from entry points and dependencies.
- **`ConfigDocsGenerator`** — Generate docs/configuration.md from Code2DocsConfig dataclass.
- **`ChangelogEntry`** — A single changelog entry.
- **`ChangelogGenerator`** — Generate CHANGELOG.md from git log and analysis diff.
- **`ModuleDocsGenerator`** — Generate docs/modules.md — consolidated module documentation.
- **`ApiReferenceGenerator`** — Generate docs/api.md — consolidated API reference.
- **`MkDocsGenerator`** — Generate mkdocs.yml from the docs/ directory structure.
- **`ExamplesGenerator`** — Generate examples/ — usage examples from public API signatures.
- **`ReadmeGeneratorAdapter`** — —
- **`ApiReferenceAdapter`** — —
- **`ModuleDocsAdapter`** — —
- **`ArchitectureAdapter`** — —
- **`DepGraphAdapter`** — —
- **`CoverageAdapter`** — —
- **`ApiChangelogAdapter`** — —
- **`ExamplesAdapter`** — —
- **`MkDocsAdapter`** — —
- **`GettingStartedAdapter`** — —
- **`ConfigDocsAdapter`** — —
- **`ContributingAdapter`** — —
- **`DefaultGroup`** — Click Group that routes unknown subcommands to 'generate'.
- **`ApiChange`** — A single API change between two analysis snapshots.
- **`ApiChangelogGenerator`** — Generate API changelog by diffing current analysis with a saved snapshot.
- **`ContributingGenerator`** — Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml.
- **`ArchitectureGenerator`** — Generate docs/architecture.md — architecture overview with diagrams.
- **`ReadmeConfig`** — Configuration for README generation.
- **`DocsConfig`** — Configuration for docs/ generation.
- **`ExamplesConfig`** — Configuration for examples/ generation.
- **`SyncConfig`** — Configuration for synchronization.
- **`LLMConfig`** — Configuration for optional LLM-assisted documentation generation.
- **`Code2DocsConfig`** — Main configuration for code2docs.
- **`ProjectScanner`** — Wraps code2llm's ProjectAnalyzer with code2docs-specific defaults.
- **`DependencyInfo`** — Information about a project dependency.
- **`ProjectDependencies`** — All detected project dependencies.
- **`DependencyScanner`** — Scan and parse project dependency files.
- **`Endpoint`** — Represents a detected web endpoint.
- **`EndpointDetector`** — Detects web endpoints from decorator patterns in source code.
- **`DocstringInfo`** — Parsed docstring with sections.
- **`DocstringExtractor`** — Extract and parse docstrings from AnalysisResult.

### Functions

- `start_watcher(project_path, config)` — Start watching project for file changes and auto-resync docs.
- `generate_badges(project_name, badge_types, stats, deps)` — Generate shields.io badge Markdown strings.
- `generate_toc(markdown_content, max_depth)` — Generate a table of contents from Markdown headings.
- `extract_headings(content, max_depth)` — Extract headings from Markdown content.
- `generate_readme(project_path, output, sections, sync_markers)` — Convenience function to generate a README.
- `generate_docs(project_path, config)` — High-level function to generate all documentation.
- `main()` — code2docs — Auto-generate project documentation from source code.
- `generate(project_path, config_path, readme_only, sections)` — Generate documentation (default command).
- `sync(project_path, config_path, verbose, dry_run)` — Synchronize documentation with source code changes.
- `watch(project_path, config_path, verbose)` — Watch for file changes and auto-regenerate docs.
- `init(project_path, output)` — Initialize code2docs.yaml configuration file.
- `check(project_path, config_path, target)` — Health check — verify documentation completeness.
- `diff(project_path, config_path)` — Preview what would change without writing anything.
- `analyze_and_document(project_path, config)` — Convenience function: analyze a project in one call.


## Project Structure

📄 `__main__`
📦 `analyzers`
📄 `analyzers.dependency_scanner` (6 functions, 3 classes)
📄 `analyzers.docstring_extractor` (10 functions, 2 classes)
📄 `analyzers.endpoint_detector` (3 functions, 2 classes)
📄 `analyzers.project_scanner` (4 functions, 1 classes)
📄 `base` (3 functions, 2 classes)
📄 `cli` (14 functions, 1 classes)
📦 `code2docs` (1 functions)
📄 `config` (5 functions, 6 classes)
📄 `examples.advanced_usage`
📄 `examples.quickstart`
📦 `formatters`
📄 `formatters.badges` (2 functions)
📄 `formatters.markdown` (13 functions, 1 classes)
📄 `formatters.toc` (3 functions)
📦 `generators` (1 functions)
📄 `generators._registry_adapters` (24 functions, 12 classes)
📄 `generators._source_links` (6 functions, 1 classes)
📄 `generators.api_changelog_gen` (9 functions, 2 classes)
📄 `generators.api_reference_gen` (7 functions, 1 classes)
📄 `generators.architecture_gen` (10 functions, 1 classes)
📄 `generators.changelog_gen` (6 functions, 2 classes)
📄 `generators.config_docs_gen` (4 functions, 1 classes)
📄 `generators.contributing_gen` (8 functions, 1 classes)
📄 `generators.coverage_gen` (7 functions, 1 classes)
📄 `generators.depgraph_gen` (9 functions, 1 classes)
📄 `generators.examples_gen` (14 functions, 1 classes)
📄 `generators.getting_started_gen` (8 functions, 1 classes)
📄 `generators.mkdocs_gen` (4 functions, 1 classes)
📄 `generators.module_docs_gen` (9 functions, 1 classes)
📄 `generators.readme_gen` (18 functions, 1 classes)
📄 `llm_helper` (7 functions, 1 classes)
📄 `registry` (4 functions, 1 classes)
📦 `sync`
📄 `sync.differ` (7 functions, 2 classes)
📄 `sync.updater` (2 functions, 1 classes)
📄 `sync.watcher` (1 functions)

## Requirements



## Contributing

**Contributors:**
- Tom Softreck <tom@sapletta.com>
- Tom Sapletta <tom-sapletta-com@users.noreply.github.com>

We welcome contributions! Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/wronai/code2docs
cd code2docs

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## Documentation

- 📖 [Full Documentation](https://github.com/wronai/code2docs/tree/main/docs) — API reference, module docs, architecture
- 🚀 [Getting Started](https://github.com/wronai/code2docs/blob/main/docs/getting-started.md) — Quick start guide
- 📚 [API Reference](https://github.com/wronai/code2docs/blob/main/docs/api.md) — Complete API documentation
- 🔧 [Configuration](https://github.com/wronai/code2docs/blob/main/docs/configuration.md) — Configuration options
- 💡 [Examples](./examples) — Usage examples and code samples

### Generated Files

| Output | Description | Link |
|--------|-------------|------|
| `README.md` | Project overview (this file) | — |
| `docs/api.md` | Consolidated API reference | [View](./docs/api.md) |
| `docs/modules.md` | Module reference with metrics | [View](./docs/modules.md) |
| `docs/architecture.md` | Architecture with diagrams | [View](./docs/architecture.md) |
| `docs/dependency-graph.md` | Dependency graphs | [View](./docs/dependency-graph.md) |
| `docs/coverage.md` | Docstring coverage report | [View](./docs/coverage.md) |
| `docs/getting-started.md` | Getting started guide | [View](./docs/getting-started.md) |
| `docs/configuration.md` | Configuration reference | [View](./docs/configuration.md) |
| `docs/api-changelog.md` | API change tracking | [View](./docs/api-changelog.md) |
| `CONTRIBUTING.md` | Contribution guidelines | [View](./CONTRIBUTING.md) |
| `examples/` | Usage examples | [Browse](./examples) |
| `mkdocs.yml` | MkDocs configuration | — |

<!-- code2docs:end -->