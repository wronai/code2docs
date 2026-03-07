# code2docs — Architecture

> Auto-generated from 31 modules, 185 functions, 42 classes

## Module Dependency Graph

```mermaid
graph LR
    note[No internal dependencies detected]
```

## Architecture Layers

### Other

- `__main__`
- `code2docs`
- `generators`
- `generators._registry_adapters`
- `generators.architecture_gen`
- `generators.changelog_gen`
- `generators.coverage_gen`
- `generators.depgraph_gen`
- `generators.examples_gen`
- `generators.mkdocs_gen`
- `generators.module_docs_gen`
- `generators.readme_gen`
- `registry`
- `sync`
- `sync.differ`
- `sync.updater`
- `sync.watcher`

### Analysis

- `analyzers`
- `analyzers.dependency_scanner`
- `analyzers.docstring_extractor`
- `analyzers.endpoint_detector`
- `analyzers.project_scanner`

### Core

- `base`

### API / CLI

- `cli`
- `generators.api_changelog_gen`
- `generators.api_reference_gen`

### Config

- `config`

### Export / Output

- `formatters`
- `formatters.badges`
- `formatters.markdown`
- `formatters.toc`

## Key Classes

```mermaid
classDiagram
    class ModuleDocsGenerator {
        -__init__(self, config, result) None
        +generate_all(self) None
        -_generate_module(self, mod_name, mod_info) None
        -_render_header(self, mod_name, mod_info) None
        -_render_overview(self, mod_info) None
        -_render_classes_section(self, mod_name) None
        -_render_functions_section(self, mod_name) None
        -_render_dependencies_section(self, mod_info) None
        ... +9 more
    }
    class MarkdownFormatter {
        -__init__(self) None
        +heading(self, text, level) None
        +paragraph(self, text) None
        +blockquote(self, text) None
        +code_block(self, code, language) None
        +inline_code(self, text) None
        +bold(self, text) None
        +link(self, text, url) None
        ... +5 more
    }
    class ReadmeGenerator {
        -__init__(self, config, result) None
        +generate(self) None
        -_build_context(self, project_name) None
        -_calc_avg_complexity(self) None
        -_build_module_tree(self) None
        -_build_manual(self, project_name, sections) None
        -_build_overview_section(project_name, context) None
        -_build_install_section(_project_name, context) None
        ... +5 more
    }
    class ExamplesGenerator {
        -__init__(self, config, result) None
        +generate_all(self) None
        -_generate_basic_usage(self) None
        -_generate_import_section(self, project_name, public_classes) None
        -_generate_class_usage_section(self, public_classes) None
        -_generate_function_usage_section(self, public_functions) None
        -_generate_entry_point_examples(self) None
        -_generate_class_examples(self, classes) None
        ... +4 more
    }
    class ApiReferenceGenerator {
        -__init__(self, config, result) None
        +generate_all(self) None
        -_generate_index(self) None
        -_generate_module_api(self, mod_name, mod_info) None
        -_render_api_header(self, mod_name, mod_info) None
        -_render_api_classes(self, mod_name) None
        -_render_api_functions(self, mod_name) None
        -_render_api_imports(self, mod_info) None
        ... +3 more
    }
    class DocstringExtractor {
        +extract_all(self, result) None
        +parse(self, docstring) None
        -_extract_summary(lines) None
        -_classify_section(line) None
        -_parse_sections(self, lines, info) None
        -_parse_param_line(info, line) None
        -_parse_returns_line(info, line) None
        -_parse_raises_line(info, line) None
        ... +2 more
    }
    class DepGraphGenerator {
        -__init__(self, config, result) None
        +generate(self) None
        -_collect_edges(self) None
        -_extract_imports_from_file(file_path) None
        -_import_matches(imp, module) None
        -_render_mermaid(self, edges) None
        -_render_matrix(self, edges) None
        -_calc_degrees(edges) None
        ... +1 more
    }
    class ApiChangelogGenerator {
        -__init__(self, config, result) None
        +generate(self, project_path) None
        +save_snapshot(self, project_path) None
        -_build_snapshot(self) None
        -_load_snapshot(path) None
        -_diff(self, old, new) None
        -_diff_functions(old, new, changes) None
        -_diff_classes(old, new, changes) None
        ... +1 more
    }
    class CoverageGenerator {
        -__init__(self, config, result) None
        +generate(self) None
        -_render_summary(report) None
        -_render_per_module(self) None
        -_collect_module_stats(self) None
        -_format_coverage_table(stats) None
        -_render_undocumented(self) None
    }
    class Differ {
        -__init__(self, config) None
        +detect_changes(self, project_path) None
        +save_state(self, project_path) None
        -_load_state(self, state_path) None
        -_compute_state(self, project) None
        -_file_to_module(filepath, project) None
    }
    class ChangelogGenerator {
        -__init__(self, config, result) None
        +generate(self, project_path, max_entries) None
        -_get_git_log(self, project_path, max_entries) None
        -_classify_message(self, message) None
        -_group_by_type(self, entries) None
        -_render(self, grouped) None
    }
    class ArchitectureGenerator {
        -__init__(self, config, result) None
        +generate(self) None
        -_generate_module_graph(self) None
        -_generate_class_diagram(self) None
        -_detect_layers(self) None
        -_generate_metrics_table(self) None
    }
    class DependencyScanner {
        +scan(self, project_path) None
        -_parse_pyproject(self, path) None
        -_parse_pyproject_regex(self, path) None
        -_parse_setup_py(self, path) None
        -_parse_requirements_txt(self, path) None
        -_parse_dep_string(dep_str) None
    }
    class GeneratorRegistry {
        -__init__(self) None
        +add(self, generator) None
        +run_all(self, ctx) None
        +run_only(self, name, ctx) None
    }
    class MkDocsGenerator {
        -__init__(self, config, result) None
        +generate(self, docs_dir) None
        -_build_nav(self, docs_dir) None
        +write(self, output_path, content) None
    }
```

