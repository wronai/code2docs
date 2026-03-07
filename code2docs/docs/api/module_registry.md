# `registry`

> Source: `/home/tom/github/wronai/code2docs/code2docs/registry.py`

## Classes

### `GeneratorRegistry`

Registry of documentation generators.

Generators register themselves via :meth:`register`. The CLI calls
:meth:`run_all` which iterates registered generators in priority order.

#### Methods

- `__init__(self)`
- `add(self, generator)` — Add a generator instance to the registry.
- `run_all(self, ctx)` — Run every registered generator that should execute.
- `run_only(self, name, ctx)` — Run a single generator by name.
