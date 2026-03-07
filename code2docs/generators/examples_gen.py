"""Auto-generate usage examples from public signatures and entry points."""

from pathlib import Path
from typing import Dict, List

from code2llm.api import AnalysisResult, FunctionInfo, ClassInfo

from ..config import Code2DocsConfig


class ExamplesGenerator:
    """Generate examples/ — usage examples from public API signatures."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate_all(self) -> Dict[str, str]:
        """Generate all example files. Returns {filename: content}."""
        files: Dict[str, str] = {}

        # Basic usage example
        files["basic_usage.py"] = self._generate_basic_usage()

        # Entry-point examples
        if self.config.examples.from_entry_points and self.result.entry_points:
            files["entry_points.py"] = self._generate_entry_point_examples()

        # Class-based examples for major classes
        major_classes = self._get_major_classes()
        if major_classes:
            files["class_examples.py"] = self._generate_class_examples(major_classes)

        return files

    def _generate_basic_usage(self) -> str:
        """Generate basic_usage.py example (orchestrator)."""
        project_name = self.config.project_name or Path(self.result.project_path).name
        public_classes = [
            c for c in self.result.classes.values()
            if not c.name.startswith("_")
        ]
        public_functions = [
            f for f in self.result.functions.values()
            if not f.is_private and not f.is_method and not f.name.startswith("_")
        ]

        sections = [
            f'"""Basic usage of {project_name}."""',
            "",
            self._generate_import_section(project_name, public_classes, public_functions),
            "",
            self._generate_class_usage_section(public_classes),
            self._generate_function_usage_section(public_functions),
            "",
        ]
        return "\n".join(s for s in sections if s is not None)

    def _generate_import_section(self, project_name: str,
                                 public_classes: List[ClassInfo],
                                 public_functions: List[FunctionInfo]) -> str:
        """Generate import statements for the example."""
        lines: List[str] = []
        imported = set()
        # Prefer classes/functions whose module looks like a public API
        for cls in public_classes[:5]:
            if cls.name in imported:
                continue
            mod = cls.module or project_name
            lines.append(f"from {mod} import {cls.name}")
            imported.add(cls.name)
        for func in public_functions[:5]:
            if func.name in imported:
                continue
            mod = func.module or project_name
            lines.append(f"from {mod} import {func.name}")
            imported.add(func.name)
        if not imported:
            lines.append(f"import {project_name}")
        return "\n".join(lines)

    def _generate_class_usage_section(self, public_classes: List[ClassInfo]) -> str:
        """Generate class instantiation and method call examples."""
        if not public_classes:
            return ""
        lines: List[str] = []
        cls = public_classes[0]
        lines.append(f"# Create {cls.name} instance")
        init_args = self._get_init_args(cls)
        if init_args:
            args_str = ", ".join(f"{a}=..." for a in init_args[:3])
            lines.append(f"obj = {cls.name}({args_str})")
        else:
            lines.append(f"obj = {cls.name}()")
        lines.append("")
        methods = self._get_public_methods(cls)
        for method in methods[:3]:
            args_str = ", ".join(f"{a}=..." for a in method.args if a != "self")
            ret_comment = f"  # → {method.returns}" if method.returns else ""
            lines.append(f"result = obj.{method.name}({args_str}){ret_comment}")
        return "\n".join(lines)

    def _generate_function_usage_section(self, public_functions: List[FunctionInfo]) -> str:
        """Generate standalone function call examples."""
        if not public_functions:
            return ""
        lines = ["", "# Standalone functions"]
        for func in public_functions[:5]:
            args_str = ", ".join(f"{a}=..." for a in func.args[:4])
            ret_comment = f"  # → {func.returns}" if func.returns else ""
            lines.append(f"result = {func.name}({args_str}){ret_comment}")
        return "\n".join(lines)

    def _generate_entry_point_examples(self) -> str:
        """Generate examples based on entry points."""
        project_name = self.config.project_name or Path(self.result.project_path).name
        lines = [
            f'"""Entry point examples for {project_name}."""',
            "",
        ]

        # Filter to public module-level functions only
        for ep in (self.result.entry_points or []):
            parts = ep.split(".")
            # Skip dunders, private, class methods (Capitalized segments)
            if any(seg.startswith("_") or (seg[0].isupper() if seg else False)
                   for seg in parts):
                continue
            func = self.result.functions.get(ep)
            if not func:
                continue
            mod = func.module or project_name
            lines.append(f"from {mod} import {func.name}")
            lines.append("")
            # Generate meaningful args (skip 'self')
            args = [a for a in func.args if a != "self"]
            args_str = ", ".join(f"{a}=..." for a in args[:4])
            if func.docstring:
                lines.append(f"# {func.docstring.splitlines()[0]}")
            lines.append(f"result = {func.name}({args_str})")
            lines.append("")
            if len(lines) > 40:
                break

        return "\n".join(lines)

    def _generate_class_examples(self, classes: List[ClassInfo]) -> str:
        """Generate examples for major classes."""
        project_name = self.config.project_name or Path(self.result.project_path).name
        lines = [
            f'"""Class usage examples for {project_name}."""',
            "",
        ]

        for cls in classes[:5]:
            mod = cls.module or project_name
            lines.append(f"from {mod} import {cls.name}")

        lines.append("")
        lines.append("")

        for cls in classes[:5]:
            lines.append(f"# --- {cls.name} ---")
            if cls.docstring:
                lines.append(f"# {cls.docstring.splitlines()[0]}")

            init_args = self._get_init_args(cls)
            if init_args:
                args_str = ", ".join(f"{a}=..." for a in init_args[:3])
                lines.append(f"instance = {cls.name}({args_str})")
            else:
                lines.append(f"instance = {cls.name}()")

            methods = self._get_public_methods(cls)
            for m in methods[:3]:
                args = [a for a in m.args if a != "self"]
                args_str = ", ".join(f"{a}=..." for a in args[:3])
                lines.append(f"instance.{m.name}({args_str})")

            lines.append("")

        return "\n".join(lines)

    def _get_major_classes(self) -> List[ClassInfo]:
        """Get classes with most methods (likely most important)."""
        classes = [c for c in self.result.classes.values() if not c.name.startswith("_")]
        # Prefer user-facing classes: Config, Generator, Scanner over internal Adapter/Info
        priority_suffixes = ("Config", "Generator", "Scanner", "Detector", "Extractor")
        depriority_suffixes = ("Info", "Adapter", "Formatter")
        return sorted(classes, key=lambda c: (
            0 if any(c.name.endswith(s) for s in priority_suffixes) else
            2 if any(c.name.endswith(s) for s in depriority_suffixes) else 1,
            -len(c.methods),
        ))[:5]

    def _get_init_args(self, cls: ClassInfo) -> List[str]:
        """Get __init__ args for a class."""
        for method_name in cls.methods:
            if "__init__" in method_name:
                for key in [method_name, f"{cls.qualified_name}.__init__"]:
                    func = self.result.functions.get(key)
                    if func:
                        return [a for a in func.args if a != "self"]
        return []

    def _get_public_methods(self, cls: ClassInfo) -> List[FunctionInfo]:
        """Get public methods of a class."""
        methods = []
        for method_name in cls.methods:
            for key in [method_name, f"{cls.qualified_name}.{method_name}"]:
                func = self.result.functions.get(key)
                if func and not func.is_private and func.name != "__init__":
                    methods.append(func)
                    break
        return methods

    def write_all(self, output_dir: str, files: Dict[str, str]) -> None:
        """Write all generated example files."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        for filename, content in files.items():
            (out / filename).write_text(content, encoding="utf-8")