## Detected Patterns

- **recursion_analyze** (recursion) — confidence: 90%, functions: `analyzers.project_scanner.ProjectScanner.analyze`
- **state_machine_Differ** (state_machine) — confidence: 70%, functions: `sync.differ.Differ.__init__`, `sync.differ.Differ.detect_changes`, `sync.differ.Differ.save_state`, `sync.differ.Differ._load_state`, `sync.differ.Differ._compute_state`

## Entry Points

- `registry.GeneratorRegistry.__init__`
- `registry.GeneratorRegistry.add` — Add a generator instance to the registry.
- `registry.GeneratorRegistry.run_all` — Run every registered generator that should execute.
- `registry.GeneratorRegistry.run_only` — Run a single generator by name.
- `code2docs.__getattr__` — Lazy import heavy modules on first access.
- `sync.updater.Updater.__init__`
- `sync.updater.Updater.apply` — Regenerate documentation for changed modules.
- `sync.differ.ChangeInfo.__str__`
- `sync.differ.Differ.__init__`
- `sync.differ.Differ.detect_changes` — Compare current file hashes with saved state. Return list of changes.
- `sync.differ.Differ.save_state` — Save current file hashes as state.
- `sync.differ.Differ._load_state` — Load previous state from file.
- `sync.differ.Differ._compute_state` — Compute file hashes for all Python files in the project.
- `sync.differ.Differ._file_to_module` — Convert file path to module name.
- `formatters.markdown.MarkdownFormatter.__init__`
- `formatters.markdown.MarkdownFormatter.heading` — Add a heading.
- `formatters.markdown.MarkdownFormatter.paragraph` — Add a paragraph.
- `formatters.markdown.MarkdownFormatter.blockquote` — Add a blockquote.
- `formatters.markdown.MarkdownFormatter.code_block` — Add a fenced code block.
- `formatters.markdown.MarkdownFormatter.inline_code` — Return inline code string.
- `formatters.markdown.MarkdownFormatter.bold` — Return bold string.
- `formatters.markdown.MarkdownFormatter.link` — Return a Markdown link.
- `formatters.markdown.MarkdownFormatter.list_item` — Add a list item.
- `formatters.markdown.MarkdownFormatter.table` — Add a Markdown table.
- `formatters.markdown.MarkdownFormatter.separator` — Add a horizontal rule.
- `formatters.markdown.MarkdownFormatter.blank` — Add a blank line.
- `formatters.markdown.MarkdownFormatter.render` — Render accumulated Markdown to string.
- `formatters.toc.generate_toc` — Generate a table of contents from Markdown headings.
- `generators.readme_gen.ReadmeGenerator.__init__`
- `generators.readme_gen.ReadmeGenerator.generate` — Generate full README content.
- `generators.readme_gen.ReadmeGenerator._build_context` — Build template context from analysis result.
- `generators.readme_gen.ReadmeGenerator._calc_avg_complexity` — Calculate average cyclomatic complexity.
- `generators.readme_gen.ReadmeGenerator._build_module_tree` — Build text-based module tree.
- `generators.readme_gen.ReadmeGenerator._build_manual` — Fallback manual README builder (orchestrator).
- `generators.readme_gen.ReadmeGenerator._build_overview_section` — Build overview section with badges and stats.
- `generators.readme_gen.ReadmeGenerator._build_install_section` — Build installation section from dependencies.
- `generators.readme_gen.ReadmeGenerator._build_quickstart_section` — Build quick start section from entry points.
- `generators.readme_gen.ReadmeGenerator._build_api_section` — Build API overview section with classes and functions.
- `generators.readme_gen.ReadmeGenerator._build_structure_section` — Build project structure section from module tree.
- `generators.readme_gen.ReadmeGenerator._build_endpoints_section` — Build endpoints section from detected routes.
- `generators.readme_gen.ReadmeGenerator.write` — Write README, respecting sync markers if existing file has them.
- `generators.readme_gen.generate_readme` — Convenience function to generate a README.
- `generators.coverage_gen.CoverageGenerator.__init__`
- `generators.coverage_gen.CoverageGenerator.generate` — Generate coverage.md content.
- `generators.coverage_gen.CoverageGenerator._render_summary` — Render overall coverage summary.
- `generators.coverage_gen.CoverageGenerator._render_per_module` — Render per-module coverage table (orchestrator).
- `generators.coverage_gen.CoverageGenerator._collect_module_stats` — Collect coverage data per module.
- `generators.coverage_gen.CoverageGenerator._format_coverage_table` — Format coverage stats as a Markdown table.
- `generators.coverage_gen.CoverageGenerator._render_undocumented` — List all undocumented public functions and classes.
- `generators.depgraph_gen.DepGraphGenerator.__init__`
- `generators.depgraph_gen.DepGraphGenerator.generate` — Generate dependency-graph.md content.
- `generators.depgraph_gen.DepGraphGenerator._collect_edges` — Build directed edges from module imports.
- `generators.depgraph_gen.DepGraphGenerator._extract_imports_from_file` — Parse source file AST to extract import targets.
- `generators.depgraph_gen.DepGraphGenerator._import_matches` — Check if an import string refers to a known module.
- `generators.depgraph_gen.DepGraphGenerator._render_mermaid` — Render Mermaid graph from edges.
- `generators.depgraph_gen.DepGraphGenerator._render_matrix` — Render a coupling matrix as a Markdown table.
- `generators.depgraph_gen.DepGraphGenerator._calc_degrees` — Calculate in-degree and out-degree per module.
- `generators.depgraph_gen.DepGraphGenerator._render_degree_table` — Render fan-in/fan-out table.
- `base.BaseGenerator.__init__`
- `base.BaseGenerator.should_run` — Return True if this generator should execute.
- `base.BaseGenerator.run` — Execute generation and write output.
- `generators.changelog_gen.ChangelogGenerator.__init__`
- `generators.changelog_gen.ChangelogGenerator.generate` — Generate changelog content from git log.
- `generators.changelog_gen.ChangelogGenerator._get_git_log` — Extract git log entries.
- `generators.changelog_gen.ChangelogGenerator._classify_message` — Classify commit message by conventional commit type.
- `generators.changelog_gen.ChangelogGenerator._group_by_type` — Group entries by type.
- `generators.changelog_gen.ChangelogGenerator._render` — Render grouped changelog to Markdown.
- `generators.generate_docs` — High-level function to generate all documentation.
- `generators.api_reference_gen.ApiReferenceGenerator.__init__`
- `generators.api_reference_gen.ApiReferenceGenerator.generate_all` — Generate API reference for all modules. Returns {filename: content}.
- `generators.api_reference_gen.ApiReferenceGenerator._generate_index` — Generate API index page.
- `generators.api_reference_gen.ApiReferenceGenerator._generate_module_api` — Generate API reference for a single module (orchestrator).
- `generators.api_reference_gen.ApiReferenceGenerator._render_api_header` — Render module header with source info.
- `generators.api_reference_gen.ApiReferenceGenerator._render_api_classes` — Render classes with their method signatures.
- `generators.api_reference_gen.ApiReferenceGenerator._render_api_functions` — Render standalone functions with signatures and complexity.
- `generators.api_reference_gen.ApiReferenceGenerator._render_api_imports` — Render module imports list.
- `generators.api_reference_gen.ApiReferenceGenerator._get_class_methods` — Get FunctionInfo objects for class methods.
- `generators.api_reference_gen.ApiReferenceGenerator._format_signature` — Format a function signature string.
- `generators.api_reference_gen.ApiReferenceGenerator.write_all` — Write all generated API reference files.
- `generators.module_docs_gen.ModuleDocsGenerator.__init__`
- `generators.module_docs_gen.ModuleDocsGenerator.generate_all` — Generate documentation for all modules. Returns {filename: content}.
- `generators.module_docs_gen.ModuleDocsGenerator._generate_module` — Generate detailed documentation for a single module (orchestrator).
- `generators.module_docs_gen.ModuleDocsGenerator._render_header` — Render module title and source metadata.
- `generators.module_docs_gen.ModuleDocsGenerator._render_overview` — Render module overview from docstring.
- `generators.module_docs_gen.ModuleDocsGenerator._render_classes_section` — Render classes and their method tables.
- `generators.module_docs_gen.ModuleDocsGenerator._render_functions_section` — Render standalone functions with signatures and call info.
- `generators.module_docs_gen.ModuleDocsGenerator._render_dependencies_section` — Render imports split into internal and stdlib.
- `generators.module_docs_gen.ModuleDocsGenerator._render_metrics_section` — Render metrics summary table.
- `generators.module_docs_gen.ModuleDocsGenerator._count_file_lines` — Count lines in source file.
- `generators.module_docs_gen.ModuleDocsGenerator._calc_module_avg_cc` — Calculate average cyclomatic complexity for module functions.
- `generators.module_docs_gen.ModuleDocsGenerator._get_module_docstring` — Try to extract module-level docstring.
- `generators.module_docs_gen.ModuleDocsGenerator._get_module_classes`
- `generators.module_docs_gen.ModuleDocsGenerator._get_module_functions`
- `generators.module_docs_gen.ModuleDocsGenerator._get_class_methods`
- `generators.module_docs_gen.ModuleDocsGenerator._get_module_metrics`
- `generators.module_docs_gen.ModuleDocsGenerator.write_all` — Write all generated module docs.
- `generators.mkdocs_gen.MkDocsGenerator.__init__`
- `generators.mkdocs_gen.MkDocsGenerator.generate` — Generate mkdocs.yml content.
- `generators.mkdocs_gen.MkDocsGenerator._build_nav` — Build navigation structure from docs tree and analysis.
- `generators.mkdocs_gen.MkDocsGenerator.write` — Write mkdocs.yml file.
- `generators.examples_gen.ExamplesGenerator.__init__`
- `generators.examples_gen.ExamplesGenerator.generate_all` — Generate all example files. Returns {filename: content}.
- `generators.examples_gen.ExamplesGenerator._generate_basic_usage` — Generate basic_usage.py example (orchestrator).
- `generators.examples_gen.ExamplesGenerator._generate_import_section` — Generate import statements for the example.
- `generators.examples_gen.ExamplesGenerator._generate_class_usage_section` — Generate class instantiation and method call examples.
- `generators.examples_gen.ExamplesGenerator._generate_function_usage_section` — Generate standalone function call examples.
- `generators.examples_gen.ExamplesGenerator._generate_entry_point_examples` — Generate examples based on entry points.
- `generators.examples_gen.ExamplesGenerator._generate_class_examples` — Generate examples for major classes.
- `generators.examples_gen.ExamplesGenerator._get_major_classes` — Get classes with most methods (likely most important).
- `generators.examples_gen.ExamplesGenerator._get_init_args` — Get __init__ args for a class.
- `generators.examples_gen.ExamplesGenerator._get_public_methods` — Get public methods of a class.
- `generators.examples_gen.ExamplesGenerator.write_all` — Write all generated example files.
- `generators._registry_adapters.ReadmeGeneratorAdapter.should_run`
- `generators._registry_adapters.ReadmeGeneratorAdapter.run`
- `generators._registry_adapters.ApiReferenceAdapter.should_run`
- `generators._registry_adapters.ApiReferenceAdapter.run`
- `generators._registry_adapters.ModuleDocsAdapter.should_run`
- `generators._registry_adapters.ModuleDocsAdapter.run`
- `generators._registry_adapters.ArchitectureAdapter.should_run`
- `generators._registry_adapters.ArchitectureAdapter.run`
- `generators._registry_adapters.DepGraphAdapter.should_run`
- `generators._registry_adapters.DepGraphAdapter.run`
- `generators._registry_adapters.CoverageAdapter.should_run`
- `generators._registry_adapters.CoverageAdapter.run`
- `generators._registry_adapters.ApiChangelogAdapter.should_run`
- `generators._registry_adapters.ApiChangelogAdapter.run`
- `generators._registry_adapters.ExamplesAdapter.should_run`
- `generators._registry_adapters.ExamplesAdapter.run`
- `generators._registry_adapters.MkDocsAdapter.should_run`
- `generators._registry_adapters.MkDocsAdapter.run`
- `generators.architecture_gen.ArchitectureGenerator.__init__`
- `generators.architecture_gen.ArchitectureGenerator.generate` — Generate architecture documentation.
- `generators.architecture_gen.ArchitectureGenerator._generate_module_graph` — Generate Mermaid module dependency graph.
- `generators.architecture_gen.ArchitectureGenerator._generate_class_diagram` — Generate Mermaid class diagram for key classes.
- `generators.architecture_gen.ArchitectureGenerator._detect_layers` — Detect architectural layers from module names.
- `generators.architecture_gen.ArchitectureGenerator._generate_metrics_table` — Generate metrics summary table.
- `generators.api_changelog_gen.ApiChangelogGenerator.__init__`
- `generators.api_changelog_gen.ApiChangelogGenerator.generate` — Generate api-changelog.md by comparing with previous snapshot.
- `generators.api_changelog_gen.ApiChangelogGenerator.save_snapshot` — Save current API state as snapshot for future diffs.
- `generators.api_changelog_gen.ApiChangelogGenerator._build_snapshot` — Build a JSON-serializable snapshot of current API.
- `generators.api_changelog_gen.ApiChangelogGenerator._load_snapshot` — Load previous snapshot, or None if not found.
- `generators.api_changelog_gen.ApiChangelogGenerator._diff` — Compute list of API changes between old and new snapshots.
- `generators.api_changelog_gen.ApiChangelogGenerator._diff_functions` — Diff function signatures.
- `generators.api_changelog_gen.ApiChangelogGenerator._diff_classes` — Diff class definitions.
- `generators.api_changelog_gen.ApiChangelogGenerator._render` — Render changelog as Markdown.
- `cli.DefaultGroup.parse_args`
- `cli.main` — code2docs — Auto-generate project documentation from source code.
- `cli.generate` — Generate documentation (default command).
- `cli.sync` — Synchronize documentation with source code changes.
- `cli.watch` — Watch for file changes and auto-regenerate docs.
- `cli.init` — Initialize code2docs.yaml configuration file.
- `config.Code2DocsConfig.from_yaml` — Load configuration from code2docs.yaml.
- `config.Code2DocsConfig.to_yaml` — Save configuration to YAML file.
- `analyzers.project_scanner.ProjectScanner.__init__`
- `analyzers.project_scanner.ProjectScanner._build_llm_config` — Create code2llm Config tuned for documentation generation.
- `analyzers.project_scanner.analyze_and_document` — Convenience function: analyze a project in one call.
- `analyzers.docstring_extractor.DocstringExtractor.extract_all` — Extract docstrings for all functions and classes.
- `analyzers.docstring_extractor.DocstringExtractor.parse` — Parse a docstring into structured sections (orchestrator).
- `analyzers.docstring_extractor.DocstringExtractor._extract_summary` — Extract the first-line summary.
- `analyzers.docstring_extractor.DocstringExtractor._classify_section` — Classify a line as a section header, or return None.
- `analyzers.docstring_extractor.DocstringExtractor._parse_sections` — Walk remaining lines, dispatching content to the right section.
- `analyzers.docstring_extractor.DocstringExtractor._parse_param_line` — Parse a single param line: 'name: description'.
- `analyzers.docstring_extractor.DocstringExtractor._parse_returns_line` — Parse a returns line.
- `analyzers.docstring_extractor.DocstringExtractor._parse_raises_line` — Parse a raises line.
- `analyzers.docstring_extractor.DocstringExtractor._parse_examples_line` — Parse an examples line.
- `analyzers.docstring_extractor.DocstringExtractor.coverage_report` — Calculate docstring coverage statistics.
- `analyzers.dependency_scanner.DependencyScanner.scan` — Scan project for dependency information.
- `analyzers.dependency_scanner.DependencyScanner._parse_pyproject` — Parse pyproject.toml for dependencies.
- `analyzers.dependency_scanner.DependencyScanner._parse_pyproject_regex` — Fallback regex-based pyproject.toml parser.
- `analyzers.dependency_scanner.DependencyScanner._parse_setup_py` — Parse setup.py for dependencies (regex-based, no exec).
- `analyzers.dependency_scanner.DependencyScanner._parse_requirements_txt` — Parse requirements.txt.
- `analyzers.dependency_scanner.DependencyScanner._parse_dep_string` — Parse a dependency string like 'package>=1.0'.
- `analyzers.endpoint_detector.EndpointDetector.detect` — Detect all endpoints from the analysis result.
- `analyzers.endpoint_detector.EndpointDetector._parse_decorator` — Try to parse a route decorator string.
- `analyzers.endpoint_detector.EndpointDetector._scan_django_urls` — Scan urls.py files for Django URL patterns.

## Metrics Summary

| Metric | Value |
|--------|-------|
| Modules | 31 |
| Functions | 185 |
| Classes | 42 |
| CFG Nodes | 1106 |
| Patterns | 2 |
| Avg Complexity | 3.8 |
| Analysis Time | 0.98s |
