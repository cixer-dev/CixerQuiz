from github_scripts.project_version_comparator.\
    pyproject_parser import PyProjectParser
from typing import Any, Optional


def get_versions_compatibility(
    previous_pyproject_path: str,
    current_pyproject_path: str,
) -> Optional[tuple[bool, bool, bool]]:
    """Compares the major, minor, and patch version components from the
    previous and current pyproject.toml files. Each position in the
    returned tuple represents whether that component is equal between
    the two versions."""
    previous_version_tuple = _get_version_tuple(previous_pyproject_path)
    current_version_tuple = _get_version_tuple(current_pyproject_path)
    try:
        if previous_version_tuple and current_version_tuple:
            compatibility_list = []
            for current, previous in zip(
                current_version_tuple,
                previous_version_tuple
                    ):
                if current == previous:
                    compatibility_list.append(True)
                else:
                    compatibility_list.append(False)
            return tuple(compatibility_list)
    except Exception:
        raise


def _get_version_tuple(
    project_path: str,
) -> Optional[tuple[int, int, int]]:
    """Return the project's major, minor, and patch versions."""
    pyproject_parser: Any = PyProjectParser(project_path)
    return pyproject_parser.get_project_version_tuple()
