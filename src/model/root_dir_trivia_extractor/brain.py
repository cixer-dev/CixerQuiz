from typing import Any
import os

from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper import reader


class RootDirTriviaExtractor:
    """Extract valid trivia directories and their manifest information \
        from the root directory."""

    def __init__(self) -> None:
        self.root_directory_path = standard_path_reader.read_standard_path(
            "root_dir_trivias_path"
        )
        self.pinned_trivias_list_path = (
            standard_path_reader.read_standard_path("pinned_trivias_list")
        )
        self.pinned_trivias_list = reader.read_json(
            self.pinned_trivias_list_path
        )
        self.valid_trivias_filepaths = self.get_valid_trivias()
        self.valid_trivias_filepaths_to_info = self.get_trivias_path_to_info()

    def get_valid_trivias(self) -> list[str]:
        """Return a list of valid trivia filepaths."""
        valid_trivias_filepaths = list(self.pinned_trivias_list)
        for filename in os.listdir(self.root_directory_path):
            filepath = os.path.join(self.root_directory_path, filename)
            is_valid_trivia = self._verify_if_valid_trivia(filepath)
            if is_valid_trivia:
                valid_trivias_filepaths.append(filepath)
        return valid_trivias_filepaths

    def _verify_if_valid_trivia(self, filepath: str) -> bool:
        """Return True if the filepath is a valid trivia directory."""
        trivia_manifest_filepath = os.path.join(filepath, "manifest.json")
        is_valid_trivia = False
        if filepath not in self.pinned_trivias_list:
            if os.path.isdir(filepath) and os.path.isfile(
                trivia_manifest_filepath
            ):
                is_valid_trivia = reader.read_json_key(
                    trivia_manifest_filepath, "is_valid_trivia"
                )
        return is_valid_trivia

    def get_trivias_path_to_info(self) -> dict[str, Any]:
        """Return a dictionary mapping trivia filepaths to their info."""
        valid_trivias_filepaths_to_info = {}
        for trivia_filepath in self.valid_trivias_filepaths:
            trivia_manifest_filepath = os.path.join(
                trivia_filepath, "manifest.json"
            )
            trivia_info = {
                "trivia_name": reader.read_json_key(
                    trivia_manifest_filepath, "trivia_name"
                ),
                "trivia_description": reader.read_json_key(
                    trivia_manifest_filepath, "trivia_description"
                ),
                "trivia_duration": reader.read_json_key(
                    trivia_manifest_filepath, "trivia_duration"
                ),
            }
            valid_trivias_filepaths_to_info[trivia_filepath] = trivia_info
        return valid_trivias_filepaths_to_info

    def get_trivias_filepaths_to_info(self) -> dict[str, Any]:
        """Return the mapping of trivia filepaths to their info."""
        return self.valid_trivias_filepaths_to_info
