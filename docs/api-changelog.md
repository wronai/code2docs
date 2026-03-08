# code2docs — API Changelog

> 10 change(s) detected

## Added

- 🆕 **class** `generators._registry_adapters.OrgReadmeAdapter`
- 🆕 **method** `run(self, ctx)`
- 🆕 **method** `should_run(self)`
- 🆕 **class** `generators.org_readme_gen.OrgReadmeGenerator`
- 🆕 **method** `generate(self)`
- 🆕 **method** `write(self, output_path, content)`

## Changed

- ✏️ **class** `analyzers.dependency_scanner.DependencyScanner`
  - added methods: analyzers.dependency_scanner.DependencyScanner._detect_version
- ✏️ **function** `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run, llm_model, org_name)`
  - signature changed
  - was: `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run, llm_model)`
- ✏️ **class** `generators.examples_gen.ExamplesGenerator`
  - added methods: generators.examples_gen.ExamplesGenerator._get_example_value
- ✏️ **class** `generators.mkdocs_gen.MkDocsGenerator`
  - added methods: generators.mkdocs_gen.MkDocsGenerator._read_pyproject_mkdocs
