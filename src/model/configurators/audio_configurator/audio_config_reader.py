from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.json_wrapper import reader

audio_config_path = standard_path_reader.\
    read_standard_path("audio_config_path")


def read_audio_config_content() -> dict[str, float]:
    """Return the audio configuration JSON content from the configured path."""
    audio_config_content = reader.read_json(audio_config_path)
    return audio_config_content


def read_volume_value(volume_key: str) -> float:
    """Return the volume value for the given volume key."""
    volume_value = reader.read_json_key(audio_config_path, volume_key)
    return volume_value
