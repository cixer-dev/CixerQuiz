from typing import Any
import os

from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper import reader


class RootDirQuizExtractor:
    """Extract valid quiz directories and their manifest information \
        from the root directory."""

    def __init__(self) -> None:
        self.root_directory_path = standard_path_reader.read_standard_path(
            "root_dir_quizzes_path"
        )
        self.pinned_quizzes_list_path = (
            standard_path_reader.read_standard_path("pinned_quizzes_list")
        )
        self.pinned_quizzes_list = reader.read_json(
            self.pinned_quizzes_list_path
        )
        self.valid_quizzes_filepaths = self.get_valid_quizzes()
        self.valid_quizzes_filepaths_to_info = self.get_quizzes_path_to_info()

    def get_valid_quizzes(self) -> list[str]:
        """Return a list of valid quiz filepaths."""
        valid_quizzes_filepaths = list(self.pinned_quizzes_list)
        for filename in os.listdir(self.root_directory_path):
            filepath = os.path.join(self.root_directory_path, filename)
            is_valid_quiz = self._verify_if_valid_quiz(filepath)
            if is_valid_quiz:
                valid_quizzes_filepaths.append(filepath)
        return valid_quizzes_filepaths

    def _verify_if_valid_quiz(self, filepath: str) -> bool:
        """Return True if the filepath is a valid quiz directory."""
        quiz_manifest_filepath = os.path.join(filepath, "manifest.json")
        is_valid_quiz = False
        if filepath not in self.pinned_quizzes_list:
            if os.path.isdir(filepath) and os.path.isfile(
                quiz_manifest_filepath
            ):
                is_valid_quiz = reader.read_json_key(
                    quiz_manifest_filepath, "is_valid_quiz"
                )
        return is_valid_quiz

    def get_quizzes_path_to_info(self) -> dict[str, Any]:
        """Return a dictionary mapping quiz filepaths to their info."""
        valid_quizzes_filepaths_to_info = {}
        for quiz_filepath in self.valid_quizzes_filepaths:
            quiz_manifest_filepath = os.path.join(
                quiz_filepath, "manifest.json"
            )
            quiz_info = {
                "quiz_name": reader.read_json_key(
                    quiz_manifest_filepath, "quiz_name"
                ),
                "quiz_description": reader.read_json_key(
                    quiz_manifest_filepath, "quiz_description"
                ),
                "quiz_duration": reader.read_json_key(
                    quiz_manifest_filepath, "quiz_duration"
                ),
            }
            valid_quizzes_filepaths_to_info[quiz_filepath] = quiz_info
        return valid_quizzes_filepaths_to_info

    def get_quizzes_filepaths_to_info(self) -> dict[str, Any]:
        """Return the mapping of quiz filepaths to their info."""
        return self.valid_quizzes_filepaths_to_info
