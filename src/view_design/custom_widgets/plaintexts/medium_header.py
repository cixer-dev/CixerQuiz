from PySide6 import QtWidgets as QtW


class MediumHeader(QtW.QPlainTextEdit):
    """QPlainTextEdit widget with medium text display."""

    def __init__(self, text):
        super().__init__(text)
