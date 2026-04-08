"""
Quickstart — code2docs

Minimal working examples for the most common use cases.
Run: python examples/quickstart.py
"""
from code2docs import Code2DocsConfig
from code2docs import generate_docs
from code2docs import generate_readme

if __name__ == "__main__":
    from code2docs.analyzers.project_scanner import ProjectScanner

    config = Code2DocsConfig(project_name='my-project', source='./src', output='./docs', verbose=True)
    generate_readme('./my-project', output='README.md')
    docs = generate_docs('./my-project', config=config)
    print(f'Generated {len(docs)} documentation sections')
    scanner = ProjectScanner(config)
    result = scanner.analyze('./my-project')
    print(f'Found {len(result.functions)} functions')
    print(f'Found {len(result.classes)} classes')
    print(f'Found {len(result.modules)} modules')