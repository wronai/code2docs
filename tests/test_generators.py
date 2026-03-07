"""Integration tests for generators using mock AnalysisResult."""

import tempfile
from pathlib import Path

import pytest

from code2llm.core.models import (
    AnalysisResult, FunctionInfo, ClassInfo, ModuleInfo,
)
from code2docs.config import Code2DocsConfig


def _make_result() -> AnalysisResult:
    """Build a realistic mock AnalysisResult for testing."""
    result = AnalysisResult(project_path="/tmp/mockproject")
    result.modules = {
        "mylib.core": ModuleInfo(
            name="mylib.core", file="/tmp/mockproject/mylib/core.py",
            imports=["os", "json", "mylib.utils"],
            functions=["process", "validate"],
            classes=["Engine"],
        ),
        "mylib.utils": ModuleInfo(
            name="mylib.utils", file="/tmp/mockproject/mylib/utils.py",
            imports=["re"],
            functions=["slugify", "sanitize"],
            classes=[],
        ),
    }
    result.classes = {
        "mylib.core.Engine": ClassInfo(
            name="Engine", qualified_name="mylib.core.Engine",
            file="/tmp/mockproject/mylib/core.py", line=10,
            module="mylib.core", bases=["BaseEngine"],
            methods=["run", "stop"],
            docstring="Main processing engine.",
        ),
    }
    result.functions = {
        "mylib.core.process": FunctionInfo(
            name="process", qualified_name="mylib.core.process",
            file="/tmp/mockproject/mylib/core.py", line=50,
            module="mylib.core", args=["data", "config"],
            returns="Result", docstring="Process input data.",
            complexity={"cyclomatic": 5},
        ),
        "mylib.core.validate": FunctionInfo(
            name="validate", qualified_name="mylib.core.validate",
            file="/tmp/mockproject/mylib/core.py", line=80,
            module="mylib.core", args=["schema", "payload"],
            returns="bool", docstring="Validate payload against schema.",
            complexity={"cyclomatic": 8},
        ),
        "mylib.core.Engine.run": FunctionInfo(
            name="run", qualified_name="mylib.core.Engine.run",
            file="/tmp/mockproject/mylib/core.py", line=15,
            module="mylib.core", is_method=True,
            args=["self", "input"], returns="Output",
            docstring="Run the engine.", complexity={"cyclomatic": 3},
        ),
        "mylib.core.Engine.stop": FunctionInfo(
            name="stop", qualified_name="mylib.core.Engine.stop",
            file="/tmp/mockproject/mylib/core.py", line=30,
            module="mylib.core", is_method=True,
            args=["self"], returns=None,
            docstring="Stop the engine.", complexity={"cyclomatic": 1},
        ),
        "mylib.utils.slugify": FunctionInfo(
            name="slugify", qualified_name="mylib.utils.slugify",
            file="/tmp/mockproject/mylib/utils.py", line=5,
            module="mylib.utils", args=["text"],
            returns="str", docstring="Convert text to slug.",
            complexity={"cyclomatic": 2},
        ),
        "mylib.utils.sanitize": FunctionInfo(
            name="sanitize", qualified_name="mylib.utils.sanitize",
            file="/tmp/mockproject/mylib/utils.py", line=20,
            module="mylib.utils", args=["html"],
            returns="str", docstring=None,
            complexity={"cyclomatic": 4},
        ),
    }
    result.stats = {
        "files_processed": 2,
        "functions_found": 6,
        "classes_found": 1,
    }
    result.entry_points = ["mylib.core.process"]
    return result


def _make_config(**kwargs) -> Code2DocsConfig:
    config = Code2DocsConfig(project_name="mockproject", **kwargs)
    return config


# --------------- ReadmeGenerator ---------------

