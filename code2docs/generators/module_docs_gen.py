"""Per-module detailed documentation generator."""

from pathlib import Path
from typing import Dict, List

from code2llm.core.models import AnalysisResult, ModuleInfo, FunctionInfo, ClassInfo

from ..config import Code2DocsConfig


class ModuleDocsGenerator:
    """Generate docs/modules/ — detailed per-module documentation."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate_all(self) -> Dict[str, str]:
        """Generate documentation for all modules. Returns {filename: content}."""
        files: Dict[str, str] = {}

        for mod_name, mod_info in sorted(self.result.modules.items()):
            safe_name = mod_name.replace(".", "_").replace("/", "_")
            filename = f"{safe_name}.md"
            files[filename] = self._generate_module(mod_name, mod_info)

        return files

    def _generate_module(self, mod_name: str, mod_info: ModuleInfo) -> str:
        """Generate detailed documentation for a single module."""
        lines: List[str] = []

        # Header
        lines.append(f"# {mod_name}\n")

        # Source metadata
        file_lines = self._count_file_lines(mod_info.file)
        avg_cc = self._calc_module_avg_cc(mod_name)
        meta_parts = [f"Source: `{mod_info.file}`"]
        if file_lines:
            meta_parts.append(f"{file_lines} lines")
        if avg_cc:
            meta_parts.append(f"CC avg: {avg_cc}")
        lines.append(f"> {' | '.join(meta_parts)}\n")

        # Overview (module docstring)
        module_doc = self._get_module_docstring(mod_info)
        if module_doc:
            lines.append("## Overview\n")
            lines.append(f"{module_doc}\n")

        # Classes
        module_classes = self._get_module_classes(mod_name)
        if module_classes:
            lines.append("## Classes\n")
            for cls_name, cls_info in module_classes.items():
                lines.append(f"### {cls_info.name}\n")
                if cls_info.bases:
                    lines.append(f"*Bases:* {', '.join(f'`{b}`' for b in cls_info.bases)}\n")
                if cls_info.docstring:
                    lines.append(f"{cls_info.docstring.strip()}\n")

                methods = self._get_class_methods(cls_info)
                if methods:
                    lines.append("#### Methods\n")
                    lines.append("| Method | Args | Returns | CC |")
                    lines.append("|--------|------|---------|----|")
                    for m in methods:
                        args = ", ".join(m.args[:4])
                        if len(m.args) > 4:
                            args += ", ..."
                        ret = m.returns or "—"
                        cc = m.complexity.get("cyclomatic", "—")
                        warn = " ⚠️" if isinstance(cc, (int, float)) and cc > 10 else ""
                        lines.append(f"| `{m.name}` | `{args}` | `{ret}` | {cc}{warn} |")
                    lines.append("")

        # Functions
        module_functions = self._get_module_functions(mod_name)
        if module_functions:
            lines.append("## Functions\n")
            for func_name, func_info in module_functions.items():
                args_str = ", ".join(func_info.args)
                ret = f" → {func_info.returns}" if func_info.returns else ""
                lines.append(f"### `{func_info.name}({args_str}){ret}`\n")
                if func_info.docstring:
                    lines.append(f"{func_info.docstring.strip()}\n")
                if func_info.calls:
                    lines.append(f"**Calls:** {', '.join(f'`{c}`' for c in func_info.calls[:10])}\n")
                if func_info.called_by:
                    lines.append(f"**Called by:** {', '.join(f'`{c}`' for c in func_info.called_by[:10])}\n")

        # Dependencies
        if mod_info.imports:
            lines.append("## Dependencies\n")
            internal = [i for i in mod_info.imports if not i.startswith(("os", "sys", "re", "json", "typing"))]
            external = [i for i in mod_info.imports if i.startswith(("os", "sys", "re", "json", "typing"))]
            if internal:
                lines.append("**Internal imports:**")
                for imp in sorted(internal):
                    lines.append(f"- `{imp}`")
                lines.append("")
            if external:
                lines.append("**Standard library:**")
                for imp in sorted(external):
                    lines.append(f"- `{imp}`")
                lines.append("")

        # Metrics table
        metrics = self._get_module_metrics(mod_name, mod_info)
        if metrics:
            lines.append("## Metrics\n")
            lines.append("| Metric | Value |")
            lines.append("|--------|-------|")
            for k, v in metrics.items():
                lines.append(f"| {k} | {v} |")
            lines.append("")

        return "\n".join(lines)

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
                cc = func.complexity.get("cyclomatic", 0)
                if cc > 0:
                    complexities.append(cc)
        return round(sum(complexities) / len(complexities), 1) if complexities else 0.0

    def _get_module_docstring(self, mod_info: ModuleInfo) -> str:
        """Try to extract module-level docstring."""
        try:
            import ast
            path = Path(mod_info.file)
            if path.exists():
                tree = ast.parse(path.read_text(encoding="utf-8"))
                return ast.get_docstring(tree) or ""
        except Exception:
            pass
        return ""

    def _get_module_classes(self, mod_name: str) -> Dict[str, ClassInfo]:
        return {
            k: v for k, v in self.result.classes.items()
            if v.module == mod_name or k.startswith(mod_name + ".")
        }

    def _get_module_functions(self, mod_name: str) -> Dict[str, FunctionInfo]:
        return {
            k: v for k, v in self.result.functions.items()
            if (v.module == mod_name or k.startswith(mod_name + ".")) and not v.is_method
        }

    def _get_class_methods(self, cls_info: ClassInfo) -> List[FunctionInfo]:
        methods = []
        for method_name in cls_info.methods:
            for key in [method_name, f"{cls_info.qualified_name}.{method_name}"]:
                if key in self.result.functions:
                    methods.append(self.result.functions[key])
                    break
        return methods

    def _get_module_metrics(self, mod_name: str, mod_info: ModuleInfo) -> Dict[str, str]:
        metrics = {}
        lines = self._count_file_lines(mod_info.file)
        if lines:
            metrics["Lines"] = str(lines)
        avg_cc = self._calc_module_avg_cc(mod_name)
        if avg_cc:
            metrics["Complexity (avg)"] = str(avg_cc)
        metrics["Functions"] = str(len(mod_info.functions))
        metrics["Classes"] = str(len(mod_info.classes))

        # Fan-in / fan-out
        fan_in = 0
        fan_out = 0
        for func in self.result.functions.values():
            if func.module == mod_name:
                fan_out += len(func.calls)
                fan_in += len(func.called_by)
        if fan_in:
            metrics["Fan-in"] = str(fan_in)
        if fan_out:
            metrics["Fan-out"] = str(fan_out)

        return metrics

    def write_all(self, output_dir: str, files: Dict[str, str]) -> None:
        """Write all generated module docs."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            (out / filename).write_text(content, encoding="utf-8")
