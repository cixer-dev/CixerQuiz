from PySide6 import QtCore as QtC
from PySide6 import QtGui as QtG
from PySide6 import QtMultimedia as QtM
from PySide6 import QtMultimediaWidgets as QtMW


class InteractiveVideo(QtMW.QVideoWidget):
    """A video widget backed by QMediaPlayer with play/pause and \
        end-of-media looping."""

    is_pressed = QtC.Signal(object)

    def __init__(self, video_path):
        super().__init__()
        self.video_path = video_path
        self.player = QtM.QMediaPlayer(self)
        self.player.setVideoOutput(self)
        self.player.setSource(video_path)
        self.refresh_player()
        self.player.mediaStatusChanged.connect(self._on_media_status_changed)
        self.play_player()

    def refresh_player(self):
        self.player.play()
        self.player.pause()

    def pause_player(self):
        self.player.pause()

    def play_player(self):
        self.player.play()

    def mousePressEvent(self, event: QtG.QMouseEvent) -> None:
        super().mousePressEvent(event)
        if event.button() == QtC.Qt.MouseButton.LeftButton:
            state = self.player.playbackState()
            if state == QtM.QMediaPlayer.PlaybackState.PlayingState:
                self.player.pause()
            else:
                self.player.play()
                self.is_pressed.emit(self)

    def _on_media_status_changed(
        self,
        status: QtM.QMediaPlayer.MediaStatus
            ) -> None:
        if status == QtM.QMediaPlayer.MediaStatus.EndOfMedia:
            self.player.setPosition(0)
            self.player.play()
