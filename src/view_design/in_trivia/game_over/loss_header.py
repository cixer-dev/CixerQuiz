from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class LossHeader(QtW.QLabel):
    """QLabel displaying game over message."""

    def __init__(self) -> None:
        super().__init__(_("GAME OVER"))
