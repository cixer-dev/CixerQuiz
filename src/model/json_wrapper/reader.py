from typing import Any
import json


def read_json(json_filepath: str) -> Any:
    """Return parsed JSON content from the given file path."""
    with open(json_filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def read_json_key(json_filepath: str, key: str) -> Any:
    """Return the value for the given key from a JSON file."""
    json_content = read_json(json_filepath)
    return json_content[key]
