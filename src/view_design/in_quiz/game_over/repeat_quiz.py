from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class RepeatQuiz(QtW.QPushButton):
    """Generic QPushButton for replaying the quiz."""

    def __init__(self):
        super().__init__(_("Replay quiz"))
