"""API reference documentation generator — per-module API docs."""

from pathlib import Path
from typing import Dict, List, Optional

from jinja2 import Environment, PackageLoader, select_autoescape

from code2llm.core.models import AnalysisResult, FunctionInfo, ClassInfo, ModuleInfo

from ..config import Code2DocsConfig


class ApiReferenceGenerator:
    """Generate docs/api/ — per-module API reference from signatures."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result
        self.env = Environment(
            loader=PackageLoader("code2docs", "templates"),
            autoescape=select_autoescape([]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def generate_all(self) -> Dict[str, str]:
        """Generate API reference for all modules. Returns {filename: content}."""
        files: Dict[str, str] = {}

        # Index page
        files["index.md"] = self._generate_index()

        # Per-module pages
        for mod_name, mod_info in sorted(self.result.modules.items()):
            safe_name = mod_name.replace(".", "_").replace("/", "_")
            filename = f"module_{safe_name}.md"
            files[filename] = self._generate_module_api(mod_name, mod_info)

        return files

    def _generate_index(self) -> str:
        """Generate API index page."""
        lines = [
            "# API Reference\n",
            f"> Auto-generated from {len(self.result.modules)} modules | "
            f"{len(self.result.functions)} functions | "
            f"{len(self.result.classes)} classes\n",
            "## Modules\n",
        ]

        for mod_name in sorted(self.result.modules.keys()):
            mod = self.result.modules[mod_name]
            safe_name = mod_name.replace(".", "_").replace("/", "_")
            func_count = len(mod.functions)
            class_count = len(mod.classes)
            lines.append(
                f"- [`{mod_name}`](module_{safe_name}.md) — "
                f"{func_count} functions, {class_count} classes"
            )

        return "\n".join(lines) + "\n"

    def _generate_module_api(self, mod_name: str, mod_info: ModuleInfo) -> str:
        """Generate API reference for a single module."""
        lines = [f"# `{mod_name}`\n"]

        # Source info
        lines.append(f"> Source: `{mod_info.file}`\n")

        # Classes in this module
        module_classes = {
            k: v for k, v in self.result.classes.items()
            if v.module == mod_name or k.startswith(mod_name + ".")
        }
        if module_classes:
            lines.append("## Classes\n")
            for cls_name, cls_info in sorted(module_classes.items()):
                lines.append(f"### `{cls_info.name}`\n")
                if cls_info.bases:
                    lines.append(f"Inherits from: {', '.join(f'`{b}`' for b in cls_info.bases)}\n")
                if cls_info.docstring:
                    lines.append(f"{cls_info.docstring.strip()}\n")

                # Methods of this class
                methods = self._get_class_methods(cls_info)
                if methods:
                    lines.append("#### Methods\n")
                    for method in methods:
                        sig = self._format_signature(method)
                        doc_line = ""
                        if method.docstring:
                            doc_line = f" — {method.docstring.splitlines()[0]}"
                        cc = method.complexity.get("cyclomatic", 0)
                        cc_badge = f" ⚠️ CC={cc}" if cc > 10 else ""
                        lines.append(f"- `{sig}`{doc_line}{cc_badge}")
                    lines.append("")

        # Standalone functions in this module
        module_functions = {
            k: v for k, v in self.result.functions.items()
            if (v.module == mod_name or k.startswith(mod_name + "."))
            and not v.is_method
        }
        if module_functions:
            lines.append("## Functions\n")
            for func_name, func_info in sorted(module_functions.items()):
                sig = self._format_signature(func_info)
                lines.append(f"### `{sig}`\n")
                if func_info.docstring:
                    lines.append(f"{func_info.docstring.strip()}\n")
                cc = func_info.complexity.get("cyclomatic", 0)
                if cc:
                    lines.append(f"- Complexity: {cc}")
                if func_info.calls:
                    lines.append(f"- Calls: {', '.join(f'`{c}`' for c in func_info.calls[:10])}")
                lines.append("")

        # Imports
        if mod_info.imports:
            lines.append("## Imports\n")
            for imp in sorted(mod_info.imports):
                lines.append(f"- `{imp}`")
            lines.append("")

        return "\n".join(lines)

    def _get_class_methods(self, cls_info: ClassInfo) -> List[FunctionInfo]:
        """Get FunctionInfo objects for class methods."""
        methods = []
        for method_name in cls_info.methods:
            # Try various qualified name patterns
            for key in [method_name, f"{cls_info.qualified_name}.{method_name}"]:
                if key in self.result.functions:
                    methods.append(self.result.functions[key])
                    break
        return methods

    @staticmethod
    def _format_signature(func: FunctionInfo) -> str:
        """Format a function signature string."""
        args_str = ", ".join(func.args)
        ret = f" → {func.returns}" if func.returns else ""
        return f"{func.name}({args_str}){ret}"

    def write_all(self, output_dir: str, files: Dict[str, str]) -> None:
        """Write all generated API reference files."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            (out / filename).write_text(content, encoding="utf-8")
