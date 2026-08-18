from PySide6 import QtWidgets as QtW
from PySide6 import QtCore as QtC


class BigHeader(QtW.QPlainTextEdit):
    """QPlainTextEdit widget with large text display."""

    def __init__(self, text):
        super().__init__(text)


class BigHeaderColored(QtW.QLabel):
    """QLabel widget with large text display and center alignment."""

    def __init__(self, text):
        super().__init__(text)
        self.setAlignment(QtC.Qt.AlignmentFlag.AlignCenter)
