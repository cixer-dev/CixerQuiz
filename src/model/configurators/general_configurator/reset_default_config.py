import os
import shutil

from src.model.configurators.standard_paths_configurator import \
    standard_path_reader


current_config_path = standard_path_reader.read_standard_path(
    "current_config_path"
)
default_config_path = standard_path_reader.read_standard_path(
    "default_config_copy"
)


def reset_default_config() -> None:
    """Clear current configuration and restore default files."""
    clear_current_config_path()
    move_default_config_to_actual()


def clear_current_config_path() -> None:
    """Remove JSON files from the current configuration directory."""
    for filename in os.listdir(current_config_path):
        config_filepath = os.path.join(current_config_path, filename)
        if config_filepath.endswith(".json"):
            os.remove(config_filepath)


def move_default_config_to_actual() -> None:
    """Copy JSON files from default configuration to current directory."""
    for filename in os.listdir(default_config_path):
        default_config_filepath = os.path.join(
            default_config_path,
            filename
        )
        if default_config_filepath.endswith(".json"):
            shutil.copy2(default_config_filepath, current_config_path)
