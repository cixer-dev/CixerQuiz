from src.model.configurators.standard_paths_configurator import \
    standard_path_reader, standard_paths_formatter
from src.model.data_structure_formatter import paths_formatter
from src.model.json_wrapper.writer import JsonOverwriter


standard_paths = standard_path_reader.get_path_to_standard_paths()


def set_standard_filepath(
    standard_path_key: str,
    standard_filepath: str
) -> None:
    """Update the standard path value for the given key in standard path \
        JSON."""
    standard_filepath_parts = paths_formatter.path_to_parts(standard_filepath)
    standard_filepath_json_overwriter = JsonOverwriter(
        standard_paths,
        standard_path_key,
        standard_filepath_parts,
    )
    standard_filepath_json_overwriter.overwrite_json_key()


def set_standard_filepath_from_title(
    standard_path_title: str,
    standard_filepath: str
) -> None:
    standard_path_key \
        = standard_paths_formatter.get_standard_path_key(standard_path_title)
    if standard_path_key:
        set_standard_filepath(standard_path_key, standard_filepath)
