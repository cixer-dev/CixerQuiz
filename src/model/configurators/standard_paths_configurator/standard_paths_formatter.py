from typing import Optional

from src.model.translation_handler import _
from src.model.configurators.standard_paths_configurator import \
    standard_path_reader


TITLES_TO_STANDARD_KEYS = {
    _("Accepted formats\nJSON path"): "accepted_filepath_formats",
    _("Audio config\npath"): "audio_config_path",
    _("Backgrounds\npath"): "backgrounds_path",
    _("Current config\npath"): "current_config_path",
    _("Default config\ncopy path"): "default_config_copy",
    _("General config\npath"): "general_config_path",
    _("Music folder\npath"): "music_folder",
    _("Path to assets\npaths"): "path_to_assets_paths",
    _("Pinned quizzes\nlist path"): "pinned_quizzes_list",
    _("Root dir quizzes\npath"): "root_dir_quizzes_path",
    _("Translations dir\npath"): "translations_dir",
}


def get_formatted_title_to_standard_path() -> dict:
    """Return translated mapping of titles to formatted standard paths."""
    title_to_standard_path = {}
    for title, standard_key in TITLES_TO_STANDARD_KEYS.items():
        standard_path = standard_path_reader.read_standard_path(standard_key)
        title_to_standard_path[title] = (
            standard_path
        )
    return title_to_standard_path


def get_standard_path_key(
    standard_path_title: str,
) -> Optional[str]:
    """Return the standard path key, or None if the title is not found."""
    return TITLES_TO_STANDARD_KEYS.get(standard_path_title)
