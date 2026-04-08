# code2docs — API Changelog

> 14 change(s) detected

## Added

- 🆕 **class** `code2docs.generators._registry_adapters.IndexHtmlAdapter`
- 🆕 **method** `run(self, ctx)`
- 🆕 **method** `should_run(self)`
- 🆕 **class** `code2docs.generators._registry_adapters.OrgReadmeAdapter`
- 🆕 **method** `run(self, ctx)`
- 🆕 **method** `should_run(self)`
- 🆕 **function** `parse_gitignore(project_path)`
- 🆕 **class** `code2docs.generators.org_readme_gen.OrgReadmeGenerator`
- 🆕 **method** `generate(self)`
- 🆕 **method** `write(self, output_path, content)`

## Changed

- ✏️ **class** `code2docs.analyzers.dependency_scanner.DependencyScanner`
  - added methods: code2docs.analyzers.dependency_scanner.DependencyScanner._detect_version, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_cargo_toml, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_go_mod, code2docs.analyzers.dependency_scanner.DependencyScanner._parse_package_json
- ✏️ **function** `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run, llm_model, org_name)`
  - signature changed
  - was: `generate(project_path, config_path, readme_only, sections, output, verbose, dry_run, llm_model)`
- ✏️ **class** `code2docs.generators.examples_gen.ExamplesGenerator`
  - added methods: code2docs.generators.examples_gen.ExamplesGenerator._get_example_value
- ✏️ **class** `code2docs.generators.mkdocs_gen.MkDocsGenerator`
  - added methods: code2docs.generators.mkdocs_gen.MkDocsGenerator._read_pyproject_mkdocs
