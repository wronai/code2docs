"""Configuration documentation generator."""

from dataclasses import fields, MISSING
from typing import Any

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


class ConfigDocsGenerator:
    """Generate docs/configuration.md from Code2DocsConfig dataclass."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self) -> str:
        """Generate configuration.md content."""
        project = self.config.project_name or "Project"
        lines = [
            f"# {project} — Configuration Reference\n",
            "> All options for `code2docs.yaml`\n",
            self._render_section("Top-level", Code2DocsConfig),
        ]
        # Nested config sections
        for f in fields(Code2DocsConfig):
            val = getattr(self.config, f.name)
            if hasattr(val, "__dataclass_fields__"):
                lines.append("")
                lines.append(self._render_section(f"`{f.name}`", type(val)))
        lines.append("")
        lines.append(self._render_example())
        return "\n".join(lines)

    @staticmethod
    def _render_section(title: str, cls: type) -> str:
        """Render a dataclass as a Markdown table."""
        lines = [
            f"## {title}\n",
            "| Option | Type | Default | Description |",
            "|--------|------|---------|-------------|",
        ]
        for f in fields(cls):
            type_str = getattr(f.type, "__name__", str(f.type))
            default = f.default if f.default is not MISSING else ""
            if f.default_factory is not MISSING:
                default = f"`{f.default_factory.__name__}()`"
            doc = ""
            if f.metadata and "help" in f.metadata:
                doc = f.metadata["help"]
            lines.append(f"| `{f.name}` | `{type_str}` | `{default}` | {doc} |")
        return "\n".join(lines)

    def _render_example(self) -> str:
        """Render an example code2docs.yaml."""
        lines = [
            "## Example `code2docs.yaml`\n",
            "```yaml",
            f"project_name: {self.config.project_name or 'my-project'}",
            f"source: {self.config.source}",
            f"output: {self.config.output}",
            f"readme_output: {self.config.readme_output}",
            "verbose: false",
            "",
            "readme:",
            "  sections:",
            "    - overview",
            "    - install",
            "    - quickstart",
            "    - api",
            "    - structure",
            "  sync_markers: true",
            "",
            "docs:",
            f"  api_reference: {self.config.docs.api_reference}",
            f"  module_docs: {self.config.docs.module_docs}",
            f"  architecture: {self.config.docs.architecture}",
            "",
            "examples:",
            f"  auto_generate: {self.config.examples.auto_generate}",
            "```",
        ]
        return "\n".join(lines)
