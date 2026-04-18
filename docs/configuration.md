# code2docs — Configuration Reference

> All options for `code2docs.yaml`

## Top-level

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `project_name` | `str` | "" | Name of the project (used in headings and badges) |
| `source` | `str` | ./ | Root directory to analyze |
| `output` | `str` | ./docs/ | Output directory for generated docs |
| `readme_output` | `str` | ./README.md | Path for the generated README file |
| `repo_url` | `str` | "" |  |
| `org_name` | `str` | "" |  |
| `readme` | `ReadmeConfig` | *see `readme` section* |  |
| `docs` | `DocsConfig` | *see `docs` section* |  |
| `examples` | `ExamplesConfig` | *see `examples` section* |  |
| `sync` | `SyncConfig` | *see `sync` section* |  |
| `llm` | `LLMConfig` | *see `llm` section* |  |
| `code2llm` | `Code2LlmConfig` | *see `code2llm` section* |  |
| `verbose` | `bool` | false | Print detailed analysis info during generation |
| `exclude_tests` | `bool` | true | Exclude test files from analysis |
| `skip_private` | `bool` | false | Skip private functions/classes in output |

## `code2llm`

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `enabled` | `bool` | true | Enable LLM-assisted documentation generation |
| `formats` | `List` | all |  |
| `strategy` | `str` | standard | Sync strategy: `markers`, `full`, or `git-diff` |
| `output_dir` | `str` | project |  |
| `chunk` | `bool` | false |  |
| `no_png` | `bool` | true |  |
| `max_depth` | `int` | 6 |  |
| `exclude_patterns` | `List` | venv, .venv, env, .env, node_modules, bower_components, __pycache__, .pytest_cache, .mypy_cache, .git, .hg, .svn, dist, build, target, out, .tox, .eggs, *.egg-info, vendor, third_party, third-party, site-packages, lib/python* |  |

