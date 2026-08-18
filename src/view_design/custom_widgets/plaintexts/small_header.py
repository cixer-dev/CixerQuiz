from PySide6 import QtWidgets as QtW


class SmallHeader(QtW.QPlainTextEdit):
    """QPlainTextEdit widget with small text display."""

    def __init__(self, text):
        super().__init__(text)
