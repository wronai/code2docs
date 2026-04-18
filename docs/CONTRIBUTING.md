## Development Setup

```bash
git clone https://github.com/wronai/code2docs
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

# Run with coverage
pytest --cov --cov-report=term-missing

# Run a specific test file
pytest tests/test_specific.py -v
```

## Code Style

- **Formatting:** [Black](https://black.readthedocs.io/) — `black .`
- **Linting:** [Ruff](https://docs.astral.sh/ruff/) — `ruff check .`
- **Type checking:** [mypy](https://mypy.readthedocs.io/) — `mypy .`

