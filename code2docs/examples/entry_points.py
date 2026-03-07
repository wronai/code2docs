"""Entry point examples for code2docs."""

from formatters.toc import generate_toc

# Generate a table of contents from Markdown headings.
result = generate_toc(markdown_content=..., max_depth=...)

from generators.readme_gen import generate_readme

# Convenience function to generate a README.
result = generate_readme(project_path=..., output=..., sections=..., sync_markers=...)

from generators import generate_docs

# High-level function to generate all documentation.
result = generate_docs(project_path=..., config=...)

from cli import main

# code2docs — Auto-generate project documentation from source code.
result = main()

from cli import generate

# Generate documentation (default command).
result = generate(project_path=..., config_path=..., readme_only=..., sections=...)

from cli import sync

# Synchronize documentation with source code changes.
result = sync(project_path=..., config_path=..., verbose=..., dry_run=...)

from cli import watch

# Watch for file changes and auto-regenerate docs.
result = watch(project_path=..., config_path=..., verbose=...)

from cli import init

# Initialize code2docs.yaml configuration file.
result = init(project_path=..., output=...)
