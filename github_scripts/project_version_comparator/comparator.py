from github_scripts.project_version_comparator.\
    pyproject_parser import PyProjectParser
from typing import Any, Optional


def have_same_major_and_minor(
    previous_pyproject_path: str,
    current_pyproject_path: str,
) -> Optional[bool]:
    """Return True if both projects have the same major and minor versions."""
    previous_version_tuple = _get_version_tuple(previous_pyproject_path)
    current_version_tuple = _get_version_tuple(current_pyproject_path)
    try:
        if previous_version_tuple and current_version_tuple:
            previous_version = _get_version_string(previous_version_tuple)
            current_version = _get_version_string(current_version_tuple)
            previous_major, previous_minor, _ = previous_version_tuple
            current_major, current_minor, _ = current_version_tuple
            if (
                previous_major == current_major
                and previous_minor == current_minor
            ):
                print(
                    f"Previous version: '{previous_version}' and "
                    f"current version '{current_version}' "
                    f"has same major and minor version"
                    )
                return True
            else:
                print(
                    f"Previous version: '{previous_version}' and "
                    f"current version '{current_version}' "
                    f"does not have the same major and minor version"
                    )
                return False
    except Exception:
        raise


def _get_version_tuple(
    project_path: str,
) -> Optional[tuple[int, int, int]]:
    """Return the project's major, minor, and patch versions."""
    pyproject_parser: Any = PyProjectParser(project_path)
    return pyproject_parser.get_project_version_tuple()


def _get_version_string(version_tuple: tuple) -> str:
    """Return version like an formatted string"""
    return ".".join(map(str, version_tuple))
