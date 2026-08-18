from PySide6 import QtWidgets as QtW


class HugeHeader(QtW.QPlainTextEdit):
    """QPlainTextEdit widget with huge text display."""

    def __init__(self, text):
        super().__init__(text)
