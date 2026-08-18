from PySide6 import QtWidgets as QtW


class SignalizedOkButton(QtW.QPushButton):
    """Generic QPushButton for confirming operations."""

    def __init__(self):
        super().__init__("OK")
