"""Docstring coverage report generator."""

from typing import Dict, List

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig
from ..analyzers.docstring_extractor import DocstringExtractor


class CoverageGenerator:
    """Generate docs/coverage.md — docstring coverage report."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self._extractor = DocstringExtractor()

    def generate(self) -> str:
        """Generate coverage.md content."""
        project_name = self.config.project_name or "Project"
        report = self._extractor.coverage_report(self.result)

        lines = [
            f"# {project_name} — Docstring Coverage\n",
            self._render_summary(report),
            "",
            "## Per-Module Breakdown\n",
            self._render_per_module(),
            "",
            "## Undocumented Items\n",
            self._render_undocumented(),
            "",
        ]
        return "\n".join(lines)

    @staticmethod
    def _render_summary(report: Dict[str, float]) -> str:
        """Render overall coverage summary."""
        overall = report.get("overall_coverage", 0)
        badge = "🟢" if overall >= 80 else "🟡" if overall >= 50 else "🔴"
        lines = [
            f"{badge} **Overall coverage: {overall:.1f}%**\n",
            "| Category | Documented | Total | Coverage |",
            "|----------|-----------|-------|----------|",
            f"| Functions | {report['functions_documented']} | {report['functions_total']} | {report['functions_coverage']:.1f}% |",
            f"| Classes | {report['classes_documented']} | {report['classes_total']} | {report['classes_coverage']:.1f}% |",
        ]
        return "\n".join(lines)

    def _render_per_module(self) -> str:
        """Render per-module coverage table."""
        rows: List[str] = [
            "| Module | Functions | Classes | Coverage |",
            "|--------|-----------|---------|----------|",
        ]
        for mod_name in sorted(self.result.modules.keys()):
            funcs = [f for f in self.result.functions.values()
                     if f.module == mod_name and not f.is_method]
            classes = [c for c in self.result.classes.values()
                       if c.module == mod_name]
            total = len(funcs) + len(classes)
            documented = (sum(1 for f in funcs if f.docstring) +
                          sum(1 for c in classes if c.docstring))
            pct = (documented / total * 100) if total else 100.0
            badge = "🟢" if pct >= 80 else "🟡" if pct >= 50 else "🔴"
            rows.append(
                f"| `{mod_name}` | {sum(1 for f in funcs if f.docstring)}/{len(funcs)} "
                f"| {sum(1 for c in classes if c.docstring)}/{len(classes)} "
                f"| {badge} {pct:.0f}% |"
            )
        return "\n".join(rows)

    def _render_undocumented(self) -> str:
        """List all undocumented public functions and classes."""
        items: List[str] = []
        for name, func in sorted(self.result.functions.items()):
            if not func.docstring and not func.is_private and not func.is_method:
                items.append(f"- `{name}` ({func.file}:{func.line})")
        for name, cls in sorted(self.result.classes.items()):
            if not cls.docstring:
                items.append(f"- `{name}` ({cls.file}:{cls.line})")
        if not items:
            return "_All public items are documented._ ✅"
        return "\n".join(items)
