from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class VictoryLabel(QtW.QLabel):
    """A QLabel displaying a localized victory message"""

    def __init__(self):
        super().__init__(_("VICTORY!"))
