"""
Advanced usage — code2docs

Shows how to use individual generators, sync, and formatters.
Run: python examples/advanced_usage.py
"""
from code2docs import Code2DocsConfig
from code2docs.analyzers.project_scanner import ProjectScanner
from code2docs.generators.readme_gen import ReadmeGenerator
from code2docs.generators.architecture_gen import ArchitectureGenerator
from code2docs.generators.coverage_gen import CoverageGenerator
from code2docs.generators.depgraph_gen import DepGraphGenerator

if __name__ == "__main__":
    from code2docs.formatters.badges import generate_badges
    from code2docs.formatters.toc import generate_toc
    from code2docs.sync.differ import Differ
    from code2docs.sync.updater import Updater

    config = Code2DocsConfig(project_name='my-project')
    scanner = ProjectScanner(config)
    result = scanner.analyze('./my-project')
    readme_gen = ReadmeGenerator(config, result)
    content = readme_gen.generate()
    print(f'Generated {len(content)} characters')
    architecture_gen = ArchitectureGenerator(config, result)
    content = architecture_gen.generate()
    print(f'Generated {len(content)} characters')
    coverage_gen = CoverageGenerator(config, result)
    content = coverage_gen.generate()
    print(f'Generated {len(content)} characters')
    depGraph_gen = DepGraphGenerator(config, result)
    content = depGraph_gen.generate()
    print(f'Generated {len(content)} characters')
    badges = generate_badges(project_name='my-project', badge_types=['version', 'python', 'coverage'], stats={'version': '1.0.0', 'python': '>=3.9'})
    for badge in badges:
        print(badge)
    markdown = '# Title\n## Section 1\n## Section 2\n### Subsection'
    toc = generate_toc(markdown, max_depth=2)
    print(toc)
    differ = Differ(config)
    changes = differ.detect_changes('./my-project')
    if changes:
        print(f'Detected {len(changes)} changed modules:')
        for change in changes:
            print(f'  {change}')
        updater = Updater(config)
        updater.apply('./my-project', changes)
        print('Documentation updated!')
    else:
        print('No changes detected.')