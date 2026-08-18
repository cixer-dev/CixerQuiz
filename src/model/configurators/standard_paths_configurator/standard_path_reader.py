from typing import Any
import os

from src.model.json_wrapper import reader


path_to_standard_paths = os.path.join("config", "standard_paths.json")


def read_standard_path(standard_path_key: str) -> str:
    """Return the assembled absolute standard path from configured parts."""
    standard_path_parts = reader.read_json_key(
        path_to_standard_paths,
        standard_path_key
    )
    standard_path = os.path.join(*standard_path_parts)
    return standard_path


def read_standard_paths_content() -> dict[str, Any]:
    """Return the standard paths JSON content."""
    standard_paths_content = reader.read_json(path_to_standard_paths)
    return standard_paths_content


def get_path_to_standard_paths() -> str:
    """Return the filesystem path to the standard paths JSON file."""
    return path_to_standard_paths
