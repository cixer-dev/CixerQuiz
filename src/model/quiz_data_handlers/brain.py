import os
from typing import Any, Type, TypeAlias

from src.model.json_wrapper import reader
from src.model.quiz_data_handlers.concrete_templates.dh_text_texts import \
    DHTextTexts
from src.model.quiz_data_handlers.concrete_templates.dh_text_images import \
    DHTextImages
from src.model.quiz_data_handlers.concrete_templates.dh_text_videos import \
    DHTextVideos
from src.model.quiz_data_handlers.concrete_templates.dh_image_texts import \
    DHImageTexts
from src.model.quiz_data_handlers.concrete_templates.dh_image_images import \
    DHImageImages
from src.model.quiz_data_handlers.concrete_templates.dh_image_videos import \
    DHImageVideos
from src.model.quiz_data_handlers.concrete_templates.dh_video_texts import \
    DHVideoTexts
from src.model.quiz_data_handlers.concrete_templates.dh_video_images import \
    DHVideoImages
from src.model.quiz_data_handlers.concrete_templates.dh_video_videos import \
    DHVideoVideos

LevelClass: TypeAlias = \
    Type[DHTextTexts] | Type[DHTextImages] | Type[DHTextVideos] | \
    Type[DHImageTexts] | Type[DHImageImages] | Type[DHImageVideos] | \
    Type[DHVideoTexts] | Type[DHVideoImages] | Type[DHVideoVideos]
LevelInstance: TypeAlias = \
    DHTextTexts | DHTextImages | DHTextVideos | \
    DHImageTexts | DHImageImages | DHImageVideos | \
    DHVideoTexts | DHVideoImages | DHVideoVideos


class QuizDataHandler:
    """
    Extract, process, and provide relevant data about a generic quiz.
    """

    def __init__(self, quiz_path: str) -> None:
        self.quiz_path = quiz_path
        self.quiz_manifest_filepath = os.path.join(
            self.quiz_path,
            "manifest.json"
        )
        self.level_type_id_to_dh_class = {
            "TEXT_TEXTS": DHTextTexts,
            "TEXT_IMAGES": DHTextImages,
            "TEXT_VIDEOS": DHTextVideos,
            "IMAGE_TEXTS": DHImageTexts,
            "IMAGE_IMAGES": DHImageImages,
            "IMAGE_VIDEOS": DHImageVideos,
            "VIDEO_TEXTS": DHVideoTexts,
            "VIDEO_IMAGES": DHVideoImages,
            "VIDEO_VIDEOS": DHVideoVideos
        }
        self.level_to_data = self._build_level_to_data()
        self.dh_levels = self._build_dh_level()

    def _build_level_to_data(self) -> dict[str, Any]:
        unsorted_level_to_data = \
            self._build_unsorted_level_name_keys_empty()
        sorted_level_to_data = \
            self._build_sorted_level_to_data(unsorted_level_to_data)
        self._append_paths(sorted_level_to_data)
        self._append_level_type_id(sorted_level_to_data)
        self._append_quiz_duration(sorted_level_to_data)
        return sorted_level_to_data

    def _build_unsorted_level_name_keys_empty(self) -> dict[str, Any]:
        unsorted_level_to_data = {}
        for filename in os.listdir(self.quiz_path):
            filepath = os.path.join(self.quiz_path, filename)
            is_level = os.path.isdir(filepath) and filename.isdigit()
            if is_level:
                unsorted_level_to_data[filename] = {}
        return unsorted_level_to_data

    @staticmethod
    def _build_sorted_level_to_data(
            unsorted_level_to_data: dict[str, Any]) -> dict[str, Any]:
        level_to_data = {}
        level_name_keys = list(unsorted_level_to_data.keys())
        level_name_keys.sort()
        for level_name in level_name_keys:
            data = unsorted_level_to_data[level_name]
            level_to_data[level_name] = data
        return level_to_data

    def _append_paths(self, sorted_level_to_data: dict[str, Any]) -> None:
        for level_name in sorted_level_to_data:
            filepath = os.path.join(self.quiz_path, level_name)
            sorted_level_to_data[level_name]["level_path"] = filepath

    def _append_quiz_duration(
            self,
            sorted_level_to_data: dict[str, Any]) -> None:
        quiz_duration = reader.read_json_key(
            self.quiz_manifest_filepath,
            "quiz_duration"
        )
        for level_name in sorted_level_to_data:
            sorted_level_to_data[level_name]["quiz_duration"] = \
                quiz_duration

    @staticmethod
    def _append_level_type_id(
        sorted_level_data_with_paths: dict[str, Any]
            ) -> None:
        for level_name in sorted_level_data_with_paths:
            level_path = \
                sorted_level_data_with_paths[level_name]["level_path"]
            manifest_filepath = os.path.join(level_path, "manifest.json")
            level_type_id = reader.read_json_key(
                manifest_filepath,
                "level_type_id"
            )
            sorted_level_data_with_paths[level_name]["level_type_id"] = \
                level_type_id

    def _build_dh_level(self) -> list[LevelInstance]:
        dh_levels = []
        for level_name, data in self.level_to_data.items():
            level_class = self._get_level_class(level_name)
            level_path = data["level_path"]
            quiz_duration = data.get("quiz_duration")
            level_object = level_class(level_path, quiz_duration)
            dh_levels.append(level_object)
        return dh_levels

    def _get_level_class(self, level_name: str) -> LevelClass:
        level_type_id = self.level_to_data[level_name]["level_type_id"]
        level_class = self.level_type_id_to_dh_class[level_type_id]
        return level_class

    def get_dh_levels(self) -> list[LevelInstance]:
        return self.dh_levels
