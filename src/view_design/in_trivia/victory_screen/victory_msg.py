from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class VictoryMsg(QtW.QLabel):
    def __init__(self):
        super().__init__(_("You win!"))
