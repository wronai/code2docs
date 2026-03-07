"""Entry point examples for code2docs."""

from registry import __init__

# Call entry point: __init__
result = __init__(self=...)

from registry import add

# Call entry point: add
# Add a generator instance to the registry.
result = add(self=..., generator=...)

from registry import run_all

# Call entry point: run_all
# Run every registered generator that should execute.
result = run_all(self=..., ctx=...)

from registry import run_only

# Call entry point: run_only
# Run a single generator by name.
result = run_only(self=..., name=..., ctx=...)

from code2docs import __getattr__

# Call entry point: __getattr__
# Lazy import heavy modules on first access.
result = __getattr__(name=...)
