from PySide6 import QtCore as QtC
from PySide6 import QtWidgets as QtW


class ProgressTimer(QtW.QProgressBar):
    """A QProgressBar animated from 0 to 100 over a fixed trivia duration and \
        emits on completion."""

    sgn_timeout = QtC.Signal()

    def __init__(self, orientation, duration):
        super().__init__()
        self.duration = duration
        self.setOrientation(orientation)
        self.setSizePolicy(
            QtW.QSizePolicy.Policy.Expanding,
            QtW.QSizePolicy.Policy.Expanding
        )
        self.setRange(0, 100)
        self.setFormat("")
        self._build_animation()

    def _build_animation(self):
        animation = QtC.QPropertyAnimation(self, b"value", self)
        animation.setDuration(self.duration)
        animation.setStartValue(0)
        animation.setEndValue(100)
        animation.finished.connect(self._on_timeout)
        animation.start()

    def _on_timeout(self):
        if self.isVisible():
            self.sgn_timeout.emit()

    def showEvent(self, event):
        super().showEvent(event)
        self._build_animation()
