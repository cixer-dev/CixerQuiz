from typing import Any

from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper import reader


general_config_path = standard_path_reader.read_standard_path(
    "general_config_path"
)


def read_general_config(general_config_key: str) -> Any:
    """Return the specified configuration value from general config JSON."""
    general_config = reader.read_json_key(
        general_config_path,
        general_config_key
    )
    return general_config
