from src.model.data_structure_formatter import paths_formatter
from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper.writer import JsonOverwriter


standard_paths = standard_path_reader.get_path_to_standard_paths()


def set_standard_filepath(
    standard_path_key: str,
    standard_filepath: list[str]
) -> None:
    """Update the standard path value for the given key in standard path \
        JSON."""
    standard_filepath_json_overwriter = JsonOverwriter(
        standard_paths,
        standard_path_key,
        standard_filepath,
    )
    standard_filepath_json_overwriter.overwrite_json_key()


def set_absolute_project_path(absolute_project_path: str) -> None:
    """Update the standard absolute project path in standard paths JSON."""
    absolute_project_parts = paths_formatter.path_to_parts(
        absolute_project_path
    )
    set_standard_filepath("absolute_project_path", absolute_project_parts)
