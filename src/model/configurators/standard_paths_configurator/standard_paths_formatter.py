from src.model.data_structure_formatter import paths_formatter

from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.translation_handler import _


def get_formatted_title_to_standard_path() -> dict:
    """Return translated mapping of titles to formatted standard paths."""
    ui_titles = [
        _("Accepted formats\nJSON path"),
        _("Audio config\npath"),
        _("Backgrounds\npath"),
        _("Current config\npath"),
        _("Default config\ncopy path"),
        _("General config\npath"),
        _("Music folder\npath"),
        _("Path to assets\npaths"),
        _("Pinned trivias\nlist path"),
        _("Root dir trivias\npath"),
        _("Thanks beta\nplaintext path"),
        _("Translations dir\npath")
    ]
    standard_paths = _get_standard_paths()
    title_to_standard_path: dict = {}
    for title, standard_path in zip(
        ui_titles,
        standard_paths
    ):
        title_to_standard_path[title] = standard_path
    return title_to_standard_path


def _get_standard_paths() -> list[str]:
    """Return standard paths in parts."""
    standard_paths_content = \
        standard_path_reader.read_standard_paths_content()
    standard_paths_parts = list(standard_paths_content.values())
    standard_paths = _build_standard_paths(standard_paths_parts)
    return standard_paths


def _build_standard_paths(standard_paths_parts: list[list[str]]) -> list[str]:
    standard_paths = []
    for standard_path_parts in standard_paths_parts:
        standard_path = paths_formatter.parts_to_path(
            standard_path_parts
        )
        standard_paths.append(standard_path)
    return standard_paths
