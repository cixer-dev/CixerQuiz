from typing import Any
import os

from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper import reader


class QuizExtractor:
    """Extract valid quiz directories and their manifest information \
        from the root directory."""

    def __init__(self) -> None:
        self.root_dir_path = standard_path_reader.read_standard_path(
            "root_dir_quizzes_path"
        )
        self.pinned_quizzes_list_path = (
            standard_path_reader.read_standard_path("pinned_quizzes_list")
        )
        self.pinned_quizzes_list = reader.read_json(
            self.pinned_quizzes_list_path
        )
        self.valid_quizzes_dirpath = self.get_valid_quizzes()
        self.valid_quizzes_filepaths_to_info \
            = self.get_quizzes_dirpath_to_info()

    def get_valid_quizzes(self) -> list[str]:
        """Return a list of valid quiz filepaths."""
        valid_quizzes_dirpath = list(self.pinned_quizzes_list)
        for filename in os.listdir(self.root_dir_path):
            quiz_dirpath = os.path.join(self.root_dir_path, filename)
            is_valid_quiz = self._verify_if_valid_quiz(quiz_dirpath)
            if is_valid_quiz:
                valid_quizzes_dirpath.append(quiz_dirpath)
        return valid_quizzes_dirpath

    def _verify_if_valid_quiz(self, dirpath: str) -> bool:
        """Return True if the filepath is a valid quiz directory."""
        quiz_data_filepath = os.path.join(dirpath, "data.json")
        is_valid_quiz = False
        if dirpath not in self.pinned_quizzes_list:
            if os.path.isdir(dirpath) and os.path.isfile(
                quiz_data_filepath
            ):
                try:
                    quiz_manifest = reader.read_json_key(
                        quiz_data_filepath, "manifest"
                    )
                    is_valid_quiz = quiz_manifest["is_valid_quiz"]
                except Exception:
                    is_valid_quiz = False
        return is_valid_quiz

    def get_quizzes_dirpath_to_info(self) -> dict[str, Any]:
        """Return a dictionary mapping quiz filepaths to their info."""
        valid_quizzes_dirpath_to_info = {}
        for quiz_dirpath in self.valid_quizzes_dirpath:
            quiz_filepath = os.path.join(quiz_dirpath, "data.json")
            quiz_manifest = reader.read_json_key(
                        quiz_filepath, "manifest"
                    )
            valid_quizzes_dirpath_to_info[quiz_dirpath] = quiz_manifest
        return valid_quizzes_dirpath_to_info
