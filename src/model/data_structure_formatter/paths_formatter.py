import os
from pathlib import Path


def parts_to_path(parts: list[str]) -> str:
    """Return a filesystem path assembled from parts."""
    path = os.path.join(*parts)
    return path


def path_to_parts(original_path: str) -> list[str]:
    """Return a list of path parts for the given path."""
    path = Path(original_path)
    path_parts = list(path.parts)
    return [str(part) for part in path_parts]


def get_suffix(path: str) -> str:
    """Return the suffix of the given path without the leading dot."""
    return Path(path).suffix.lstrip(".")
