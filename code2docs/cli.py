"""CLI interface for code2docs."""

import sys
from pathlib import Path
from typing import Optional

import click

from .config import Code2DocsConfig


class DefaultGroup(click.Group):
    """Click Group that routes unknown subcommands to 'generate'."""

    def parse_args(self, ctx, args):
        if not args:
            args = ["generate"]
        elif args[0] not in self.commands and args[0] not in ("--help", "-h"):
            args = ["generate"] + args
        return super().parse_args(ctx, args)


@click.group(cls=DefaultGroup)
def main():
    """code2docs — Auto-generate project documentation from source code."""


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
@click.option("--readme-only", is_flag=True, help="Generate only README.md")
@click.option("--sections", "-s", default=None, help="Comma-separated sections to generate")
@click.option("--output", "-o", default=None, help="Output directory for docs")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.option("--dry-run", is_flag=True, help="Show what would be generated without writing")
def generate(project_path, config_path, readme_only, sections, output, verbose, dry_run):
    """Generate documentation (default command)."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True
    if output:
        config.output = output
    if sections:
        config.readme.sections = [s.strip() for s in sections.split(",")]

    _run_generate(project_path, config, readme_only=readme_only, dry_run=dry_run)


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
@click.option("--dry-run", is_flag=True, help="Show what would change without writing")
def sync(project_path, config_path, verbose, dry_run):
    """Synchronize documentation with source code changes."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True

    _run_sync(project_path, config, dry_run=dry_run)


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
@click.option("--verbose", "-v", is_flag=True, help="Verbose output")
def watch(project_path, config_path, verbose):
    """Watch for file changes and auto-regenerate docs."""
    config = _load_config(project_path, config_path)
    if verbose:
        config.verbose = True

    _run_watch(project_path, config)


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--output", "-o", default="code2docs.yaml", help="Output config file path")
def init(project_path, output):
    """Initialize code2docs.yaml configuration file."""
    project_path = Path(project_path).resolve()
    config = Code2DocsConfig(
        project_name=project_path.name,
        source="./",
    )
    out_path = project_path / output
    config.to_yaml(str(out_path))
    click.echo(f"Created {out_path}")


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
@click.option("--target", "-t", default=80, type=int, help="Docstring coverage target (%)")
def check(project_path, config_path, target):
    """Health check — verify documentation completeness."""
    config = _load_config(project_path, config_path)
    _run_check(project_path, config, target)


@main.command()
@click.argument("project_path", default=".", type=click.Path(exists=True))
@click.option("--config", "-c", "config_path", default=None, help="Path to code2docs.yaml")
def diff(project_path, config_path):
    """Preview what would change without writing anything."""
    config = _load_config(project_path, config_path)
    _run_diff(project_path, config)


def _load_config(project_path: str, config_path: Optional[str] = None) -> Code2DocsConfig:
    """Load configuration, auto-detecting code2docs.yaml if present."""
    project = Path(project_path).resolve()

    if config_path:
        return Code2DocsConfig.from_yaml(config_path)

    # Auto-detect
    for name in ("code2docs.yaml", "code2docs.yml"):
        candidate = project / name
        if candidate.exists():
            return Code2DocsConfig.from_yaml(str(candidate))

    # Defaults
    config = Code2DocsConfig(project_name=project.name, source="./")
    return config


def _run_generate(project_path: str, config: Code2DocsConfig,
                  readme_only: bool = False, dry_run: bool = False):
    """Run full documentation generation via the generator registry."""
    from .analyzers.project_scanner import ProjectScanner
    from .base import GenerateContext
    from .registry import GeneratorRegistry
    from .generators._registry_adapters import ALL_ADAPTERS

    project = Path(project_path).resolve()
    click.echo(f"📖 code2docs: analyzing {project.name}...")

    # Step 1: Analyze
    scanner = ProjectScanner(config)
    result = scanner.analyze(str(project))

    if config.verbose:
        click.echo(f"  Functions: {len(result.functions)}")
        click.echo(f"  Classes: {len(result.classes)}")
        click.echo(f"  Modules: {len(result.modules)}")

    # Step 2: Build context and registry
    docs_dir = project / config.output
    if not dry_run and not readme_only:
        docs_dir.mkdir(parents=True, exist_ok=True)

    ctx = GenerateContext(
        project=project, docs_dir=docs_dir,
        dry_run=dry_run, verbose=config.verbose,
    )

    registry = GeneratorRegistry()
    for adapter_cls in ALL_ADAPTERS:
        registry.add(adapter_cls(config, result))

    # Step 3: Run all generators
    registry.run_all(ctx, readme_only=readme_only)

    click.echo("📖 Done!")


