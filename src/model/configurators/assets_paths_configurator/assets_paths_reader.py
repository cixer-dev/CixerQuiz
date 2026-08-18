import os

from src.model.configurators.standard_paths_configurator.\
    standard_path_reader import read_standard_path
from src.model.json_wrapper import reader

path_to_assets_paths = read_standard_path("path_to_assets_paths")


def read_asset_path(asset_key: str) -> str:
    """Return the assembled asset path from the asset paths JSON."""
    asset_path_parts = reader.read_json_key(
        path_to_assets_paths, asset_key
    )
    asset_path = os.path.join(*asset_path_parts)
    return asset_path


def read_assets_paths_content() -> dict[str, list[str]]:
    """Return the asset paths JSON content."""
    assets_paths_content = reader.read_json(path_to_assets_paths)
    return assets_paths_content
