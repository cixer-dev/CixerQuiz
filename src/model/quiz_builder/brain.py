from typing import Any
import os
import shutil

from src.model.configurators.standard_paths_configurator \
    import standard_path_reader
from src.model.json_wrapper import writer


class QuizBuilder:
    """Build filesystem structure and JSON manifests for a quiz package."""

    def __init__(self, quiz_manifest: dict, quiz_data: list[dict]):
        """Initialize the quiz builder with quiz configuration and data."""
        self.levels_data = quiz_data
        self.root_dir_quizzes_path = standard_path_reader.read_standard_path(
            "root_dir_quizzes_path"
        )
        self.quiz_manifest = quiz_manifest
        self.quiz_name = self._build_quiz_name()
        self.quiz_path = os.path.join(
            self.root_dir_quizzes_path,
            self.quiz_name
        )
        self.quiz_data_path = os.path.join(self.quiz_path, "data.json")
        self.assets_dir = os.path.join(
            self.quiz_path,
            "assets"
        )
        self.quiz_asset_paths = self._build_quiz_asset_paths()

    def _build_quiz_name(self) -> str:
        """Extract the quiz name from the quiz manifest content."""
        return self.quiz_manifest["quiz_name"]

    def _build_quiz_asset_paths(self) -> set[str]:
        """Build a set of asset source paths."""
        quiz_asset_paths: set[str] = set()
        for level_data in self.levels_data:
            assets_paths_list = level_data.get("assets_paths_list")
            if assets_paths_list:
                self._format_answer_paths(level_data)
                self._format_question_paths(level_data)
                for asset_path in assets_paths_list:
                    quiz_asset_paths.add(asset_path)
            del level_data["assets_paths_list"]
        return quiz_asset_paths

    def build_quiz(self) -> None:
        """Create quiz directories and write all manifests and text\
            content."""
        self._create_quiz_dir()
        self._create_quiz_data()
        self._copy_assets()

    def _create_quiz_data(self) -> None:
        """Create data JSON that contains the information for represent
        the quiz and its levels"""
        quiz_data = {}
        quiz_data["manifest"] = self.quiz_manifest
        quiz_data["levels"] = self.levels_data
        writer.write_json(self.quiz_data_path, quiz_data)

    def _create_quiz_dir(self) -> None:
        """Create the root directory for the quiz package."""
        os.makedirs(self.quiz_path)

    def _copy_assets(self):
        """Copy the files from the user’s machine to the quiz’s
        assets directory"""
        os.makedirs(self.assets_dir)
        for path in self.quiz_asset_paths:
            shutil.copy2(path, self.assets_dir)

    @staticmethod
    def _format_question_paths(level_data: dict[str, Any]) -> None:
        """Rewrite question asset paths to be relative to the quiz assets\
            directory."""
        questions = level_data["text_content"]["questions"]
        for question_index, question in enumerate(questions):
            if isinstance(question, dict):
                question_text = next(iter(question.keys()))
                question_path = next(iter(question.values()))
                question_asset_name = os.path.basename(question_path)
                formatted_question_path = os.path.join(
                    "assets",
                    question_asset_name,
                )
                level_data["text_content"]["questions"][question_index][
                    question_text] = formatted_question_path

    @staticmethod
    def _format_answer_paths(level_data: dict[str, Any]) -> None:
        """Rewrite answer asset paths to be relative to the quiz assets\
            directory."""
        answers = level_data["text_content"]["answers"]
        for possible_answer_index, possible_answers in enumerate(answers):
            for index, answer in enumerate(possible_answers):
                if isinstance(answer, dict):
                    answer_text = next(iter(answer.keys()))
                    answer_path = next(iter(answer.values()))
                    answer_asset_name = os.path.basename(answer_path)
                    formatted_answer_path = os.path.join(
                        "assets",
                        answer_asset_name,
                    )
                    possible_answers = level_data["text_content"]["answers"]
                    answers = possible_answers[possible_answer_index]
                    answer_to_text = answers[index]
                    answer_to_text[answer_text] = formatted_answer_path
