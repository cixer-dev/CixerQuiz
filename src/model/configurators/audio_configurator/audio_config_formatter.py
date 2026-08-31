from src.model.configurators.audio_configurator import \
    audio_config_reader
from src.model.translation_handler import _


def get_formatted_volume_key_to_value() -> dict[str, int]:
    """Return a translated mapping of title-cased volume keys to \
        percentage values."""
    ui_volume_titles = [
        _("Sound effects volume"),
        _("Music volume"),
    ]
    volume_values = _get_volume_values()
    volume_key_to_value = {}
    for title, volume_value in zip(ui_volume_titles, volume_values):
        volume_key_to_value[title] = volume_value
    return volume_key_to_value


def _get_volume_values() -> list[int]:
    """Return a list with the volume values."""
    audio_config_content = audio_config_reader.\
        read_audio_config_content()
    volume_values_percent = list(audio_config_content.values())
    volume_values = [
        int(volume_value * 100)
        for volume_value in volume_values_percent
    ]
    return volume_values
