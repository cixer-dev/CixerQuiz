import os
from typing import Type, TypeAlias

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

    def __init__(self, quiz_dirpath: str) -> None:
        self.quiz_dirpath = quiz_dirpath
        self.quiz_filepath = os.path.join(self.quiz_dirpath, "data.json")
        self.quiz_manifest = reader.read_json_key(
            self.quiz_filepath,
            "manifest"
        )
        self.quiz_levels = reader.read_json_key(
            self.quiz_filepath,
            "levels"
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
        self.formatted_levels = self._build_formatted_levels()
        self.dh_levels = self._build_dh_level()

    def _build_formatted_levels(self) -> list[dict]:
        self._append_quiz_duration(self.quiz_levels)
        return self.quiz_levels

    def _append_quiz_duration(
            self,
            levels: list[dict]) -> None:
        quiz_duration = self.quiz_manifest["quiz_duration"]
        for index in range(len(levels)):
            levels[index]["manifest"]["quiz_duration"] = \
                quiz_duration

    def _build_dh_level(self) -> list[LevelInstance]:
        dh_levels = []
        for index, data in enumerate(self.formatted_levels):
            level_class = self._get_level_class(index)
            quiz_duration = data["manifest"]["quiz_duration"]
            level_object = level_class(
                self.quiz_dirpath,
                data,
                quiz_duration
            )
            dh_levels.append(level_object)
        return dh_levels

    def _get_level_class(self, index: int) -> LevelClass:
        level_type_id \
            = self.formatted_levels[index]["manifest"]["level_type_id"]
        level_class = self.level_type_id_to_dh_class[level_type_id]
        return level_class

    def get_dh_levels(self) -> list[LevelInstance]:
        return self.dh_levels
