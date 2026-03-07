"""Getting Started guide generator."""

from typing import List, Optional

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig
from ..analyzers.dependency_scanner import DependencyScanner


class GettingStartedGenerator:
    """Generate docs/getting-started.md from entry points and dependencies."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self) -> str:
        """Generate getting-started.md content."""
        project = self.config.project_name or "Project"
        lines = [
            f"# Getting Started with {project}\n",
            self._render_prerequisites(),
            "",
            self._render_installation(),
            "",
            self._render_first_usage(),
            "",
            self._render_next_steps(),
            "",
        ]
        return "\n".join(lines)

    def _render_prerequisites(self) -> str:
        """Render prerequisites section."""
        dep_scanner = DependencyScanner()
        deps = dep_scanner.scan(self.result.project_path)
        py_ver = deps.python_version or ">=3.9"
        lines = [
            "## Prerequisites\n",
            f"- Python {py_ver}",
            "- pip (or your preferred package manager)",
        ]
        if deps.dependencies:
            lines.append(f"- {len(deps.dependencies)} dependencies (installed automatically)")
        return "\n".join(lines)

    def _render_installation(self) -> str:
        """Render installation section."""
        dep_scanner = DependencyScanner()
        deps = dep_scanner.scan(self.result.project_path)
        cmd = deps.install_command or f"pip install {self.config.project_name or '.'}"
        lines = [
            "## Installation\n",
            "```bash",
            cmd,
            "```\n",
            "To install from source:\n",
            "```bash",
            "git clone <repository-url>",
            f"cd {self.config.project_name or 'project'}",
            "pip install -e .",
            "```",
        ]
        return "\n".join(lines)

    def _render_first_usage(self) -> str:
        """Render first usage example from entry points."""
        lines = ["## Your First Usage\n"]
        entry_points = self.result.entry_points or []

        if entry_points:
            lines.append("```python")
            for ep in entry_points[:3]:
                lines.append(f"from {ep.rsplit('.', 1)[0]} import {ep.rsplit('.', 1)[-1]}")
            lines.append("")
            lines.append(f"# Call the main entry point")
            lines.append(f"result = {entry_points[0].rsplit('.', 1)[-1]}()")
            lines.append("```")
        else:
            # Fallback: show module import
            top_modules = self._get_top_level_modules()
            if top_modules:
                lines.append("```python")
                lines.append(f"import {top_modules[0]}")
                lines.append("```")
            else:
                lines.append("```python")
                lines.append(f"import {self.config.project_name or 'project'}")
                lines.append("```")

        return "\n".join(lines)

    def _render_next_steps(self) -> str:
        """Render next steps with links to other docs."""
        lines = [
            "## What's Next\n",
            "- 📖 [API Reference](api/index.md) — Full function and class documentation",
            "- 🏗️ [Architecture](architecture.md) — System design and module relationships",
            "- 📊 [Coverage Report](coverage.md) — Docstring coverage analysis",
            "- 🔗 [Dependency Graph](dependency-graph.md) — Module dependency visualization",
        ]
        return "\n".join(lines)

    def _get_top_level_modules(self) -> List[str]:
        """Get top-level package names."""
        top = set()
        for mod_name in self.result.modules:
            parts = mod_name.split(".")
            if len(parts) >= 1:
                top.add(parts[0])
        return sorted(top)
