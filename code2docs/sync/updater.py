"""Selectively regenerate documentation for changed modules."""

from pathlib import Path
from typing import List, Optional

from ..config import Code2DocsConfig
from .differ import ChangeInfo, Differ


class Updater:
    """Apply selective documentation updates based on detected changes."""

    def __init__(self, config: Optional[Code2DocsConfig] = None):
        self.config = config or Code2DocsConfig()

    def apply(self, project_path: str, changes: List[ChangeInfo]) -> None:
        """Regenerate documentation for changed modules."""
        from ..analyzers.project_scanner import ProjectScanner
        from ..generators.readme_gen import ReadmeGenerator
        from ..generators.api_reference_gen import ApiReferenceGenerator
        from ..generators.module_docs_gen import ModuleDocsGenerator

        project = Path(project_path).resolve()

        # Re-analyze project
        scanner = ProjectScanner(self.config)
        result = scanner.analyze(str(project))

        changed_modules = {c.module for c in changes}

        # Always regenerate README (it references all modules)
        readme_gen = ReadmeGenerator(self.config, result)
        readme_content = readme_gen.generate()
        readme_gen.write(str(project / self.config.readme_output), readme_content)

        docs_dir = project / self.config.output
        docs_dir.mkdir(parents=True, exist_ok=True)

        # Regenerate consolidated API reference
        if self.config.docs.api_reference:
            api_gen = ApiReferenceGenerator(self.config, result)
            (docs_dir / "api.md").write_text(api_gen.generate(), encoding="utf-8")

        # Regenerate consolidated module docs
        if self.config.docs.module_docs:
            mod_gen = ModuleDocsGenerator(self.config, result)
            (docs_dir / "modules.md").write_text(mod_gen.generate(), encoding="utf-8")

        # Save new state
        differ = Differ(self.config)
        differ.save_state(str(project))
