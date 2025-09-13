# Contributing to GeoPointDB

Welcome! We're excited you're interested in contributing to GeoPointDB. This document outlines how you can help improve this project.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in the [issues](https://github.com/Pulkit-Py/geopointdb/issues).
2. If not, create a new issue with a clear title and description.
3. Include steps to reproduce the bug, expected behavior, and actual behavior.
4. Add any relevant error messages or screenshots.

### Suggesting Enhancements

1. Check if the enhancement has already been suggested.
2. Create a new issue with a clear title and description of the enhancement.
3. Explain why this enhancement would be useful.

### Code Contributions

1. Fork the repository and create a new branch for your feature or bugfix.
2. Make your changes with clear, concise commits.
3. Add tests for your changes.
4. Run all tests to ensure they pass.
5. Submit a pull request with a clear description of your changes.

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/your-username/geopointdb.git
   cd geopointdb
   ```

2. Set up a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Unix/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
- Use type hints for all function signatures.
- Write docstrings for all public functions and classes.
- Keep lines under 88 characters (Black's default line length).

## Testing

Run tests using pytest:

```bash
pytest
```

## Pull Request Process

1. Update the CHANGELOG.md with details of your changes.
2. Ensure all tests pass.
3. Make sure your code is well-documented.
4. Submit the pull request with a clear description of the changes.

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
