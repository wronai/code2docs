# code2docs — Docstring Coverage

🟢 **Overall coverage: 80.4%**

| Category | Documented | Total | Coverage |
|----------|-----------|-------|----------|
| Functions | 240 | 298 | 80.5% |
| Classes | 48 | 60 | 80.0% |

## Per-Module Breakdown

| Module | Functions | Classes | Coverage |
|--------|-----------|---------|----------|
| `code2docs` | 1/1 | 0/0 | 🟢 100% |
| `code2docs.__main__` | 0/0 | 0/0 | 🟢 100% |
| `code2docs.analyzers` | 0/0 | 0/0 | 🟢 100% |
| `code2docs.analyzers.dependency_scanner` | 0/0 | 3/3 | 🟢 100% |
| `code2docs.analyzers.docstring_extractor` | 0/0 | 2/2 | 🟢 100% |
| `code2docs.analyzers.endpoint_detector` | 0/0 | 2/2 | 🟢 100% |
| `code2docs.analyzers.project_scanner` | 1/1 | 1/1 | 🟢 100% |
| `code2docs.base` | 0/0 | 2/2 | 🟢 100% |
| `code2docs.cli` | 13/13 | 1/1 | 🟢 100% |
| `code2docs.config` | 0/0 | 7/7 | 🟢 100% |
| `code2docs.examples.advanced_usage` | 0/0 | 0/0 | 🟢 100% |
| `code2docs.examples.quickstart` | 0/0 | 0/0 | 🟢 100% |
| `code2docs.formatters` | 0/0 | 0/0 | 🟢 100% |
| `code2docs.formatters.badges` | 2/2 | 0/0 | 🟢 100% |
| `code2docs.formatters.markdown` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.formatters.toc` | 3/3 | 0/0 | 🟢 100% |
| `code2docs.generators` | 1/1 | 0/0 | 🟢 100% |
| `code2docs.generators._registry_adapters` | 0/0 | 3/15 | 🔴 20% |
| `code2docs.generators._source_links` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.api_changelog_gen` | 0/0 | 2/2 | 🟢 100% |
| `code2docs.generators.api_reference_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.architecture_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.changelog_gen` | 0/0 | 2/2 | 🟢 100% |
| `code2docs.generators.code2llm_gen` | 2/2 | 1/1 | 🟢 100% |
| `code2docs.generators.config_docs_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.contributing_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.coverage_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.depgraph_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.examples_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.getting_started_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.mkdocs_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.module_docs_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.org_readme_gen` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.generators.readme_gen` | 1/1 | 1/1 | 🟢 100% |
| `code2docs.llm_helper` | 1/1 | 1/1 | 🟢 100% |
| `code2docs.registry` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.sync` | 0/0 | 0/0 | 🟢 100% |
| `code2docs.sync.differ` | 0/0 | 2/2 | 🟢 100% |
| `code2docs.sync.updater` | 0/0 | 1/1 | 🟢 100% |
| `code2docs.sync.watcher` | 1/1 | 0/0 | 🟢 100% |
| `docs.examples.advanced_usage` | 0/0 | 0/0 | 🟢 100% |
| `docs.examples.quickstart` | 0/0 | 0/0 | 🟢 100% |
| `examples.01_cli_usage` | 2/2 | 0/0 | 🟢 100% |
| `examples.02_configuration` | 4/4 | 0/0 | 🟢 100% |
| `examples.03_programmatic_api` | 5/5 | 0/0 | 🟢 100% |
| `examples.04_sync_and_watch` | 6/6 | 0/0 | 🟢 100% |
| `examples.05_custom_generators` | 1/1 | 3/3 | 🟢 100% |
| `examples.06_formatters` | 5/5 | 0/0 | 🟢 100% |
| `examples.07_web_frameworks` | 5/5 | 0/0 | 🟢 100% |
| `examples.advanced_usage` | 0/0 | 0/0 | 🟢 100% |
| `examples.basic_usage` | 0/0 | 0/0 | 🟢 100% |
| `examples.class_examples` | 0/0 | 0/0 | 🟢 100% |
| `examples.entry_points` | 0/0 | 0/0 | 🟢 100% |
| `examples.quickstart` | 0/0 | 0/0 | 🟢 100% |
| `project` | 0/0 | 0/0 | 🟢 100% |

## Undocumented Items

- `code2docs.generators._registry_adapters.ApiChangelogAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:111)
- `code2docs.generators._registry_adapters.ApiReferenceAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:34)
- `code2docs.generators._registry_adapters.ArchitectureAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:66)
- `code2docs.generators._registry_adapters.ConfigDocsAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:174)
- `code2docs.generators._registry_adapters.ContributingAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:190)
- `code2docs.generators._registry_adapters.CoverageAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:96)
- `code2docs.generators._registry_adapters.DepGraphAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:81)
- `code2docs.generators._registry_adapters.ExamplesAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:127)
- `code2docs.generators._registry_adapters.GettingStartedAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:158)
- `code2docs.generators._registry_adapters.MkDocsAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:143)
- `code2docs.generators._registry_adapters.ModuleDocsAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:50)
- `code2docs.generators._registry_adapters.ReadmeGeneratorAdapter` (/home/tom/github/semcod/code2docs/code2docs/generators/_registry_adapters.py:11)
