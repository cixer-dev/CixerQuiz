from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.data_structure_formatter import paths_formatter
from src.model.json_wrapper.writer import JsonOverwriter


assets_paths = standard_path_reader.\
    read_standard_path("path_to_assets_paths")


def set_asset_filepath(asset_key: str, asset_filepath: str) -> None:
    """Persist an asset filepath by converting it to a parts list and \
        overwriting JSON."""
    asset_filepath_parts = paths_formatter.path_to_parts(asset_filepath)
    asset_filepath_json_overwriter = JsonOverwriter(
        assets_paths,
        asset_key,
        asset_filepath_parts,
    )
    asset_filepath_json_overwriter.overwrite_json_key()