def _run_sync(project_path: str, config: Code2DocsConfig, dry_run: bool = False):
    """Run sync — regenerate only changed documentation."""
    from .sync.differ import Differ
    from .sync.updater import Updater

    project = Path(project_path).resolve()
    click.echo(f"🔄 code2docs sync: {project.name}...")

    differ = Differ(config)
    changes = differ.detect_changes(str(project))

    if not changes:
        click.echo("  No changes detected.")
        return

    click.echo(f"  Changes detected in {len(changes)} modules")

    if dry_run:
        for change in changes:
            click.echo(f"    - {change}")
        return

    updater = Updater(config)
    updater.apply(str(project), changes)
    click.echo("🔄 Sync complete!")


def _run_watch(project_path: str, config: Code2DocsConfig):
    """Run file watcher for auto-resync."""
    try:
        from .sync.watcher import start_watcher
    except ImportError:
        click.echo("Error: watchdog not installed. Install with: pip install code2docs[watch]")
        sys.exit(1)

    project = Path(project_path).resolve()
    click.echo(f"👁 Watching {project.name} for changes... (Ctrl+C to stop)")
    start_watcher(str(project), config)


def _run_check(project_path: str, config: Code2DocsConfig, target: int = 80):
    """Run documentation health check."""
    from .analyzers.project_scanner import ProjectScanner
    from .analyzers.docstring_extractor import DocstringExtractor

    project = Path(project_path).resolve()
    click.echo(f"🩺 code2docs check: {project.name}\n")

    scanner = ProjectScanner(config)
    result = scanner.analyze(str(project))

    score = 0
    total = 0

    # Check README
    total += 1
    readme = project / config.readme_output
    if readme.exists():
        click.echo("  ✅ README.md exists")
        score += 1
    else:
        click.echo("  ❌ README.md missing")

    # Check docs/
    docs_dir = project / config.output
    for subdir, label in [("api", "API reference"), ("modules", "Module docs")]:
        total += 1
        d = docs_dir / subdir
        if d.exists() and any(d.iterdir()):
            count = sum(1 for f in d.glob("*.md"))
            click.echo(f"  ✅ {label}: {count} files")
            score += 1
        else:
            click.echo(f"  ❌ {label}: missing or empty")

    # Check examples/
    total += 1
    ex_dir = project / "examples"
    if ex_dir.exists() and any(ex_dir.iterdir()):
        count = sum(1 for f in ex_dir.glob("*.py"))
        click.echo(f"  ✅ examples/: {count} files")
        score += 1
    else:
        click.echo(f"  ❌ examples/: missing or empty")

    # Docstring coverage
    total += 1
    extractor = DocstringExtractor()
    report = extractor.coverage_report(result)
    coverage = report.get("overall_coverage", 0)
    if coverage >= target:
        click.echo(f"  ✅ Docstring coverage: {coverage:.0f}% (target: {target}%)")
        score += 1
    else:
        click.echo(f"  ⚠️  Docstring coverage: {coverage:.0f}% (target: {target}%)")

    click.echo(f"\n  Score: {score}/{total}")


def _run_diff(project_path: str, config: Code2DocsConfig):
    """Preview documentation changes without writing."""
    from .analyzers.project_scanner import ProjectScanner
    from .base import GenerateContext
    from .registry import GeneratorRegistry
    from .generators._registry_adapters import ALL_ADAPTERS

    project = Path(project_path).resolve()
    click.echo(f"🔍 code2docs diff: {project.name}\n")

    scanner = ProjectScanner(config)
    result = scanner.analyze(str(project))

    docs_dir = project / config.output
    ctx = GenerateContext(project=project, docs_dir=docs_dir, dry_run=True)

    registry = GeneratorRegistry()
    for adapter_cls in ALL_ADAPTERS:
        registry.add(adapter_cls(config, result))

    registry.run_all(ctx)
