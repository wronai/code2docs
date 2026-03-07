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

        # Regenerate API docs for changed modules
        if self.config.docs.api_reference:
            api_gen = ApiReferenceGenerator(self.config, result)
            all_files = api_gen.generate_all()

            # Filter to changed modules only
            docs_dir = project / self.config.output / "api"
            docs_dir.mkdir(parents=True, exist_ok=True)

            # Always regenerate index
            index_content = all_files.get("index.md", "")
            if index_content:
                (docs_dir / "index.md").write_text(index_content, encoding="utf-8")

            for filename, content in all_files.items():
                if filename == "index.md":
                    continue
                # Check if this file corresponds to a changed module
                for mod in changed_modules:
                    safe_mod = mod.replace(".", "_").replace("/", "_")
                    if safe_mod in filename:
                        (docs_dir / filename).write_text(content, encoding="utf-8")
                        break

        # Regenerate module docs for changed modules
        if self.config.docs.module_docs:
            mod_gen = ModuleDocsGenerator(self.config, result)
            all_files = mod_gen.generate_all()

            docs_dir = project / self.config.output / "modules"
            docs_dir.mkdir(parents=True, exist_ok=True)

            for filename, content in all_files.items():
                for mod in changed_modules:
                    safe_mod = mod.replace(".", "_").replace("/", "_")
                    if safe_mod in filename:
                        (docs_dir / filename).write_text(content, encoding="utf-8")
                        break

        # Save new state
        differ = Differ(self.config)
        differ.save_state(str(project))
