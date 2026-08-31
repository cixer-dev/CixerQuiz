from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper.writer import JsonOverwriter


general_config_path = standard_path_reader.read_standard_path(
    "general_config_path"
)


def set_general_config(config_key: str, config_value: str) -> None:
    """Update the specified key in the general configuration JSON."""
    json_overwriter = JsonOverwriter(
        general_config_path,
        config_key,
        config_value,
    )
    json_overwriter.overwrite_json_key()