class TestReadmeGenerator:
    def test_manual_fallback_contains_sections(self):
        from code2docs.generators.readme_gen import ReadmeGenerator
        config = _make_config()
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        # Force manual build via _build_manual
        context = gen._build_context("mockproject")
        content = gen._build_manual("mockproject", config.readme.sections, context)
        assert "# mockproject" in content
        assert "## API Overview" in content
        assert "## Quick Start" in content

    def test_manual_fallback_sync_markers(self):
        from code2docs.generators.readme_gen import ReadmeGenerator, MARKER_START, MARKER_END
        config = _make_config()
        config.readme.sync_markers = True
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        context = gen._build_context("mockproject")
        context["sync_markers"] = True
        content = gen._build_manual("mockproject", config.readme.sections, context)
        assert MARKER_START in content
        assert MARKER_END in content

    def test_generate_produces_output(self):
        from code2docs.generators.readme_gen import ReadmeGenerator
        config = _make_config()
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        content = gen.generate()
        assert len(content) > 100
        assert "mockproject" in content

    def test_build_api_section_lists_classes(self):
        from code2docs.generators.readme_gen import ReadmeGenerator
        config = _make_config()
        result = _make_result()
        gen = ReadmeGenerator(config, result)
        context = gen._build_context("mockproject")
        section = gen._build_api_section("mockproject", context)
        assert "Engine" in section

    def test_build_endpoints_section_empty(self):
        from code2docs.generators.readme_gen import ReadmeGenerator
        section = ReadmeGenerator._build_endpoints_section("x", {"endpoints": []})
        assert section == ""


# --------------- ApiReferenceGenerator ---------------

class TestApiReferenceGenerator:
    def test_generate_all_produces_files(self):
        from code2docs.generators.api_reference_gen import ApiReferenceGenerator
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        files = gen.generate_all()
        assert "index.md" in files
        assert len(files) >= 3  # index + 2 modules

    def test_index_lists_modules(self):
        from code2docs.generators.api_reference_gen import ApiReferenceGenerator
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        files = gen.generate_all()
        index = files["index.md"]
        assert "mylib.core" in index
        assert "mylib.utils" in index

    def test_module_api_contains_class(self):
        from code2docs.generators.api_reference_gen import ApiReferenceGenerator
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        content = gen._generate_module_api(
            "mylib.core", result.modules["mylib.core"]
        )
        assert "Engine" in content
        assert "## Classes" in content

    def test_module_api_contains_functions(self):
        from code2docs.generators.api_reference_gen import ApiReferenceGenerator
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        content = gen._generate_module_api(
            "mylib.core", result.modules["mylib.core"]
        )
        assert "process" in content
        assert "validate" in content

    def test_render_api_imports(self):
        from code2docs.generators.api_reference_gen import ApiReferenceGenerator
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        content = gen._render_api_imports(result.modules["mylib.core"])
        assert "## Imports" in content
        assert "`os`" in content

    def test_write_all(self):
        from code2docs.generators.api_reference_gen import ApiReferenceGenerator
        config = _make_config()
        result = _make_result()
        gen = ApiReferenceGenerator(config, result)
        files = gen.generate_all()
        with tempfile.TemporaryDirectory() as tmpdir:
            gen.write_all(tmpdir, files)
            written = list(Path(tmpdir).glob("*.md"))
            assert len(written) == len(files)


# --------------- ModuleDocsGenerator ---------------

