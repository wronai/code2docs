"""MkDocs configuration generator — auto-generate mkdocs.yml from docs tree."""

from pathlib import Path
from typing import Dict, List, Optional

import yaml

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig


class MkDocsGenerator:
    """Generate mkdocs.yml from the docs/ directory structure."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self, docs_dir: Optional[str] = None) -> str:
        """Generate mkdocs.yml content."""
        project_name = self.config.project_name or "Project"
        nav = self._build_nav(docs_dir)

        data = {
            "site_name": f"{project_name} Documentation",
            "theme": {"name": "material"},
            "nav": nav,
            "markdown_extensions": [
                "admonition",
                "pymdownx.highlight",
                "pymdownx.superfences",
                {"pymdownx.superfences": {
                    "custom_fences": [{
                        "name": "mermaid",
                        "class": "mermaid",
                        "format": "!!python/name:pymdownx.superfences.fence_code_format",
                    }]
                }},
            ],
        }
        return yaml.dump(data, default_flow_style=False, sort_keys=False)

    def _build_nav(self, docs_dir: Optional[str] = None) -> List:
        """Build navigation structure from docs tree and analysis."""
        nav: List = [{"Home": "index.md"}]

        if self.config.docs.architecture:
            nav.append({"Architecture": "architecture.md"})

        # API reference
        if self.config.docs.api_reference:
            api_items = [{"Overview": "api/index.md"}]
            for mod_name in sorted(self.result.modules.keys()):
                safe = mod_name.replace(".", "_").replace("/", "_")
                api_items.append({mod_name: f"api/module_{safe}.md"})
            nav.append({"API Reference": api_items})

        # Module docs
        if self.config.docs.module_docs:
            mod_items = []
            for mod_name in sorted(self.result.modules.keys()):
                safe = mod_name.replace(".", "_").replace("/", "_")
                mod_items.append({mod_name: f"modules/{safe}.md"})
            if mod_items:
                nav.append({"Modules": mod_items})

        # Extra pages
        nav.append({"Dependency Graph": "dependency-graph.md"})
        nav.append({"Coverage": "coverage.md"})

        if self.config.docs.changelog:
            nav.append({"Changelog": "changelog.md"})

        return nav

    def write(self, output_path: str, content: str) -> None:
        """Write mkdocs.yml file."""
        Path(output_path).write_text(content, encoding="utf-8")
