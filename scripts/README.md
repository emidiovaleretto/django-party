# Code Formatting Scripts

This directory contains scripts for maintaining code quality and PEP8 compliance.

## Scripts

### `check_formatting.sh`

**Purpose**: Checks Python code for PEP8 compliance without making changes.

**Usage**:
```bash
./scripts/check_formatting.sh
```

**What it does**:
- Checks for critical Python syntax errors (E9, F63, F7, F82)
- Performs full PEP8 compliance check
- Reports issues but doesn't modify files
- Exit code 0: all checks passed
- Exit code 1: issues found

**When to use**:
- Before committing code
- During code review
- In CI/CD pipeline (automated)

---

### `fix_formatting.sh`

**Purpose**: Automatically fixes PEP8 formatting issues in your code.

**Usage**:
```bash
./scripts/fix_formatting.sh
```

**What it does**:
- Removes unused imports and variables
- Fixes PEP8 formatting issues (indentation, spacing, line length, etc.)
- Applies changes in-place to your files
- Runs `check_formatting.sh` at the end to verify fixes

**When to use**:
- When `check_formatting.sh` reports issues
- Before committing code to save manual fixes
- After adding new code or imports

---

## Configuration

Formatting rules are configured in `.flake8` at the project root:

- **Max line length**: 127 characters
- **Max complexity**: 10
- **Excluded directories**: migrations, `__pycache__`, venv, fixtures, etc.
- **Ignored rules**: W503, E203 (conflicts with modern formatters)

---

## CI/CD Integration

The `check_formatting.sh` script runs automatically in GitHub Actions on every push and pull request. Code must pass formatting checks before tests run.

---

## Required Dependencies

These tools are included in `requirements.txt`:

- **flake8**: PEP8 linting and checking
- **autopep8**: Automatic PEP8 formatting
- **autoflake**: Remove unused imports and variables

Install with:
```bash
pip install -r requirements.txt
```
