"""CLI smoke tests using Click's CliRunner and subprocess e2e tests."""

import subprocess
import sys
import tempfile
from pathlib import Path

import pytest
from click.testing import CliRunner

from code2docs.cli import main


class TestCLI:
    """Unit tests using Click's CliRunner."""

    def setup_method(self):
        self.runner = CliRunner()

    def test_help(self):
        result = self.runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "code2docs" in result.output
        assert "generate" in result.output
        assert "sync" in result.output
        assert "init" in result.output

    def test_generate_help(self):
        result = self.runner.invoke(main, ["generate", "--help"])
        assert result.exit_code == 0
        assert "--readme-only" in result.output
        assert "--dry-run" in result.output
        assert "--verbose" in result.output

    def test_sync_help(self):
        result = self.runner.invoke(main, ["sync", "--help"])
        assert result.exit_code == 0
        assert "Synchronize" in result.output

    def test_init_creates_config(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = self.runner.invoke(main, ["init", tmpdir])
            assert result.exit_code == 0
            assert (Path(tmpdir) / "code2docs.yaml").exists()

    def test_generate_dry_run(self):
        result = self.runner.invoke(main, [".", "--dry-run"])
        assert result.exit_code == 0
        assert "code2docs" in result.output
        assert "README.md" in result.output
        assert "dry-run" in result.output
        assert "Done!" in result.output

    def test_readme_only_dry_run(self):
        result = self.runner.invoke(main, [".", "--readme-only", "--dry-run"])
        assert result.exit_code == 0
        assert "README.md" in result.output
        # Should NOT have docs/api since --readme-only
        assert "docs/api" not in result.output

    def test_default_group_routes_path(self):
        """Ensure bare path argument is routed to generate."""
        result = self.runner.invoke(main, [".", "--dry-run"])
        assert result.exit_code == 0
        assert "Done!" in result.output

    def test_verbose(self):
        result = self.runner.invoke(main, [".", "--verbose", "--dry-run"])
        assert result.exit_code == 0
        assert "Functions" in result.output
        assert "Classes" in result.output
        assert "Modules" in result.output

    def test_check_help(self):
        result = self.runner.invoke(main, ["check", "--help"])
        assert result.exit_code == 0
        assert "Health check" in result.output
        assert "--target" in result.output

    def test_check_runs(self):
        result = self.runner.invoke(main, ["check", "."])
        assert result.exit_code == 0
        assert "check" in result.output
        assert "Score:" in result.output

    def test_diff_help(self):
        result = self.runner.invoke(main, ["diff", "--help"])
        assert result.exit_code == 0
        assert "Preview" in result.output

    def test_diff_runs(self):
        result = self.runner.invoke(main, ["diff", "."])
        assert result.exit_code == 0
        assert "diff" in result.output
        assert "dry-run" in result.output


class TestCLIShellE2E:
    """E2E tests using actual shell subprocess calls."""

    @pytest.fixture
    def temp_project(self):
        """Create a temporary project with Python files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            project_dir = Path(tmpdir) / "test_project"
            project_dir.mkdir()

            # Create a simple Python package
            pkg_dir = project_dir / "my_pkg"
            pkg_dir.mkdir()
            (pkg_dir / "__init__.py").write_text('"""My package."""\n')
            (pkg_dir / "module.py").write_text(
                '"""A module."""\n\ndef hello():\n    """Say hello."""\n    return "Hello"\n'
            )

            # Create pyproject.toml
            (project_dir / "pyproject.toml").write_text(
                '[project]\nname = "test-project"\nversion = "0.1.0"\n'
            )

            yield project_dir

    def _run_shell(self, cmd: list, cwd: Path = None) -> subprocess.CompletedProcess:
        """Run command in shell and return result."""
        return subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            timeout=30,
        )

    def test_shell_generate(self, temp_project):
        """E2E: Generate docs via shell."""
        result = self._run_shell(
            [sys.executable, "-m", "code2docs", str(temp_project), "--dry-run"],
        )
        assert result.returncode == 0
        assert "code2docs" in result.stdout

    def test_shell_generate_creates_files(self, temp_project):
        """E2E: Generate actually creates output files."""
        output_dir = temp_project / "docs_output"

        result = self._run_shell(
            [sys.executable, "-m", "code2docs", str(temp_project),
             "--output", str(output_dir)],
            cwd=temp_project,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "Done!" in result.stdout

        # Check files were created
        assert (temp_project / "README.md").exists()

    def test_shell_init(self, temp_project):
        """E2E: Init command creates config file."""
        result = self._run_shell(
            [sys.executable, "-m", "code2docs", "init", str(temp_project)],
        )
        assert result.returncode == 0
        assert (temp_project / "code2docs.yaml").exists()

    def test_shell_check(self, temp_project):
        """E2E: Check command runs successfully."""
        # First generate some docs
        self._run_shell(
            [sys.executable, "-m", "code2docs", str(temp_project)],
            cwd=temp_project,
        )

        result = self._run_shell(
            [sys.executable, "-m", "code2docs", "check", str(temp_project)],
        )
        assert result.returncode == 0
        assert "Health" in result.stdout or "check" in result.stdout
        assert "Score:" in result.stdout

    def test_shell_diff(self, temp_project):
        """E2E: Diff command runs successfully."""
        result = self._run_shell(
            [sys.executable, "-m", "code2docs", "diff", str(temp_project)],
        )
        assert result.returncode == 0
        assert "diff" in result.stdout.lower()

    def test_shell_help(self):
        """E2E: Help command works."""
        result = self._run_shell(
            [sys.executable, "-m", "code2docs", "--help"],
        )
        assert result.returncode == 0
        assert "code2docs" in result.stdout
        assert "generate" in result.stdout

    def test_shell_generate_with_sections(self, temp_project):
        """E2E: Generate with --sections option."""
        result = self._run_shell(
            [sys.executable, "-m", "code2docs", str(temp_project),
             "--sections", "overview,install", "--dry-run"],
            cwd=temp_project,
        )
        assert result.returncode == 0

    def test_shell_version(self):
        """E2E: Check version output."""
        result = self._run_shell(
            [sys.executable, "-c", "import code2docs; print(code2docs.__version__)"],
        )
        assert result.returncode == 0
        assert "." in result.stdout.strip()


class TestCLINewFeaturesE2E:
    """E2E tests for new CLI features (--org-name)."""

    @pytest.fixture
    def temp_org(self):
        """Create a temporary organization with multiple projects."""
        with tempfile.TemporaryDirectory() as tmpdir:
            org_dir = Path(tmpdir) / "test_org"
            org_dir.mkdir()

            # Create project 1
            proj1 = org_dir / "project1"
            proj1.mkdir()
            (proj1 / "pyproject.toml").write_text(
                '[project]\nname = "project1"\nversion = "0.1.0"\n'
                'description = "First project"\n'
            )
            pkg1 = proj1 / "pkg1"
            pkg1.mkdir()
            (pkg1 / "__init__.py").write_text('"""Package 1."""\n')

            # Create project 2
            proj2 = org_dir / "project2"
            proj2.mkdir()
            (proj2 / "pyproject.toml").write_text(
                '[project]\nname = "project2"\nversion = "0.2.0"\n'
                'description = "Second project"\n'
            )
            pkg2 = proj2 / "pkg2"
            pkg2.mkdir()
            (pkg2 / "__init__.py").write_text('"""Package 2."""\n')

            yield org_dir

    def _run_shell(self, cmd: list, cwd: Path = None) -> subprocess.CompletedProcess:
        """Run command in shell and return result."""
        return subprocess.run(
            cmd,
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            timeout=30,
        )

    def test_shell_org_mode(self, temp_org):
        """E2E: Generate organization README with --org-name."""
        output_dir = temp_org / "articles"

        result = self._run_shell(
            [sys.executable, "-m", "code2docs", str(temp_org),
             "--output", str(output_dir),
             "--org-name", "TestOrg"],
            cwd=temp_org,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert "Done!" in result.stdout

        # Check org README was created
        org_readme = output_dir / "README.md"
        assert org_readme.exists(), f"Files in {output_dir}: {list(output_dir.iterdir())}"

        content = org_readme.read_text()
        assert "TestOrg" in content
        assert "project1" in content
        assert "project2" in content

    def test_shell_org_mode_dry_run(self, temp_org):
        """E2E: Organization mode dry run."""
        result = self._run_shell(
            [sys.executable, "-m", "code2docs", str(temp_org),
             "--org-name", "TestOrg", "--dry-run"],
        )
        assert result.returncode == 0
        assert "TestOrg" in result.stdout or "dry-run" in result.stdout
