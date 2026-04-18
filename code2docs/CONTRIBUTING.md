## Development Setup

```bash
git clone <repository-url>
cd code2docs
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"
```

## Development Workflow

1. Create a feature branch from `main`
2. Make your changes
3. Add or update tests
4. Run the test suite
5. Submit a pull request

## Testing

```bash
python -m unittest discover tests/
```

## Code Style

Follow PEP 8 conventions.

