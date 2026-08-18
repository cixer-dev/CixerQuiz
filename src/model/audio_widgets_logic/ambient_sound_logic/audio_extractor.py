import os
import random

from src.model.configurators.accepted_formats_configurator import \
    accepted_formats_reader
from src.model.configurators.standard_paths_configurator import \
    standard_path_reader
from src.model.data_structure_formatter import paths_formatter

music_path = standard_path_reader.read_standard_path("music_folder")


def get_audio_paths() -> list[str]:
    """Return list of audio file paths found in the standard music path."""
    valid_audio_formats = accepted_formats_reader.read_accepted_formats(
        "AUDIO"
    )
    audio_paths = []
    audio_names = os.listdir(music_path)
    for audio_name in audio_names:
        audio_suffix = paths_formatter.get_suffix(audio_name)
        if audio_suffix in valid_audio_formats:
            audio_path = os.path.join(music_path, audio_name)
            audio_paths.append(audio_path)
    return audio_paths


def get_random_audio_path() -> str:
    """Return a randomly selected audio file path."""
    audio_path = get_audio_paths()
    audio_path = random.choice(audio_path)
    return audio_path
