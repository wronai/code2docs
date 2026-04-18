## Prerequisites

- Python >=3.9
- pip (or your preferred package manager)
- 5 dependencies (installed automatically)

## Installation

```bash
pip install code2docs
```

To install from source:

```bash
git clone https://github.com/wronai/code2docs
cd code2docs
pip install -e .
```

# Generate full documentation for your project
code2docs ./path/to/your/project

# Preview what would be generated (no file writes)
code2docs ./path/to/your/project --dry-run

# Only regenerate README
code2docs ./path/to/your/project --readme-only
```

### Python API

```python
from code2docs.analyzers.project_scanner import analyze_and_document

# Convenience function: analyze a project in one call.
result = analyze_and_document("project_path", config=...)
```

