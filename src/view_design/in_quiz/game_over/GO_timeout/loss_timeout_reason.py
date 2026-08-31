from PySide6 import QtWidgets as QtW

from src.model.translation_handler import _


class LossTimeoutReasonExplanation(QtW.QLabel):
    """QLabel displaying timeout expiration message."""

    def __init__(self):
        super().__init__(_("Time is up"))
