"""Scan project dependencies from requirements.txt, pyproject.toml, setup.py, package.json, Cargo.toml, go.mod."""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        tomllib = None  # type: ignore


@dataclass
class DependencyInfo:
    """Information about a project dependency."""
    name: str
    version_spec: str = ""
    optional: bool = False
    group: str = "main"


@dataclass
class ProjectDependencies:
    """All detected project dependencies."""
    language: str = "python"
    python_version: str = ""
    runtime_version: str = ""
    dependencies: List[DependencyInfo] = field(default_factory=list)
    dev_dependencies: List[DependencyInfo] = field(default_factory=list)
    optional_groups: Dict[str, List[DependencyInfo]] = field(default_factory=dict)
    install_command: str = "pip install ."
    source_file: str = ""
    # Additional metadata from pyproject.toml
    keywords: List[str] = field(default_factory=list)
    classifiers: List[str] = field(default_factory=list)
    urls: Dict[str, str] = field(default_factory=dict)
    version: str = ""


class DependencyScanner:
    """Scan and parse project dependency files."""

    def scan(self, project_path: str) -> ProjectDependencies:
        """Scan project for dependency information."""
        project = Path(project_path)
        deps = ProjectDependencies()

        # Detect language from dependency files
        # Priority: pyproject.toml > setup.py > requirements.txt (Python)
        #           package.json (JS/TS) > Cargo.toml (Rust) > go.mod (Go)
        package_json = project / "package.json"
        if package_json.exists():
            deps = self._parse_package_json(package_json)
            deps.source_file = "package.json"
            # Detect TypeScript
            tsconfig = project / "tsconfig.json"
            if tsconfig.exists():
                deps.language = "typescript"
            return deps

        cargo_toml = project / "Cargo.toml"
        if cargo_toml.exists():
            deps = self._parse_cargo_toml(cargo_toml)
            deps.source_file = "Cargo.toml"
            return deps

        go_mod = project / "go.mod"
        if go_mod.exists():
            deps = self._parse_go_mod(go_mod)
            deps.source_file = "go.mod"
            return deps

        pyproject = project / "pyproject.toml"
        if pyproject.exists():
            deps = self._parse_pyproject(pyproject)
            deps.source_file = "pyproject.toml"
            return deps

        setup_py = project / "setup.py"
        if setup_py.exists():
            deps = self._parse_setup_py(setup_py)
            deps.source_file = "setup.py"
            return deps

        req_txt = project / "requirements.txt"
        if req_txt.exists():
            deps = self._parse_requirements_txt(req_txt)
            deps.source_file = "requirements.txt"
            return deps

        return deps

    def _parse_pyproject(self, path: Path) -> ProjectDependencies:
        """Parse pyproject.toml for dependencies."""
        deps = ProjectDependencies()

        if tomllib is None:
            # Fallback: regex-based parsing
            return self._parse_pyproject_regex(path)

        with open(path, "rb") as f:
            data = tomllib.load(f)

        project = data.get("project", {})
        deps.python_version = project.get("requires-python", "")
        deps.version = project.get("version", "")
        deps.keywords = project.get("keywords", [])
        deps.classifiers = project.get("classifiers", [])
        deps.urls = project.get("urls", {})

        # Main dependencies
        for dep_str in project.get("dependencies", []):
            deps.dependencies.append(self._parse_dep_string(dep_str))

        # Optional dependencies
        for group, dep_list in project.get("optional-dependencies", {}).items():
            group_deps = [self._parse_dep_string(d) for d in dep_list]
            for d in group_deps:
                d.optional = True
                d.group = group
            deps.optional_groups[group] = group_deps
            if group == "dev":
                deps.dev_dependencies = group_deps

        # Install command
        name = project.get("name", "")
        if name:
            deps.install_command = f"pip install {name}"

        # Detect version with fallback to git tags or VERSION file
        deps.version = self._detect_version(path.parent, deps.version)

        return deps

    def _parse_pyproject_regex(self, path: Path) -> ProjectDependencies:
        """Fallback regex-based pyproject.toml parser."""
        deps = ProjectDependencies()
        content = path.read_text(encoding="utf-8")

        # Extract dependencies array
        dep_match = re.search(r'dependencies\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if dep_match:
            for dep_str in re.findall(r'"([^"]+)"', dep_match.group(1)):
                deps.dependencies.append(self._parse_dep_string(dep_str))

        # Extract python version
        py_match = re.search(r'requires-python\s*=\s*"([^"]+)"', content)
        if py_match:
            deps.python_version = py_match.group(1)

        return deps

    def _parse_setup_py(self, path: Path) -> ProjectDependencies:
        """Parse setup.py for dependencies (regex-based, no exec)."""
        deps = ProjectDependencies()
        content = path.read_text(encoding="utf-8")

        # install_requires
        match = re.search(r'install_requires\s*=\s*\[(.*?)\]', content, re.DOTALL)
        if match:
            for dep_str in re.findall(r'"([^"]+)"', match.group(1)):
                deps.dependencies.append(self._parse_dep_string(dep_str))

        # python_requires
        py_match = re.search(r'python_requires\s*=\s*"([^"]+)"', content)
        if py_match:
            deps.python_version = py_match.group(1)

        return deps

    def _parse_requirements_txt(self, path: Path) -> ProjectDependencies:
        """Parse requirements.txt."""
        deps = ProjectDependencies()

        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("-"):
                continue
            deps.dependencies.append(self._parse_dep_string(line))

        deps.install_command = "pip install -r requirements.txt"
        return deps

    def _parse_package_json(self, path: Path) -> ProjectDependencies:
        """Parse package.json for dependencies."""
        import json
        deps = ProjectDependencies(language="javascript")
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return deps

        deps.version = data.get("version", "")
        name = data.get("name", "")

        # Node engine version
        engines = data.get("engines", {})
        deps.runtime_version = engines.get("node", "")

        for dep_name, ver in data.get("dependencies", {}).items():
            deps.dependencies.append(DependencyInfo(name=dep_name, version_spec=ver))

        for dep_name, ver in data.get("devDependencies", {}).items():
            deps.dev_dependencies.append(DependencyInfo(name=dep_name, version_spec=ver, group="dev"))

        # Detect install command
        lock_yarn = path.parent / "yarn.lock"
        lock_pnpm = path.parent / "pnpm-lock.yaml"
        if lock_pnpm.exists():
            deps.install_command = "pnpm install"
        elif lock_yarn.exists():
            deps.install_command = "yarn install"
        else:
            deps.install_command = "npm install"

        if name:
            deps.keywords = data.get("keywords", [])

        return deps

    def _parse_cargo_toml(self, path: Path) -> ProjectDependencies:
        """Parse Cargo.toml for Rust dependencies."""
        deps = ProjectDependencies(language="rust")
        content = path.read_text(encoding="utf-8")

        # Version
        ver_match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
        if ver_match:
            deps.version = ver_match.group(1)

        # Dependencies section
        in_deps = False
        in_dev_deps = False
        for line in content.splitlines():
            stripped = line.strip()
            if stripped == "[dependencies]":
                in_deps, in_dev_deps = True, False
                continue
            elif stripped == "[dev-dependencies]":
                in_deps, in_dev_deps = False, True
                continue
            elif stripped.startswith("["):
                in_deps, in_dev_deps = False, False
                continue

            dep_match = re.match(r'^([a-zA-Z0-9_-]+)\s*=\s*"?([^"\s]+)"?', stripped)
            if dep_match:
                info = DependencyInfo(name=dep_match.group(1), version_spec=dep_match.group(2))
                if in_dev_deps:
                    info.group = "dev"
                    deps.dev_dependencies.append(info)
                elif in_deps:
                    deps.dependencies.append(info)

        deps.install_command = "cargo build"
        return deps

    def _parse_go_mod(self, path: Path) -> ProjectDependencies:
        """Parse go.mod for Go dependencies."""
        deps = ProjectDependencies(language="go")
        content = path.read_text(encoding="utf-8")

        # Go version
        go_ver = re.search(r'^go\s+(\S+)', content, re.MULTILINE)
        if go_ver:
            deps.runtime_version = go_ver.group(1)

        # Require block
        require_block = re.search(r'require\s*\((.*?)\)', content, re.DOTALL)
        if require_block:
            for line in require_block.group(1).splitlines():
                line = line.strip()
                if not line or line.startswith("//"):
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    deps.dependencies.append(DependencyInfo(name=parts[0], version_spec=parts[1]))

        # Single-line requires
        for match in re.finditer(r'^require\s+(\S+)\s+(\S+)', content, re.MULTILINE):
            deps.dependencies.append(DependencyInfo(name=match.group(1), version_spec=match.group(2)))

        deps.install_command = "go mod download"
        return deps

    @staticmethod
    def _parse_dep_string(dep_str: str) -> DependencyInfo:
        """Parse a dependency string like 'package>=1.0'."""
        match = re.match(r'^([a-zA-Z0-9_-]+)\s*(.*)', dep_str.strip())
        if match:
            return DependencyInfo(
                name=match.group(1),
                version_spec=match.group(2).strip(),
            )
        return DependencyInfo(name=dep_str.strip())

    def _detect_version(self, project_path: Path, pyproject_version: str = "") -> str:
        """Detect version from pyproject.toml, git tags, or VERSION file."""
        # Priority 1: pyproject.toml version
        if pyproject_version:
            return pyproject_version

        # Priority 2: VERSION file
        version_file = project_path / "VERSION"
        if version_file.exists():
            return version_file.read_text(encoding="utf-8").strip()

        # Priority 3: git tags (latest tag)
        try:
            import subprocess
            result = subprocess.run(
                ["git", "describe", "--tags", "--abbrev=0"],
                cwd=str(project_path),
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0:
                return result.stdout.strip().lstrip("v")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        return ""
