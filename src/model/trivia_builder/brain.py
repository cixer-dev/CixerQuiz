import os
import shutil

from src.model.configurators.standard_paths_configurator \
    import standard_path_reader
from src.model.json_wrapper import writer


class TriviaBuilder:
    """Build filesystem structure and JSON manifests for a trivia package."""

    def __init__(self, trivia_manifest_content: dict, trivia_data: list[dict]):
        """Initialize the trivia builder with trivia configuration and data."""
        self.levels_data = trivia_data
        self.root_dir_trivias_path = standard_path_reader.read_standard_path(
            "root_dir_trivias_path"
        )
        self.trivia_manifest_content = trivia_manifest_content
        self.trivia_manifest_content_list = \
            self._build_trivia_manifest_content_list()
        self.trivia_text_content_list = self._build_trivia_text_content_list()
        self.trivia_assets_path_list = self._build_trivia_assets_path_list()
        self.trivia_name = self._build_trivia_name()
        self.trivia_path = os.path.join(
            self.root_dir_trivias_path,
            self.trivia_name
        )

    def _build_trivia_manifest_content_list(self) -> list[dict]:
        """Build a list of per-level manifest contents."""
        trivia_manifest_content_list: list[dict] = []
        for level_data in self.levels_data:
            level_manifest_content = level_data["manifest"]
            trivia_manifest_content_list.append(level_manifest_content)
        return trivia_manifest_content_list

    def _build_trivia_text_content_list(self) -> list[dict]:
        """Build a list of per-level text content."""
        trivia_text_content_list: list[dict] = []
        for level_data in self.levels_data:
            level_text_content = level_data["text_content"]
            trivia_text_content_list.append(level_text_content)
        return trivia_text_content_list

    def _build_trivia_assets_path_list(self) -> list[list[str]]:
        """Build a list of per-level asset source paths."""
        trivia_assets_path_list: list[list[str]] = []
        for level_data in self.levels_data:
            level_assets_paths_list = level_data["assets_paths_list"]
            trivia_assets_path_list.append(level_assets_paths_list)
        return trivia_assets_path_list

    def _build_trivia_name(self) -> str:
        """Extract the trivia name from the trivia manifest content."""
        return self.trivia_manifest_content["trivia_name"]

    def build_trivia(self) -> None:
        """Create trivia directories and write all manifests and text\
              content."""
        self._create_trivia_dir()
        self._create_levels_content()
        self._create_trivia_manifest_content()

    def _create_trivia_dir(self) -> None:
        """Create the root directory for the trivia package."""
        os.makedirs(self.trivia_path)

    def _create_levels_content(self) -> None:
        """Create all level directories, manifests, text content, and\
            assets."""
        for level_index in range(len(self.trivia_text_content_list)):
            self._create_level_path(level_index)
            self._create_level_manifest(level_index)
            self._create_level_text_content(level_index)
            if self.trivia_assets_path_list:
                self._copy_trivia_assets(level_index)

    def _create_level_path(self, level_index: int) -> None:
        """Create a directory for a specific level."""
        level_path = self._get_level_path_by_index(level_index)
        os.makedirs(level_path)

    def _get_level_path_by_index(self, level_index: int) -> str:
        """Return the filesystem path for a given level index."""
        return os.path.join(self.trivia_path, str(level_index + 1))

    def _create_level_manifest(self, level_index: int) -> None:
        """Write the manifest.json file for a specific level."""
        level_path = self._get_level_path_by_index(level_index)
        level_manifest_content_path = os.path.join(level_path, "manifest.json")
        level_manifest_content = self.trivia_manifest_content_list[level_index]
        writer.write_json(level_manifest_content_path, level_manifest_content)

    def _create_level_text_content(self, level_index: int) -> None:
        """Write the text_content.json file for a specific level."""
        level_path = self._get_level_path_by_index(level_index)
        level_text_content_path = os.path.join(level_path, "text_content.json")
        level_text_content = self.trivia_text_content_list[level_index]
        if self.trivia_assets_path_list:
            self._format_question_paths(level_text_content)
            self._format_answer_paths(level_text_content)
        writer.write_json(level_text_content_path, level_text_content)

    @staticmethod
    def _format_question_paths(level_text_content: dict) -> None:
        """Rewrite question asset paths to be relative to the level assets\
              dir."""
        questions = level_text_content["questions"]
        for question_index, question in enumerate(questions):
            if isinstance(question, dict):
                question_text = next(iter(question.keys()))
                question_path = next(iter(question.values()))
                question_asset_name = os.path.basename(question_path)
                formatted_question_path = os.path.join(
                    "assets",
                    question_asset_name,
                )
                level_text_content["questions"][question_index][question_text]\
                    = (formatted_question_path)

    @staticmethod
    def _format_answer_paths(level_text_content: dict) -> None:
        """Rewrite answer asset paths to be relative to the level assets\
              dir."""
        answers = level_text_content["answers"]
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
                    possible_answers = level_text_content["answers"]
                    answers = possible_answers[possible_answer_index]
                    answer_to_text = answers[index]
                    answer_to_text[answer_text] = formatted_answer_path

    def _copy_trivia_assets(self, level_index: int) -> None:
        """Copy level assets into the trivia structure."""
        level_path = self._get_level_path_by_index(level_index)
        level_assets_path = self.trivia_assets_path_list[level_index]
        if level_assets_path:
            level_assets_dirpath = self._get_level_assets_dirpath(level_path)
            os.makedirs(level_assets_dirpath)
            for asset_path in level_assets_path:
                shutil.copy2(asset_path, level_assets_dirpath)

    def _create_trivia_manifest_content(self) -> None:
        """Write the top-level manifest.json for the trivia package."""
        trivia_manifest_content_path = os.path.join(
            self.trivia_path, "manifest.json"
        )
        writer.write_json(
            trivia_manifest_content_path,
            self.trivia_manifest_content
        )

    @staticmethod
    def _get_level_assets_dirpath(level_path: str) -> str:
        """Return the assets directory path for a specific level."""
        level_assets_dirpath = os.path.join(level_path, "assets")
        return level_assets_dirpath
