"""Auto-generate usage examples from public signatures and entry points."""

from pathlib import Path
from typing import Dict, List

from code2llm.core.models import AnalysisResult, FunctionInfo, ClassInfo

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
        """Generate basic_usage.py example."""
        project_name = self.config.project_name or Path(self.result.project_path).name
        lines: List[str] = [
            f'"""Basic usage of {project_name}."""',
            "",
        ]

        # Find importable public classes and functions
        public_classes = [
            c for c in self.result.classes.values()
            if not c.name.startswith("_")
        ]
        public_functions = [
            f for f in self.result.functions.values()
            if not f.is_private and not f.is_method and not f.name.startswith("_")
        ]

        # Generate import statements
        imported = set()
        for cls in public_classes[:5]:
            mod = cls.module or project_name
            lines.append(f"from {mod} import {cls.name}")
            imported.add(cls.name)

        for func in public_functions[:5]:
            if func.name not in imported:
                mod = func.module or project_name
                lines.append(f"from {mod} import {func.name}")
                imported.add(func.name)

        if not imported:
            lines.append(f"import {project_name}")

        lines.append("")
        lines.append("")

        # Generate usage examples
        if public_classes:
            cls = public_classes[0]
            lines.append(f"# Create {cls.name} instance")
            init_args = self._get_init_args(cls)
            if init_args:
                args_str = ", ".join(f"{a}=..." for a in init_args[:3])
                lines.append(f"obj = {cls.name}({args_str})")
            else:
                lines.append(f"obj = {cls.name}()")
            lines.append("")

            # Show method calls
            methods = self._get_public_methods(cls)
            for method in methods[:3]:
                args_str = ", ".join(f"{a}=..." for a in method.args if a != "self")
                ret_comment = f"  # → {method.returns}" if method.returns else ""
                lines.append(f"result = obj.{method.name}({args_str}){ret_comment}")

        if public_functions:
            lines.append("")
            lines.append("# Standalone functions")
            for func in public_functions[:5]:
                args_str = ", ".join(f"{a}=..." for a in func.args[:4])
                ret_comment = f"  # → {func.returns}" if func.returns else ""
                lines.append(f"result = {func.name}({args_str}){ret_comment}")

        lines.append("")
        return "\n".join(lines)

    def _generate_entry_point_examples(self) -> str:
        """Generate examples based on entry points."""
        project_name = self.config.project_name or Path(self.result.project_path).name
        lines = [
            f'"""Entry point examples for {project_name}."""',
            "",
        ]

        for ep in self.result.entry_points[:5]:
            func = self.result.functions.get(ep)
            if func:
                mod = func.module or project_name
                lines.append(f"from {mod} import {func.name}")
                lines.append("")
                args_str = ", ".join(f"{a}=..." for a in func.args[:4])
                lines.append(f"# Call entry point: {func.name}")
                if func.docstring:
                    lines.append(f"# {func.docstring.splitlines()[0]}")
                lines.append(f"result = {func.name}({args_str})")
                lines.append("")

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
        return sorted(classes, key=lambda c: len(c.methods), reverse=True)[:5]

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
