# AGENTS.md

This file documents the AI agents and tools used for development and maintenance of the Diffractio library.

## Quality Assurance Tools

### Ruff (Linter and Formatter)
- **Purpose**: Fast Python linter and code formatter, replacing Flake8, isort, Black, and more.
- **Usage**:
  - Lint: `uv run ruff check .`
  - Auto-fix: `uv run ruff check --fix .`
  - Format: `uv run ruff format .`
- **Configuration**: `[tool.ruff]` section in `pyproject.toml`.
- **Rules**: Enabled sets include E (pycodestyle), F (Pyflakes), I (isort).

### Ty (Type Checker)
- **Purpose**: Extremely fast Python type checker and language server.
- **Usage**:
  - Check: `uv run ty check .`
- **Configuration**: `[tool.ty]` section in `pyproject.toml`.
- **Rules**: Configurable error/warn levels for various type issues.

### UV (Package Manager)
- **Purpose**: Fast Python package installer and dependency manager.
- **Usage**:
  - Install: `uv add package`
  - Sync: `uv sync`
  - Lock: `uv lock`
- **Benefits**: 10-100x faster than pip, reproducible builds with lockfiles.

## Package Structure (Just-Init)

All `__init__.py` files follow the just-init convention:
- One-line description of package purpose.
- File tree listing `.py` files and subdirectories alphabetically.
- Brief description for each entry.

Example:
```
"""
Core functionality for Diffractio.

core/
├── __init__.py        # Exports math, optics, drawing, operations.
├── drawing.py         # 2D drawing utilities.
...
"""
```

## Commit Guidelines

- Use descriptive commit messages focusing on "why" rather than "what".
- Run quality checks before committing: `uv run ruff check . && uv run ty check .`
- Include lockfile changes in commits: `uv.lock` for dependency updates.