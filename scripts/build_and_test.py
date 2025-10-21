#!/usr/bin/env python3
"""
Script to build and test the package locally before publishing
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(
            cmd, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed")
        print(f"Error: {e.stderr}")
        return False


def main():
    """Main function to build and test the package"""
    print("🚀 Building and testing vn-numberwords package...")

    # Change to project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    # Clean previous builds
    if not run_command("rm -rf build/ dist/ *.egg-info/", "Cleaning previous builds"):
        return False

    # Install build dependencies
    if not run_command("pip install build twine", "Installing build dependencies"):
        return False

    # Build package
    if not run_command("python -m build", "Building package"):
        return False

    # Check package
    if not run_command("twine check dist/*", "Checking package"):
        return False

    # Test package installation
    if not run_command("pip install dist/*.whl", "Testing package installation"):
        return False

    # Test import
    try:
        import vn_numberwords

        print(
            f"✅ Package imported successfully. Version: {vn_numberwords.__version__}"
        )

        # Test basic functionality
        from vn_numberwords import words_to_number, number_to_words

        assert words_to_number("muoi mot") == 11
        assert number_to_words(11) == "mười một"
        print("✅ Basic functionality test passed")

    except Exception as e:
        print(f"❌ Package test failed: {e}")
        return False

    print("\n🎉 Package build and test completed successfully!")
    print("📦 Package files are ready in dist/ directory")
    print("🚀 Ready to publish to PyPI!")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
