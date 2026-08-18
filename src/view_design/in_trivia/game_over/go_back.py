from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class GoBack(QtW.QPushButton):
    """Generic QPushButton for returning to the main menu."""

    def __init__(self):
        super().__init__(_("Go to main menu"))
