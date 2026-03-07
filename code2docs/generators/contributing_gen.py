"""CONTRIBUTING.md generator from project tooling detection."""

from typing import Dict, List

from code2llm.api import AnalysisResult

from ..config import Code2DocsConfig
from ..analyzers.dependency_scanner import DependencyScanner


class ContributingGenerator:
    """Generate CONTRIBUTING.md by detecting dev tools from pyproject.toml."""

    def __init__(self, config: Code2DocsConfig, result: AnalysisResult):
        self.config = config
        self.result = result

    def generate(self) -> str:
        """Generate CONTRIBUTING.md content."""
        project = self.config.project_name or "Project"
        tools = self._detect_dev_tools()
        lines = [
            f"# Contributing to {project}\n",
            self._render_setup(tools),
            "",
            self._render_development(tools),
            "",
            self._render_testing(tools),
            "",
            self._render_code_style(tools),
            "",
            self._render_pull_request(),
            "",
        ]
        return "\n".join(lines)

    def _detect_dev_tools(self) -> Dict[str, bool]:
        """Detect which dev tools are configured in the project."""
        scanner = DependencyScanner()
        deps = scanner.scan(self.result.project_path)
        all_deps = {d.name.lower() for d in deps.dependencies}
        all_deps |= {d.name.lower() for d in deps.dev_dependencies}
        return {
            "pytest": "pytest" in all_deps,
            "black": "black" in all_deps,
            "ruff": "ruff" in all_deps,
            "mypy": "mypy" in all_deps,
            "flake8": "flake8" in all_deps,
            "isort": "isort" in all_deps,
            "pre-commit": "pre-commit" in all_deps,
            "tox": "tox" in all_deps,
        }

    def _render_setup(self, tools: Dict[str, bool]) -> str:
        """Render development setup instructions."""
        project = self.config.project_name or "project"
        lines = [
            "## Development Setup\n",
            "```bash",
            f"git clone <repository-url>",
            f"cd {project}",
            "python -m venv .venv",
            "source .venv/bin/activate  # or .venv\\Scripts\\activate on Windows",
            "pip install -e \".[dev]\"",
            "```",
        ]
        return "\n".join(lines)

    @staticmethod
    def _render_development(tools: Dict[str, bool]) -> str:
        """Render development workflow."""
        lines = [
            "## Development Workflow\n",
            "1. Create a feature branch from `main`",
            "2. Make your changes",
            "3. Add or update tests",
            "4. Run the test suite",
            "5. Submit a pull request",
        ]
        return "\n".join(lines)

    @staticmethod
    def _render_testing(tools: Dict[str, bool]) -> str:
        """Render testing instructions."""
        lines = ["## Testing\n"]
        if tools.get("pytest"):
            lines.extend([
                "```bash",
                "# Run all tests",
                "pytest",
                "",
                "# Run with coverage",
                "pytest --cov --cov-report=term-missing",
                "",
                "# Run a specific test file",
                "pytest tests/test_specific.py -v",
                "```",
            ])
        else:
            lines.extend([
                "```bash",
                "python -m unittest discover tests/",
                "```",
            ])
        return "\n".join(lines)

    @staticmethod
    def _render_code_style(tools: Dict[str, bool]) -> str:
        """Render code style guidelines."""
        lines = ["## Code Style\n"]
        if tools.get("black"):
            lines.append("- **Formatting:** [Black](https://black.readthedocs.io/) — `black .`")
        if tools.get("ruff"):
            lines.append("- **Linting:** [Ruff](https://docs.astral.sh/ruff/) — `ruff check .`")
        if tools.get("mypy"):
            lines.append("- **Type checking:** [mypy](https://mypy.readthedocs.io/) — `mypy .`")
        if tools.get("flake8"):
            lines.append("- **Linting:** [flake8](https://flake8.pycqa.org/) — `flake8 .`")
        if tools.get("isort"):
            lines.append("- **Imports:** [isort](https://pycqa.github.io/isort/) — `isort .`")
        if not any(tools.get(t) for t in ("black", "ruff", "mypy", "flake8", "isort")):
            lines.append("Follow PEP 8 conventions.")
        return "\n".join(lines)

    @staticmethod
    def _render_pull_request() -> str:
        """Render pull request guidelines."""
        lines = [
            "## Pull Request Guidelines\n",
            "- Keep PRs focused — one feature or fix per PR",
            "- Include tests for new functionality",
            "- Update documentation if needed",
            "- Ensure all tests pass before submitting",
            "- Use descriptive commit messages",
        ]
        return "\n".join(lines)
