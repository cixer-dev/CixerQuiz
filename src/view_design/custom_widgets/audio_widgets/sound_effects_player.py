from PySide6 import QtMultimedia as QtM

from src.model.configurators.assets_paths_configurator\
    import assets_paths_reader
from src.model.configurators.audio_configurator\
    import audio_config_reader


class SoundEffectsPlayer(QtM.QMediaPlayer):
    """Play sound effects with volume controlled from configuration."""

    def __init__(self):
        super().__init__()

        self.volume_value = audio_config_reader.read_volume_value(
            "sound_effects_volume"
        )

        self.audio_output = QtM.QAudioOutput()
        self.setAudioOutput(self.audio_output)

        self.audio_output.setVolume(self.volume_value)

    def play_sound_effect(self, sound_effect_key):
        sound_effect_path = assets_paths_reader.read_asset_path(
            sound_effect_key
        )
        self.setSource(sound_effect_path)
        self.play()
