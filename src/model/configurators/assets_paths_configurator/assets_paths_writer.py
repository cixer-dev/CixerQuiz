from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.configurators.assets_paths_configurator import \
    assets_paths_formatter
from src.model.data_structure_formatter import paths_formatter
from src.model.json_wrapper.writer import JsonOverwriter


assets_paths = standard_path_reader.\
    read_standard_path("path_to_assets_paths")


def set_asset_path(asset_key: str, asset_path: str) -> None:
    """Persist an asset path by converting it to a parts list and \
        overwriting JSON."""
    asset_path_parts = paths_formatter.path_to_parts(asset_path)
    asset_path_json_overwriter = JsonOverwriter(
        assets_paths,
        asset_key,
        asset_path_parts,
    )
    asset_path_json_overwriter.overwrite_json_key()


def set_asset_path_from_title(
    asset_path_title: str,
    asset_path: str
) -> None:
    asset_path_key \
        = assets_paths_formatter.get_asset_path_key(asset_path_title)
    if asset_path_key:
        set_asset_path(asset_path_key, asset_path)
