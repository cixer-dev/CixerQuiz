from PySide6 import QtMultimedia as QtM

from src.model.audio_widgets_logic.ambient_sound_logic import audio_extractor
from src.model.configurators.audio_configurator import audio_config_reader


class AmbientSoundPlayer(QtM.QMediaPlayer):
    """Play ambient audio in a loop by selecting tracks of audio extractor."""

    def __init__(self):
        super().__init__()

        self.audio_path = audio_extractor.get_random_audio_path()
        self.volume_value = audio_config_reader.read_volume_value(
            "music_volume"
        )

        self.audio_output = QtM.QAudioOutput()
        self.setAudioOutput(self.audio_output)

        self.setSource(self.audio_path)
        self.audio_output.setVolume(self.volume_value)

        self.mediaStatusChanged.connect(self._on_media_status_changed)

        self.play()

    def _on_media_status_changed(self, status):
        if status == QtM.QMediaPlayer.MediaStatus.EndOfMedia:
            self.audio_path = audio_extractor.get_random_audio_path()
            self.setSource(self.audio_path)
            self.play()
