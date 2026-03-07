"""README.md generator from AnalysisResult."""

import re
from pathlib import Path
from typing import Dict, List, Optional

from jinja2 import Environment, PackageLoader, select_autoescape

from code2llm.core.models import AnalysisResult, FunctionInfo, ClassInfo

from ..config import Code2DocsConfig
from ..analyzers.dependency_scanner import DependencyScanner
from ..analyzers.endpoint_detector import EndpointDetector
from ..formatters.badges import generate_badges
from ..formatters.toc import generate_toc


MARKER_START = "<!-- code2docs:start -->"
MARKER_END = "<!-- code2docs:end -->"


class ReadmeGenerator:
    """Generate README.md from AnalysisResult."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self.env = Environment(
            loader=PackageLoader("code2docs", "templates"),
            autoescape=select_autoescape([]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def generate(self) -> str:
        """Generate full README content."""
        sections = self.config.readme.sections
        project_name = self.config.project_name or Path(self.result.project_path).name

        context = self._build_context(project_name)

        try:
            template = self.env.get_template("readme.md.j2")
            return template.render(**context, sections=sections)
        except Exception:
            # Fallback: build manually if template fails
            return self._build_manual(project_name, sections, context)

    def _build_context(self, project_name: str) -> Dict:
        """Build template context from analysis result."""
        # Dependencies
        dep_scanner = DependencyScanner()
        deps = dep_scanner.scan(self.result.project_path)

        # Endpoints
        endpoint_detector = EndpointDetector()
        endpoints = endpoint_detector.detect(self.result, self.result.project_path)

        # Public API
        public_functions = {
            k: v for k, v in self.result.functions.items()
            if not v.is_private and not v.is_method
        }
        public_classes = {
            k: v for k, v in self.result.classes.items()
        }

        # Entry points
        entry_points = self.result.entry_points or []

        # Metrics
        stats = self.result.stats or {}
        avg_complexity = self._calc_avg_complexity()

        # Module tree
        module_tree = self._build_module_tree()

        return {
            "project_name": project_name,
            "project_path": self.result.project_path,
            "badges": generate_badges(project_name, self.config.readme.badges, stats, deps),
            "stats": stats,
            "avg_complexity": avg_complexity,
            "dependencies": deps,
            "endpoints": endpoints,
            "public_functions": public_functions,
            "public_classes": public_classes,
            "entry_points": entry_points,
            "module_tree": module_tree,
            "modules": self.result.modules,
            "sync_markers": self.config.readme.sync_markers,
        }

    def _calc_avg_complexity(self) -> float:
        """Calculate average cyclomatic complexity."""
        complexities = []
        for func in self.result.functions.values():
            cc = func.complexity.get("cyclomatic", 0)
            if cc > 0:
                complexities.append(cc)
        return round(sum(complexities) / len(complexities), 1) if complexities else 0.0

    def _build_module_tree(self) -> str:
        """Build text-based module tree."""
        if not self.result.modules:
            return ""

        lines = []
        sorted_modules = sorted(self.result.modules.keys())
        for mod_name in sorted_modules:
            mod = self.result.modules[mod_name]
            prefix = "📦" if mod.is_package else "📄"
            func_count = len(mod.functions)
            class_count = len(mod.classes)
            detail = []
            if func_count:
                detail.append(f"{func_count} functions")
            if class_count:
                detail.append(f"{class_count} classes")
            detail_str = f" ({', '.join(detail)})" if detail else ""
            lines.append(f"{prefix} `{mod_name}`{detail_str}")

        return "\n".join(lines)

    def _build_manual(self, project_name: str, sections: List[str], context: Dict) -> str:
        """Fallback manual README builder."""
        parts: List[str] = []

        if context.get("sync_markers"):
            parts.append(MARKER_START)

        if "overview" in sections:
            parts.append(f"# {project_name}\n")
            if context.get("badges"):
                parts.append(context["badges"] + "\n")
            stats = context.get("stats", {})
            if stats:
                parts.append(
                    f"> **{stats.get('functions_found', 0)}** functions | "
                    f"**{stats.get('classes_found', 0)}** classes | "
                    f"**{stats.get('files_processed', 0)}** files | "
                    f"CC̄ = {context.get('avg_complexity', 0)}\n"
                )

        if "install" in sections:
            deps = context.get("dependencies")
            if deps and deps.install_command:
                parts.append("## Installation\n")
                parts.append(f"```bash\n{deps.install_command}\n```\n")
                if deps.python_version:
                    parts.append(f"Requires Python {deps.python_version}\n")

        if "quickstart" in sections:
            parts.append("## Quick Start\n")
            entry_points = context.get("entry_points", [])
            if entry_points:
                parts.append("```python")
                parts.append(f"# Entry points: {', '.join(entry_points[:3])}")
                parts.append("```\n")

        if "api" in sections:
            parts.append("## API Overview\n")
            for name, cls in list(context.get("public_classes", {}).items())[:20]:
                doc = f" — {cls.docstring.splitlines()[0]}" if cls.docstring else ""
                parts.append(f"- **`{cls.name}`**{doc}")
            parts.append("")
            for name, func in list(context.get("public_functions", {}).items())[:30]:
                args_str = ", ".join(func.args[:5])
                ret = f" → {func.returns}" if func.returns else ""
                parts.append(f"- `{func.name}({args_str}){ret}`")
            parts.append("")

        if "structure" in sections:
            tree = context.get("module_tree", "")
            if tree:
                parts.append("## Project Structure\n")
                parts.append(tree + "\n")

        if "endpoints" in sections:
            endpoints = context.get("endpoints", [])
            if endpoints:
                parts.append("## Endpoints\n")
                parts.append("| Method | Path | Function | Framework |")
                parts.append("|--------|------|----------|-----------|")
                for ep in endpoints:
                    parts.append(f"| {ep.method} | `{ep.path}` | `{ep.function_name}` | {ep.framework} |")
                parts.append("")

        if context.get("sync_markers"):
            parts.append(MARKER_END)

        return "\n".join(parts)

    def write(self, path: str, content: str) -> None:
        """Write README, respecting sync markers if existing file has them."""
        readme_path = Path(path)

        if readme_path.exists():
            existing = readme_path.read_text(encoding="utf-8")
            if MARKER_START in existing and MARKER_END in existing:
                # Replace only between markers
                pattern = re.compile(
                    re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
                    re.DOTALL,
                )
                content = pattern.sub(content, existing)

        readme_path.parent.mkdir(parents=True, exist_ok=True)
        readme_path.write_text(content, encoding="utf-8")


def generate_readme(project_path: str = "./", output: str = "README.md",
                    sections: Optional[List[str]] = None, sync_markers: bool = True,
                    config: Optional[Code2DocsConfig] = None) -> str:
    """Convenience function to generate a README."""
    from ..analyzers.project_scanner import ProjectScanner

    config = config or Code2DocsConfig()
    if sections:
        config.readme.sections = sections
    config.readme.sync_markers = sync_markers

    scanner = ProjectScanner(config)
    result = scanner.analyze(project_path)

    gen = ReadmeGenerator(config, result)
    content = gen.generate()
    gen.write(output, content)
    return content
