"""Module documentation generator — single consolidated modules.md."""

import ast
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from code2llm.api import AnalysisResult, FunctionInfo, ClassInfo, ModuleInfo

from ..config import Code2DocsConfig


class ModuleDocsGenerator:
    """Generate docs/modules.md — consolidated module documentation."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self) -> str:
        """Generate a single modules.md with all modules grouped by package."""
        project = self.config.project_name or Path(self.result.project_path).name

        lines = [
            f"# {project} — Module Reference\n",
            f"> {len(self.result.modules)} modules | "
            f"{len(self.result.functions)} functions | "
            f"{len(self.result.classes)} classes\n",
        ]

        # Overview table of all modules
        lines.append("## Module Overview\n")
        lines.append("| Module | Lines | Functions | Classes | CC avg | Description |")
        lines.append("|--------|-------|-----------|---------|--------|-------------|")
        for mod_name, mod_info in sorted(self.result.modules.items()):
            if mod_name.startswith("_"):
                continue
            file_lines = self._count_file_lines(mod_info.file)
            func_count = len([
                f for f in self.result.functions.values()
                if f.module == mod_name and not f.is_method
            ])
            class_count = len([
                c for c in self.result.classes.values()
                if c.module == mod_name
            ])
            if not func_count and not class_count:
                continue
            avg_cc = self._calc_module_avg_cc(mod_name)
            cc_str = str(avg_cc) if avg_cc else "—"
            doc = self._get_module_docstring(mod_info)
            doc_short = doc.splitlines()[0][:60] if doc else "—"
            lines.append(
                f"| `{mod_name}` | {file_lines} | {func_count} | "
                f"{class_count} | {cc_str} | {doc_short} |"
            )
        lines.append("")

        # Group modules by package and render details
        groups = self._group_modules()
        for group_name, modules in groups.items():
            non_trivial = [
                (m, self.result.modules[m]) for m in modules
                if self._has_content(m)
            ]
            if not non_trivial:
                continue
            lines.append(f"## {group_name}\n")
            for mod_name, mod_info in non_trivial:
                lines.append(self._render_module_detail(mod_name, mod_info))

        return "\n".join(lines)

    def _group_modules(self) -> Dict[str, List[str]]:
        """Group module names by top-level package."""
        groups: Dict[str, List[str]] = defaultdict(list)
        for mod_name in sorted(self.result.modules.keys()):
            parts = mod_name.split(".")
            if parts[0].startswith("_"):
                continue
            group = parts[0] if len(parts) > 1 else "Core"
            groups[group].append(mod_name)
        return dict(groups)

    def _has_content(self, mod_name: str) -> bool:
        """Check if module has public functions or classes."""
        return any(
            (not f.is_method and not f.name.startswith("_"))
            for f in self.result.functions.values()
            if f.module == mod_name
        ) or any(
            not c.name.startswith("_")
            for c in self.result.classes.values()
            if c.module == mod_name
        )

    def _render_module_detail(self, mod_name: str, mod_info: ModuleInfo) -> str:
        """Render a single module's detail section."""
        lines = [f"### `{mod_name}`\n"]

        # One-line description from docstring
        doc = self._get_module_docstring(mod_info)
        if doc:
            lines.append(f"{doc.splitlines()[0]}\n")

        # Classes with method summary
        module_classes = {
            k: v for k, v in self.result.classes.items()
            if v.module == mod_name and not v.name.startswith("_")
        }
        if module_classes:
            for cls_name, cls_info in sorted(module_classes.items()):
                bases = f" ({', '.join(cls_info.bases)})" if cls_info.bases else ""
                lines.append(f"**`{cls_info.name}`**{bases}")
                if cls_info.docstring:
                    lines.append(f": {cls_info.docstring.splitlines()[0]}")
                lines.append("")
                methods = self._get_public_methods(cls_info)
                if methods:
                    lines.append("| Method | Args | Returns | CC |")
                    lines.append("|--------|------|---------|----|")
                    for m in methods:
                        args = ", ".join(a for a in m.args[:4] if a != "self")
                        ret = m.returns or "—"
                        cc = m.complexity.get("cyclomatic_complexity",
                                              m.complexity.get("cyclomatic", "—"))
                        lines.append(f"| `{m.name}` | `{args}` | `{ret}` | {cc} |")
                    lines.append("")

        # Standalone functions
        module_functions = {
            k: v for k, v in self.result.functions.items()
            if v.module == mod_name and not v.is_method and not v.name.startswith("_")
        }
        if module_functions:
            for func_name, func_info in sorted(module_functions.items()):
                args = ", ".join(a for a in func_info.args if a != "self")
                ret = f" → {func_info.returns}" if func_info.returns else ""
                doc_line = ""
                if func_info.docstring:
                    doc_line = f" — {func_info.docstring.splitlines()[0]}"
                lines.append(f"- `{func_info.name}({args}){ret}`{doc_line}")
            lines.append("")

        return "\n".join(lines)

    def _get_public_methods(self, cls_info: ClassInfo) -> List[FunctionInfo]:
        """Get public (non-dunder) methods."""
        methods = []
        for method_name in cls_info.methods:
            short = method_name.split(".")[-1]
            if short.startswith("_"):
                continue
            for key in [method_name, f"{cls_info.qualified_name}.{short}"]:
                if key in self.result.functions:
                    methods.append(self.result.functions[key])
                    break
        return methods

    def _count_file_lines(self, file_path: str) -> int:
        """Count lines in source file."""
        try:
            path = Path(file_path)
            if path.exists():
                return len(path.read_text(encoding="utf-8").splitlines())
        except (OSError, UnicodeDecodeError):
            pass
        return 0

    def _calc_module_avg_cc(self, mod_name: str) -> float:
        """Calculate average cyclomatic complexity for module functions."""
        complexities = []
        for func in self.result.functions.values():
            if func.module == mod_name:
                cc = func.complexity.get(
                    "cyclomatic_complexity", func.complexity.get("cyclomatic", 0)
                )
                if cc > 0:
                    complexities.append(cc)
        return round(sum(complexities) / len(complexities), 1) if complexities else 0.0

    def _get_module_docstring(self, mod_info: ModuleInfo) -> str:
        """Try to extract module-level docstring."""
        try:
            path = Path(mod_info.file)
            if path.exists():
                tree = ast.parse(path.read_text(encoding="utf-8"))
                return ast.get_docstring(tree) or ""
        except Exception:
            pass
        return ""
