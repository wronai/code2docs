# `base`

> Source: `/home/tom/github/wronai/code2docs/code2docs/base.py`

## Classes

### `BaseGenerator`

Inherits from: `ABC`

Abstract base for all documentation generators.

Subclasses must define ``name`` and implement ``should_run`` / ``run``.
Adding a new generator requires only creating a subclass and registering it
with the :class:`GeneratorRegistry`; no changes to ``cli.py`` needed.

#### Methods

- `__init__(self, config, result)`
- `should_run(self)` — Return True if this generator should execute.
- `run(self, ctx)` — Execute generation and write output.

### `GenerateContext`

Shared context passed to all generators during a run.
