from src.model.configurators.assets_paths_configurator import \
    assets_paths_reader
from src.model.data_structure_formatter import paths_formatter
from src.model.translation_handler import _


def build_formatted_title_to_asset_path() -> dict[str, str]:
    """Return a translated mapping from translated UI titles to formatted \
asset paths."""
    assets_paths_parts = _get_assets_paths_parts()
    ui_titles = [
        _("Add file\nicon path"),
        _("Add icon path"),
        _("Current QSS\nstyle path"),
        _("Delete icon\npath"),
        _("Game logo path"),
        _("Github logo"),
        _("Pinned icon\npath"),
        _("Push button\nsound effect path"),
        _("Reduced game\nlogo path"),
        _("Start icon\npath"),
        _("Unpin icon\npath"),
    ]
    title_to_asset_path = {}
    for title, asset_path_parts in zip(ui_titles, assets_paths_parts):
        asset_path = paths_formatter.parts_to_path(asset_path_parts)
        title_to_asset_path[title] = asset_path
    return title_to_asset_path


def _get_assets_paths_parts() -> list[list[str]]:
    """Return a list with the asset paths."""
    assets_paths_content = assets_paths_reader.read_assets_paths_content()
    assets_paths = list(assets_paths_content.values())

    return assets_paths
