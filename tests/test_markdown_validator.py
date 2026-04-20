"""Tests for markdown validator."""
from pathlib import Path

from code2docs.analyzers.markdown_validator import (
    validate_markdown_file,
    validate_markdown_tree,
)


def test_validate_broken_link(tmp_path: Path) -> None:
    md = tmp_path / "README.md"
    md.write_text(
        "# Title\n\n"
        "[missing](./does-not-exist.md)\n"
        "[existing](./present.md)\n",
        encoding="utf-8",
    )
    (tmp_path / "present.md").write_text("# Present", encoding="utf-8")
    issues = validate_markdown_file(md, project_root=tmp_path)
    kinds = {i.kind for i in issues}
    assert "broken_link" in kinds
    assert any("does-not-exist" in i.message for i in issues)
    assert not any("present.md" in i.message for i in issues)


def test_validate_ignores_http_and_anchors(tmp_path: Path) -> None:
    md = tmp_path / "a.md"
    md.write_text(
        "[web](https://example.com)\n"
        "[anchor](#section)\n"
        "[mail](mailto:x@example.com)\n",
        encoding="utf-8",
    )
    assert validate_markdown_file(md, project_root=tmp_path) == []


def test_validate_ignores_links_in_code_fences(tmp_path: Path) -> None:
    md = tmp_path / "a.md"
    md.write_text(
        "```\n[missing](./nope.md)\n```\n",
        encoding="utf-8",
    )
    assert validate_markdown_file(md, project_root=tmp_path) == []


def test_validate_detects_table_shape(tmp_path: Path) -> None:
    md = tmp_path / "a.md"
    md.write_text(
        "| a | b | c |\n"
        "|---|---|---|\n"
        "| 1 | 2 |\n",
        encoding="utf-8",
    )
    issues = validate_markdown_file(md, project_root=tmp_path)
    assert any(i.kind == "table_shape" for i in issues)


def test_validate_detects_duplicate_headings(tmp_path: Path) -> None:
    md = tmp_path / "a.md"
    md.write_text(
        "## Intro\n\n## Intro\n",
        encoding="utf-8",
    )
    issues = validate_markdown_file(md, project_root=tmp_path)
    assert any(i.kind == "duplicate_heading" for i in issues)


def test_validate_tree_skips_ignored_dirs(tmp_path: Path) -> None:
    (tmp_path / "good.md").write_text("# ok\n", encoding="utf-8")
    vendor = tmp_path / "vendor"
    vendor.mkdir()
    (vendor / "bad.md").write_text("[x](./missing.md)\n", encoding="utf-8")
    report = validate_markdown_tree(tmp_path)
    assert report.files_checked == 1
    assert report.ok
