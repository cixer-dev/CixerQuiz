from typing import Optional
import argparse

from github_scripts.project_version_comparator.comparator import (
    get_versions_compatibility,
)


def compare_versions() -> Optional[tuple[bool, bool, bool]]:
    """Return whether the major and minor versions are equal."""
    argument_parser = argparse.ArgumentParser(
        description=(
            "Compare the major and minor versions of two "
            "pyproject.toml files."
        )
    )
    argument_parser.add_argument(
        "previous_pyproject_path",
        help="Path to the previous pyproject.toml file.",
    )
    argument_parser.add_argument(
        "current_pyproject_path",
        help="Path to the current pyproject.toml file.",
    )
    arguments = argument_parser.parse_args()

    return get_versions_compatibility(
        arguments.previous_pyproject_path,
        arguments.current_pyproject_path,
    )


def main() -> int:
    """Return an exit code based on the version comparison."""
    result = compare_versions()

    if result == (False, False, False):
        print("Major, minor, and patch versions are different.")
        return 2
    elif result == (True, False, False):
        print(
            "Major version is equal, but minor and patch versions "
            "are different.")
        return 3
    elif result == (True, True, False):
        print(
            "Major and minor versions are equal, but the patch version "
            "is different.")
        return 4
    elif result == (True, True, True):
        print("Major, minor, and patch versions are equal.")
        return 5
    else:
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