class TestModuleDocsGenerator:
    def test_generate_all_produces_files(self):
        from code2docs.generators.module_docs_gen import ModuleDocsGenerator
        config = _make_config()
        result = _make_result()
        gen = ModuleDocsGenerator(config, result)
        files = gen.generate_all()
        assert len(files) == 2

    def test_render_header(self):
        from code2docs.generators.module_docs_gen import ModuleDocsGenerator
        config = _make_config()
        result = _make_result()
        gen = ModuleDocsGenerator(config, result)
        header = gen._render_header("mylib.core", result.modules["mylib.core"])
        assert "# mylib.core" in header
        assert "Source:" in header

    def test_render_classes_section(self):
        from code2docs.generators.module_docs_gen import ModuleDocsGenerator
        config = _make_config()
        result = _make_result()
        gen = ModuleDocsGenerator(config, result)
        section = gen._render_classes_section("mylib.core")
        assert "## Classes" in section
        assert "Engine" in section

    def test_render_functions_section(self):
        from code2docs.generators.module_docs_gen import ModuleDocsGenerator
        config = _make_config()
        result = _make_result()
        gen = ModuleDocsGenerator(config, result)
        section = gen._render_functions_section("mylib.core")
        assert "## Functions" in section
        assert "process" in section
        assert "validate" in section

    def test_render_dependencies_section(self):
        from code2docs.generators.module_docs_gen import ModuleDocsGenerator
        config = _make_config()
        result = _make_result()
        gen = ModuleDocsGenerator(config, result)
        section = gen._render_dependencies_section(result.modules["mylib.core"])
        assert "## Dependencies" in section
        assert "mylib.utils" in section

    def test_render_metrics_section(self):
        from code2docs.generators.module_docs_gen import ModuleDocsGenerator
        config = _make_config()
        result = _make_result()
        gen = ModuleDocsGenerator(config, result)
        section = gen._render_metrics_section("mylib.core", result.modules["mylib.core"])
        assert "## Metrics" in section

    def test_empty_module(self):
        from code2docs.generators.module_docs_gen import ModuleDocsGenerator
        config = _make_config()
        result = _make_result()
        gen = ModuleDocsGenerator(config, result)
        section = gen._render_classes_section("nonexistent.module")
        assert section == ""


# --------------- ExamplesGenerator ---------------

class TestExamplesGenerator:
    def test_generate_all_produces_basic_usage(self):
        from code2docs.generators.examples_gen import ExamplesGenerator
        config = _make_config()
        result = _make_result()
        gen = ExamplesGenerator(config, result)
        files = gen.generate_all()
        assert "basic_usage.py" in files

    def test_basic_usage_contains_imports(self):
        from code2docs.generators.examples_gen import ExamplesGenerator
        config = _make_config()
        result = _make_result()
        gen = ExamplesGenerator(config, result)
        content = gen._generate_basic_usage()
        assert "import" in content

    def test_basic_usage_contains_class_example(self):
        from code2docs.generators.examples_gen import ExamplesGenerator
        config = _make_config()
        result = _make_result()
        gen = ExamplesGenerator(config, result)
        content = gen._generate_basic_usage()
        assert "Engine" in content

    def test_entry_point_examples(self):
        from code2docs.generators.examples_gen import ExamplesGenerator
        config = _make_config()
        config.examples.from_entry_points = True
        result = _make_result()
        gen = ExamplesGenerator(config, result)
        files = gen.generate_all()
        assert "entry_points.py" in files
        assert "process" in files["entry_points.py"]

    def test_class_examples(self):
        from code2docs.generators.examples_gen import ExamplesGenerator
        config = _make_config()
        result = _make_result()
        gen = ExamplesGenerator(config, result)
        files = gen.generate_all()
        assert "class_examples.py" in files
        assert "Engine" in files["class_examples.py"]


# --------------- ArchitectureGenerator ---------------

class TestArchitectureGenerator:
    def test_generate_produces_output(self):
        from code2docs.generators.architecture_gen import ArchitectureGenerator
        config = _make_config()
        result = _make_result()
        gen = ArchitectureGenerator(config, result)
        content = gen.generate()
        assert "Architecture" in content
        assert len(content) > 50

    def test_contains_mermaid(self):
        from code2docs.generators.architecture_gen import ArchitectureGenerator
        config = _make_config()
        result = _make_result()
        gen = ArchitectureGenerator(config, result)
        content = gen.generate()
        assert "```mermaid" in content

    def test_contains_metrics(self):
        from code2docs.generators.architecture_gen import ArchitectureGenerator
        config = _make_config()
        result = _make_result()
        gen = ArchitectureGenerator(config, result)
        content = gen.generate()
        assert "Metrics" in content or "Metric" in content


# --------------- ChangelogGenerator ---------------

class TestChangelogGenerator:
    def test_generate_with_no_git(self):
        from code2docs.generators.changelog_gen import ChangelogGenerator
        config = _make_config()
        result = _make_result()
        gen = ChangelogGenerator(config, result)
        with tempfile.TemporaryDirectory() as tmpdir:
            content = gen.generate(tmpdir)
            # No git repo → should still return a valid string
            assert isinstance(content, str)
