from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper.writer import JsonOverwriter


audio_config_path: str = standard_path_reader.read_standard_path(
    "audio_config_path"
)


def set_volume(volume_key: str, volume_value: float) -> None:
    """Update the audio configuration value for the specified volume key in \
        general config JSON."""
    json_overwriter = JsonOverwriter(
        audio_config_path,
        volume_key,
        volume_value,
    )
    json_overwriter.overwrite_json_key()
