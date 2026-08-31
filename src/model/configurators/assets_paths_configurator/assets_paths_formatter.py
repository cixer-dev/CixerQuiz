from typing import Optional

from src.model.configurators.assets_paths_configurator import (
    assets_paths_reader,
)
from src.model.data_structure_formatter import paths_formatter
from src.model.translation_handler import _


TITLES_TO_ASSET_KEYS = {
    _("Add file\nicon path"): "add_file_icon_path",
    _("Add icon path"): "add_icon_path",
    _("Current QSS\nstyle path"): "current_qss_style_path",
    _("Delete icon\npath"): "delete_icon_path",
    _("Game logo (ICO) path"): "reduced_game_logo_ico",
    _("Game logo (SVG) path"): "complete_game_logo",
    _("Github logo"): "github_logo",
    _("Pinned icon\npath"): "pinned_icon_path",
    _("Push button\nsound effect path"): "push_button_sound_effect",
    _("Star logo path"): "star_logo",
    _("Start icon\npath"): "start_icon_path",
    _("Unpin icon\npath"): "unpin_icon_path",
}


def get_title_to_asset_path() -> dict[str, str]:
    """Return translated mapping of titles to formatted asset paths."""
    assets_paths_content = (
        assets_paths_reader.read_assets_paths_content()
    )

    title_to_asset_path = {}

    for title, asset_key in TITLES_TO_ASSET_KEYS.items():
        asset_path_parts = assets_paths_content[asset_key]
        asset_path = paths_formatter.parts_to_path(asset_path_parts)
        title_to_asset_path[title] = asset_path

    return title_to_asset_path


def get_asset_path_key(
    asset_path_title: str,
) -> Optional[str]:
    """Return the asset path key, or None if the title is not found."""
    return TITLES_TO_ASSET_KEYS.get(asset_path_title)
