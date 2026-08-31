import os


def is_directory(path: str) -> bool:
    """Return True if the given path is an existing directory."""
    return os.path.isdir(path)


def is_file(path: str) -> bool:
    """Return True if the given path is an existing file."""
    return os.path.isfile(path)
