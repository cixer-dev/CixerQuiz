from typing import Any
import json

from src.model.json_wrapper import reader


def write_json(json_filepath: str, json_content: Any) -> None:
    """Write JSON content to the given file path."""
    with open(json_filepath, "w", encoding="utf-8") as file:
        json.dump(json_content, file, indent=4)


class JsonOverwriter:
    """Update a specific key in a JSON file with a new value."""

    def __init__(
        self,
        json_filepath: str,
        json_key: str,
        json_value: Any
    ) -> None:
        self.json_filepath = json_filepath
        self.json_key = json_key
        self.json_value = json_value
        self.json_original_content = reader.read_json(self.json_filepath)

    def overwrite_json_key(self) -> None:
        """Update the JSON key with the provided value and persist to file."""
        if not isinstance(self.json_original_content, dict):
            raise TypeError(
                f"JSON content at {self.json_filepath} is not an object"
            )
        updated_json = self.json_original_content
        updated_json[self.json_key] = self.json_value
        write_json(self.json_filepath, updated_json)
