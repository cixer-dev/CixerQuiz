from scripts.project_version_comparator.pyproject_parser import PyProjectParser
from typing import Any, Optional


def have_same_major_and_minor(
    previous_pyproject_path: str,
    current_pyproject_path: str,
) -> Optional[bool]:
    """Return True if both projects have the same major and minor versions."""
    previous_version = get_version_tuple(previous_pyproject_path)
    current_version = get_version_tuple(current_pyproject_path)
    try:
        if previous_version and current_version:
            previous_major, previous_minor, _ = previous_version
            current_major, current_minor, _ = current_version
            if (
                previous_major == current_major
                and previous_minor == current_minor
            ):
                print(
                    f"Previous version: {previous_version}' and "
                    f"current version {current_version} "
                    f"has same major and minor version"
                    )
                return True
            else:
                print(
                    f"Previous version: {previous_version}' and "
                    f"current version {current_version} "
                    f"does not have the same major and minor version"
                    )
                return False
    except Exception:
        raise


def get_version_tuple(
    project_path: str,
) -> tuple[int, int, int] | None:
    """Return the project's major, minor, and patch versions."""
    pyproject_parser: Any = PyProjectParser(project_path)
    return pyproject_parser.get_project_version_tuple()
