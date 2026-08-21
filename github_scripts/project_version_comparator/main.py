from typing import Optional
import argparse

from github_scripts.project_version_comparator.comparator import (
    have_same_major_and_minor,
)


def compare_versions() -> Optional[bool]:
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

    return have_same_major_and_minor(
        arguments.previous_pyproject_path,
        arguments.current_pyproject_path,
    )


def main() -> int:
    """Return an exit code based on the version comparison."""
    result = compare_versions()

    if result:
        return 0
    elif result is False:
        return 2
    else:
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
