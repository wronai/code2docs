# `generators.coverage_gen`

> Source: `/home/tom/github/wronai/code2docs/code2docs/generators/coverage_gen.py`

## Classes

### `CoverageGenerator`

Generate docs/coverage.md — docstring coverage report.

#### Methods

- `__init__(self, config, result)`
- `generate(self)` — Generate coverage.md content.
- `_render_summary(report)` — Render overall coverage summary.
- `_render_per_module(self)` — Render per-module coverage table (orchestrator).
- `_collect_module_stats(self)` — Collect coverage data per module. ⚠️ CC=12
- `_format_coverage_table(stats)` — Format coverage stats as a Markdown table.
- `_render_undocumented(self)` — List all undocumented public functions and classes.
