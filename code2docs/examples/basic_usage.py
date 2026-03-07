"""Basic usage of code2docs."""

from registry import GeneratorRegistry
from sync.updater import Updater
from sync.differ import ChangeInfo
from sync.differ import Differ
from formatters.markdown import MarkdownFormatter
from sync.watcher import start_watcher
from formatters.badges import generate_badges
from formatters.toc import generate_toc
from formatters.toc import extract_headings
from generators.readme_gen import generate_readme

# Create GeneratorRegistry instance
obj = GeneratorRegistry()

result = obj.add(generator=...)
result = obj.run_all(ctx=...)
result = obj.run_only(name=..., ctx=...)

# Standalone functions
result = start_watcher(project_path=..., config=...)
result = generate_badges(project_name=..., badge_types=..., stats=..., deps=...)
result = generate_toc(markdown_content=..., max_depth=...)
result = extract_headings(content=..., max_depth=...)
result = generate_readme(project_path=..., output=..., sections=..., sync_markers=...)
