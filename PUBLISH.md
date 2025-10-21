# Publishing to PyPI

This document explains how to publish the `vn-numberwords` package to PyPI.

## Prerequisites

1. **PyPI Account**: Create an account at [pypi.org](https://pypi.org)
2. **API Token**: Generate an API token from your PyPI account settings
3. **GitHub Secrets**: Add your PyPI API token as a secret named `PYPI_API_TOKEN` in your GitHub repository

## Publishing Methods

### Method 1: GitHub Actions (Recommended)

1. **Create a Release**:
   - Go to your GitHub repository
   - Click "Releases" → "Create a new release"
   - Tag version: `v0.2.0` (must match version in `pyproject.toml`)
   - Release title: `v0.2.0 - Add words to number conversion`
   - Description: Include changelog
   - Click "Publish release"

2. **Automatic Publishing**:
   - The `publish.yml` workflow will automatically trigger
   - It will build and publish the package to PyPI
   - Check the Actions tab for progress

### Method 2: Manual Publishing

1. **Build the Package**:
   ```bash
   python -m pip install --upgrade build twine
   python -m build
   ```

2. **Check the Package**:
   ```bash
   twine check dist/*
   ```

3. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

### Method 3: Using the Build Script

1. **Run the Build Script**:
   ```bash
   python scripts/build_and_test.py
   ```

2. **Upload to PyPI**:
   ```bash
   twine upload dist/*
   ```

## Version Management

- Update version in `pyproject.toml` and `vn_numberwords/__init__.py`
- Use semantic versioning (MAJOR.MINOR.PATCH)
- For this release: `0.2.0` (new feature: words to number conversion)

## Testing Before Publishing

1. **Local Testing**:
   ```bash
   python scripts/build_and_test.py
   ```

2. **Test Installation**:
   ```bash
   pip install dist/*.whl
   python -c "import vn_numberwords; print(vn_numberwords.__version__)"
   ```

## Post-Publishing

1. **Verify Installation**:
   ```bash
   pip install vn-numberwords
   python -c "from vn_numberwords import words_to_number; print(words_to_number('muoi mot'))"
   ```

2. **Update Documentation**: Ensure README and examples are up to date

## Troubleshooting

- **Build Errors**: Check `pyproject.toml` syntax
- **Upload Errors**: Verify PyPI credentials and package name availability
- **Import Errors**: Ensure all dependencies are properly specified

## Changelog for v0.2.0

- ✅ Add `words_to_number()` function
- ✅ Add `currency_words_to_number()` function  
- ✅ Support both accented and non-accented Vietnamese
- ✅ Handle complex numbers with multiple magnitude keywords
- ✅ Add comprehensive test suite (95+ test cases)
- ✅ Update documentation with new features
- ✅ Fix linting issues and type annotations
