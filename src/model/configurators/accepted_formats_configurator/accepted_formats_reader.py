from src.model.configurators.standard_paths_configurator.\
    standard_path_reader import read_standard_path
from src.model.json_wrapper import reader

accepted_filepath_formats = read_standard_path("accepted_filepath_formats")


def read_accepted_formats_content() -> dict[str, list[str]]:
    """Return the accepted formats JSON content from the configured path."""
    accepted_formats_content = reader.read_json(accepted_filepath_formats)
    return accepted_formats_content


def read_accepted_formats(asset_key: str) -> list[str]:
    """Return the accepted formats list for the given asset key."""
    accepted_formats_content = read_accepted_formats_content()
    accepted_formats = accepted_formats_content[asset_key]
    return accepted_formats
