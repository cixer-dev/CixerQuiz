import argparse
import sys
import subprocess

from scripts.project_version_comparator.\
    main import have_same_major_and_minor


def main() -> None:
    """Compare dependency versions and update requirements if compatible."""
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

    versions_are_compatible = have_same_major_and_minor(
        arguments.previous_pyproject_path,
        arguments.current_pyproject_path,
    )
    if versions_are_compatible:
        update_requirements()


def update_requirements() -> None:
    """Run the Bash script that installs all dependencies with
    Poetry and exports them."""
    result = subprocess.run(
        [
            "bash",
            "scripts/update_requirements/main.sh",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    if result.stdout:
        print("Standard output:")
        print(result.stdout)

    if result.stderr:
        print("Error output:")
        print(result.stderr)


if __name__ == "__main__":
    sys.exit(main())
